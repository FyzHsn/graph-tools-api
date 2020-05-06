import pytest

from centrality_metrics.text2graph import InvalidWindowLength, Text2Graph


DOC = "I eat rice. I drink water."

TEXT_1 = "i eat rice"
TEXT_2 = "i drink water"

GRAPH_12 = {('eat', 'i'): 1,
            ('eat', 'rice'): 1,
            ('i', 'eat'): 1,
            ('rice', 'eat'): 1,
            ('drink', 'i'): 1,
            ('i', 'drink'): 1,
            ('drink', 'water'): 1,
            ('water', 'drink'): 1}


@pytest.fixture
def document():
    """Create and initialize a text document and its graph.

    :return: text document
    :rtype: Text2Graph
    """

    doc_graph = Text2Graph(DOC)
    return doc_graph


def test_doc_graph_init(document):
    assert document.graph == {}


def test_preprocess(document, monkeypatch):
    def mock_preprocess(*args, **kwargs):
        return ["this part was patched", "this part was also patched"]

    monkeypatch.setattr("centrality_metrics.text2graph.preprocess",
                        mock_preprocess)
    document.preprocess_text()
    assert document.text == "this part was patched. this part was also " \
                            "patched."


def test_weighted_graph_window_2(document):
    graph = document.weighted_graph({}, "i eat rice", window=2)
    result = {('eat', 'i'): 1,
              ('eat', 'rice'): 1,
              ('i', 'eat'): 1,
              ('rice', 'eat'): 1}
    assert graph == result

    graph = document.weighted_graph(result, "i drink water", window=2)
    assert graph == GRAPH_12


def test_weighted_graph_window_3(document):
    graph = document.weighted_graph({}, "i eat rice", window=3)
    result = {('eat', 'i'): 1,
              ('eat', 'rice'): 1,
              ('i', 'eat'): 1,
              ('rice', 'eat'): 1,
              ('i', 'rice'): 1,
              ('rice', 'i'): 1}
    assert graph == result


def test_transform_invalid_window_length(document):
    with pytest.raises(InvalidWindowLength):
        document.transform(window=1)


def test_transform(document):
    document.text = "i eat rice. i drink water."
    assert document.graph == {}

    document.transform(window=2)
    assert document.graph == GRAPH_12


def test_degree_centrality(document):
    document.graph = GRAPH_12
    assert document.degree_centrality() == \
           [('eat', 2), ('i', 2), ('drink', 2), ('rice', 1), ('water', 1)]


def test_normalized_degree_centrality(document, monkeypatch):
    monkeypatch.setattr(Text2Graph, "degree_centrality",
                        lambda *args, **kwargs:
                        [('apple', 1), ('orange', 1), ('fruits', 1.0)])
    assert document.normalized_degree_centrality() == \
           [('apple', 0.50), ('orange', 0.50), ('fruits', 0.50)]

    monkeypatch.setattr(Text2Graph, "degree_centrality",
                        lambda *args, **kwargs: [('a', 1.0)])
    assert document.normalized_degree_centrality() == [('a', 1.0)]
