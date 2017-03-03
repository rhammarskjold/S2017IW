import re
import string
import glob

def get_all_unlabeled():
    return glob.glob("../SentenceCorpus/unlabeled_articles/*/*.txt")

REVIEWER = "1"
def get_all_labeled():
    return glob.glob("../SentenceCorpus/labeled_articles/*" + REVIEWER + ".txt")

def stem(word):
    regexp = r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)?$'
    stem, _ = re.findall(regexp, word)[0]
    return stem

def get_words(text):
    text = text.replace("### abstract ###\n", "")
    text = text.replace("### introduction ###\n", "")
    text = text.translate(None, string.punctuation)
    text = text.lower()
    return [stem(word) for word in text.split()]

def read_in_vocab(v_name):
    words = ((open(v_name)).read()).splitlines()
    vocab_list = []
    vocab_dict = dict()
    for i, w in enumerate(words):
        vocab_list.append(w)
        vocab_dict[w] = i
    return (vocab_list, vocab_dict)
