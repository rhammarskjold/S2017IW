import numpy as np
import process_utils as pu


def parseFile(fname, labeled=False):
    file = open(fname)

def main():
    print "reading vocabulary"
    vocab_list, vocab_dict = pu.read_in_vocab("../ProcessedData/vocab_10.csv")
    files = pu.get_all_unlabeled()
    bows = []
    print "parsing files"
    for fname in ["../SentenceCorpus/unlabeled_articles/arxiv_unlabeled/1.txt"]:
        full_text = (open(fname)).read()
        full_text = full_text.replace("### abstract ###\n", "")
        full_text = full_text.replace("### introduction ###\n", "")
        sentences = full_text.splitlines()
        for sentence in sentences:
            bow = np.zeros(len(vocab_list))
            words = pu.get_words(sentence)
            for word in words:
                if word in vocab_dict.keys():
                    bow[vocab_dict[word]] += 1
            bows.append(bow)
    print "writing bow file"
    np.savetxt("../ProcessedData/unlabeled_bows.csv.gz", bows, fmt="%d")
main()