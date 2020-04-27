import pytest

from centrality_metrics.text2graph import Text2Graph
from centrality_metrics.tests.data import TEST_DOC


@pytest.fixture
def document_graph():
    """Create and initialize a text document and its graph.

    :return: text document
    :rtype: Text2Graph
    """

    doc_graph = Text2Graph(" ".join(TEST_DOC))
    return doc_graph





