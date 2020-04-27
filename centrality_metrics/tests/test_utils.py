import itertools

from centrality_metrics.utils import filter_pos, preprocess

from centrality_metrics.tests.data import TEST_TEXT


def test_filter_pos():
    assert filter_pos("I am running fast towards a library") == "library"


def test_empty_strings():
    preprocessing_args = itertools.product([True, False], repeat=2)

    for stop_filter, pos_filter in preprocessing_args:
        preprocessed_text = preprocess(text="",
                                       stop_filter=stop_filter,
                                       pos_filter=pos_filter)
        assert len(preprocessed_text) == 0

    assert filter_pos("") == ""


def test_preprocess_with_stopword_filtered():
    preprocessed_text = preprocess(TEST_TEXT, stop_filter=True,
                                   pos_filter=False)
    assert len(preprocessed_text) == 4


def test_preprocess_with_pos_filtered():
    preprocessed_text = preprocess(TEST_TEXT, stop_filter=False,
                                   pos_filter=True)
    assert len(preprocessed_text) == 3


def test_preprocess_with_pos_stopword_filtered():
    preprocessed_text = preprocess(TEST_TEXT, stop_filter=True,
                                   pos_filter=True)
    assert len(preprocessed_text) == 3


def test_preprocess_with_no_filter():
    preprocessed_text = \
        preprocess(TEST_TEXT, stop_filter=False, pos_filter=False)
    assert len(preprocessed_text) == 5
