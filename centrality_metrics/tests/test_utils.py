from centrality_metrics.utils import preprocess


def test_preprocess_with_stopword_filtered():
    text = "Cosmology (from the Greek κόσμος, kosmos 'world' and -λογία, " \
           "-logia 'study of') is a branch of astronomy concerned with the " \
           "studies of the origin and evolution of the universe, from the " \
           "Big Bang to today and on into the future. It is the scientific " \
           "study of the origin, evolution, and eventual fate of the " \
           "universe."

    preprocessed_text = preprocess(text, stop_filter=True, pos_filter=False)
    assert len(preprocessed_text) == 2

    text = ""
    preprocessed_text = preprocess(text, stop_filter=True, pos_filter=False)
    assert len(preprocessed_text) == 0


def test_preprocess_with_pos_filtered():
    text = "Cosmology (from the Greek κόσμος, kosmos 'world' and -λογία, " \
           "-logia 'study of') is a branch of astronomy concerned with the " \
           "studies of the origin and evolution of the universe, from the " \
           "Big Bang to today and on into the future. It is the scientific " \
           "study of the origin, evolution, and eventual fate of the " \
           "universe."

    preprocessed_text = preprocess(text, stop_filter=False, pos_filter=True)
    assert len(preprocessed_text) == 2

    text = ""
    preprocessed_text = preprocess(text, stop_filter=False, pos_filter=True)
    assert len(preprocessed_text) == 0


def test_preprocess_with_pos_stopword_filtered():
    text = "Cosmology (from the Greek κόσμος, kosmos 'world' and -λογία, " \
           "-logia 'study of') is a branch of astronomy concerned with the " \
           "studies of the origin and evolution of the universe, from the " \
           "Big Bang to today and on into the future. It is the scientific " \
           "study of the origin, evolution, and eventual fate of the " \
           "universe."

    preprocessed_text = preprocess(text)
    assert len(preprocessed_text) == 2

    text = ""
    preprocessed_text = preprocess(text)
    assert len(preprocessed_text) == 0


def test_preprocess_with_no_filter():
    text = "Cosmology (from the Greek κόσμος, kosmos 'world' and -λογία, " \
           "-logia 'study of') is a branch of astronomy concerned with the " \
           "studies of the origin and evolution of the universe, from the " \
           "Big Bang to today and on into the future. It is the scientific " \
           "study of the origin, evolution, and eventual fate of the " \
           "universe."

    preprocessed_text = preprocess(text, stop_filter=False, pos_filter=False)
    assert len(preprocessed_text) == 2

    text = ""
    preprocessed_text = preprocess(text, stop_filter=False, pos_filter=False)
    assert len(preprocessed_text) == 0
