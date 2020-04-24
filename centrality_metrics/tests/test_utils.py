from centrality_metrics.utils import filter_pos, preprocess


TEST_TEXT = "Cosmology (from the Greek κόσμος, kosmos 'world' and -λογία, " \
           "-logia 'study of') is a branch of astronomy concerned with the " \
           "studies of the origin and evolution of the universe, from the " \
           "Big Bang to today and on into the future. It is the scientific " \
           "study of the origin, evolution, and eventual fate of the " \
           "universe. Absolutely. Big Apple. Running fast."


def test_filter_pos():
    assert filter_pos("I am running fast towards a library") == "library"
    assert filter_pos("") == ""


def test_preprocess_with_stopword_filtered():
    preprocessed_text = preprocess(TEST_TEXT, stop_filter=True,
                                   pos_filter=False)
    assert len(preprocessed_text) == 4

    text = ""
    preprocessed_text = preprocess(text, stop_filter=True, pos_filter=False)
    assert len(preprocessed_text) == 0


def test_preprocess_with_pos_filtered():
    preprocessed_text = preprocess(TEST_TEXT, stop_filter=False,
                                   pos_filter=True)
    assert len(preprocessed_text) == 3

    text = ""
    preprocessed_text = preprocess(text, stop_filter=False, pos_filter=True)
    assert len(preprocessed_text) == 0


def test_preprocess_with_pos_stopword_filtered():
    preprocessed_text = preprocess(TEST_TEXT, stop_filter=True,
                                   pos_filter=True)
    assert len(preprocessed_text) == 3

    text = ""
    preprocessed_text = preprocess(text, stop_filter=True, pos_filter=True)
    assert len(preprocessed_text) == 0


def test_preprocess_with_no_filter():
    preprocessed_text = \
        preprocess(TEST_TEXT, stop_filter=False, pos_filter=False)
    assert len(preprocessed_text) == 5

    text = ""
    preprocessed_text = preprocess(text, stop_filter=False, pos_filter=False)
    assert len(preprocessed_text) == 0
