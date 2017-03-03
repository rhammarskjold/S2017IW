import numpy as np
import process_utils as pu

LABEL_DICT = {"misc": 0, "ownx": 1, "aimx": 2, "cont": 3, "base": 4}

def main():
    print "reading vocabulary"
    vocab_list, vocab_dict = pu.read_in_vocab("../ProcessedData/vocab_10.csv")
    files = pu.get_all_labeled()
    bows = []
    classes = []
    print "parsing files"
    for fname in files:
        full_text = (open(fname)).read()
        full_text = full_text.replace("### abstract ###\n", "")
        full_text = full_text.replace("### introduction ###\n", "")
        sentences = full_text.splitlines()
        for sentence in sentences:
            bow = np.zeros(len(vocab_list))
            words = pu.get_words(sentence)
            try:
                classes.append(LABEL_DICT[words[0]])
            except KeyError:
                print fname
            words = words[1:]
            for word in words:
                if word in vocab_dict.keys():
                    bow[vocab_dict[word]] += 1
            bows.append(bow)
    print "writing bow file"
    np.savetxt("../ProcessedData/labeled_bows.csv", bows, fmt="%d", delimiter=",")
    np.savetxt("../ProcessedData/labeled_classes.csv", classes, fmt="%d", delimiter=",")
main()