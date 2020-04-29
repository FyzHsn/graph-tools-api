import pytest

from centrality_metrics.text2graph import Text2Graph
from centrality_metrics.tests.data import TEST_DOC


@pytest.fixture
def document():
    """Create and initialize a text document and its graph.

    :return: text document
    :rtype: Text2Graph
    """

    doc_graph = Text2Graph(" ".join(TEST_DOC))
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


def test_weighted_graph(document):
    text = "i eat rice. i drink water."
    graph = document.weighted_graph({}, text, window=2)
    result = {('drink', 'i'): 1,
              ('drink', 'water.'): 1,
              ('eat', 'i'): 1,
              ('eat', 'rice.'): 1,
              ('i', 'drink'): 1,
              ('i', 'eat'): 1,
              ('i', 'rice.'): 1,
              ('rice.', 'eat'): 1,
              ('rice.', 'i'): 1,
              ('water.', 'drink'): 1}
    assert graph == result
