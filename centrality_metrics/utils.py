import re

import nltk
from nltk.stem import PorterStemmer


STOPWORDS = {"i", "me", "us", "you", "them", "he", "she", "him", "her",
             "their", "theirs", "it", "that",

             "can", "cant", "could", "coudnt", "shall", "should",
             "shoudnt", "shant", "will", "wont", "would", "wouldnt",

             "is", "was", "were", "werent", "a", "are", "arent"

             "maybe", "perhaps", "yes", "no", "sure", "ok", "yess",
             "absolutely", "not", "ever", "never", "often", "then", "now",
             "must",

             "at", "of", "and", "or", "for", "the", "too", "to", "its",
             "and", "as", "in", "such", "an", "into", "other",
             "used", "from", "your", "be", "if",

             "when", "how", "what", "who",

             "i.e.", "o.k.",

             "&quot", "&gt", "&lt", }


def filter_pos(text):
    """Parts Of Speech Filter

    Remove words that aren't nouns or adjectives.

    :param text: text to be processed
    :type text: str
    :return: clean_text
    :rtype: str
    """

    text_pos = nltk.pos_tag(text.split())
    clean_text = ""

    for (word, tag) in text_pos:
        if ("NN" in tag) or ("ADJ" in tag) or ("JJ" in tag):
            clean_text += word + " "

    return clean_text


def preprocess(text, stop_filter=True, pos_filter=True):
    """Text preprocessor

    Clean text by removing punctuations, stopwords, non-noun and
    adjectives in addition to stemming.

    :param text: document text that needs to be preprocessed
    :type text: str
    :param stop_filter: stopword filter status
    :type stop_filter: bool
    :param pos_filter: part of speech filter status
    :type pos_filter: bool
    :return: stemmed and preprocessed text
    :rtype: str
    """

    text = text.lower()
    text = re.sub(r"[,()\n\[\]<>;:\'\{\}]", "", text)
    sentence_list = re.split("[?.]", text)

    stemmer = PorterStemmer()
    cleaned_sentence_list = []
    for sentence in sentence_list:
        if pos_filter:
            sentence = filter_pos(sentence)

        if stop_filter:
            sentence = " ".join([word for word in sentence.split() if
                                 word not in STOPWORDS])

        sentence = " ".join([stemmer.stem(word) for word in
                             sentence.split()])
        if sentence:
            cleaned_sentence_list.append(sentence)

    return cleaned_sentence_list


if __name__ == "__main__":
    text = "Cosmology (from the Greek κόσμος, kosmos 'world' and -λογία, " \
           "-logia 'study of') is a branch of astronomy concerned with the " \
           "studies of the origin and evolution of the universe, from the " \
           "Big Bang to today and on into the future. It is the scientific " \
           "study of the origin, evolution, and eventual fate of the " \
           "universe. Absolutely. Running. Big apple."
    print(preprocess(text, False, True))

    print(filter_pos("") == "")