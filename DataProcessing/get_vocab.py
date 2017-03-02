import process_utils as utils
import numpy as np
FREQUENCY_CUTOFF = 10

def main():
    word_counts = dict()

    for fname in utils.get_all_unlabeled():

        text = (open(fname)).read()
        for word in utils.get_words(text):
            if word in word_counts.keys():
                word_counts[word] += 1
            else:
                word_counts[word] = 1

    vocab = []
    for word, word_count in word_counts.iteritems():
        if word_count >= FREQUENCY_CUTOFF:
            vocab.append(word)
    np.savetxt("./vocab_" + str(FREQUENCY_CUTOFF) + ".csv", vocab, fmt="%s")
main()