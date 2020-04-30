import numpy as np
import re

from centrality_metrics.utils import preprocess


class InvalidWindowLength(Exception):
    pass


class Text2Graph:
    def __init__(self, text):
        """Initialize graph representation of text

        :param text: document containing text
        :type text: str
        """

        self.text = text
        self.graph = {}

    def preprocess_text(self, stop_filter=True, pos_filter=True):
        """Preprocess document text

        This method can filter out basic stopwords listed in the utils file
        and parts of speech.

        :param stop_filter: stopword filter status
        :type stop_filter: bool
        :param pos_filter: parts of speech filter status
        :type pos_filter: bool
        """

        preprocessed_sentence_list = preprocess(self.text,
                                                stop_filter=stop_filter,
                                                pos_filter=pos_filter)
        self.text = ". ".join(preprocessed_sentence_list) + "."

    @staticmethod
    def weighted_graph(graph, text, window=2):
        """Convert text to graph

        This method updates a graph according to the frequency of
        co-occurrence of words within the specified window.

        :param graph: graph that has to updated
        :type graph: dict(tuple: int)
        :param text: sentence
        :type text: str
        :param window: window of word/node co-occurrence
        :return: updated graph
        :rtype: dict(tuple: int)
        """

        text += " PADPAD" * (window - 2)
        text = text.split()

        def update_collocation_weights(graph, text, i, j):
            text_ij = (text[i], text[j])

            if text_ij in graph.keys() and "PADPAD" not in text_ij:
                graph[text_ij] += 1
            elif text_ij not in graph.keys() and "PADPAD" not in text_ij:
                graph[text_ij] = 1

            return graph

        for i in range(0, len(text) - window + 1):
            for j in range(i + 1, i + window):
                graph = update_collocation_weights(graph, text, i, j)
                graph = update_collocation_weights(graph, text, j, i)

        return graph

    def transform(self, window=2):
        """Transform document to graph

        This method transforms a document to a weighted graph by examining
        each sentence and frequency of mutually occurring terms within a
        specified window.

        :param window: Right window to each word (node) within which to
        other nodes are considered to be co-occurring.
        :type window: int
        """

        if window < 2:
            raise InvalidWindowLength("Window length should be greater than or equal to 2")

        for sentence in re.split("[?.]", self.text):
            self.graph = self.weighted_graph(self.graph, sentence, window)

    def degree_centrality(self):
        """Compute degree centrality

        This method computes the degree centrality of each node in the graph.

        :return: centrality measure of each node (word)
        :rtype: list of tuples
        """

        node_score = {}

        for (node_1, node_2), weight_12 in self.graph.items():
            if node_1 not in node_score.keys():
                node_score[node_1] = weight_12
            else:
                node_score[node_1] += weight_12

        return sorted([(n, np.round(s, 2)) for (n, s) in node_score.items()],
                      key=lambda x: x[1],
                      reverse=True)

    def normalized_degree_centrality(self):
        """Compute normalized degree centrality

        This method computes the normalized degree centrality of each node
        in the graph.

        :return: each node (word) and its corresponding normalized centrality
        score
        :rtype: list of tuples
        """

        node_score = self.degree_centrality()
        node_num = len(node_score) - 1
        return [(n, np.round(s / node_num, 2)) for (n, s) in node_score]
