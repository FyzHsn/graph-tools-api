import pytest

from centrality_metrics.text2graph import Text2Graph


DOC_1 = ["I like peaches.",
         "Peaches taste good.",
         "Ontario is known for its peaches.",
         "Blueberries like peaches are another fruit type.",
        ]

TEXT_1 = "i eat rice"
TEXT_2 = "i drink water"


@pytest.fixture
def document():
    """Create and initialize a text document and its graph.

    :return: text document
    :rtype: Text2Graph
    """

    doc_graph = Text2Graph(" ".join(DOC_1))
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
              ('rice', 'eat'): 1,
             }
    assert graph == result

    graph = document.weighted_graph(result, "i drink water", window=2)
    result = {('eat', 'i'): 1,
              ('eat', 'rice'): 1,
              ('i', 'eat'): 1,
              ('rice', 'eat'): 1,
              ('drink', 'i'): 1,
              ('i', 'drink'): 1,
              ('drink', 'water'): 1,
              ('water', 'drink'): 1,
             }

    assert graph == result


def test_weighted_graph_window_3(document):
    graph = document.weighted_graph({}, "i eat rice", window=3)

    result = {('eat', 'i'): 1,
              ('eat', 'rice'): 1,
              ('i', 'eat'): 1,
              ('rice', 'eat'): 1,
              ('i', 'rice'): 1,
              ('rice', 'i'): 1
             }
    assert graph == result


# def test_transform(document):
