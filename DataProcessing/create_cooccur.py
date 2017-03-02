import numpy as np
import process_utils as pu
import sys
STEPS  = 30

def main():
    print "reading bow"
    bows = np.loadtxt("../ProcessedData/unlabeled_bows.csv.gz", dtype=int)
    vocab_len = len(bows[0])
    cooccur = np.zeros((vocab_len, vocab_len), dtype=int)
    frequencies = np.zeros(vocab_len, dtype=int)
    s = len(bows) / STEPS
    print "filling matrix"
    print "[###############################]"
    sys.stdout.write("[")
    for i, bow in enumerate(bows):
        for word, n in enumerate(bow):
            cooccur[word] += bow
            frequencies[word] += 1
        if i % s == 0:
            sys.stdout.write("#")
    print "]"
    print "writing matrix and frequencies to file"
    np.savetxt("../ProcessedData/unlabeled_freq.csv.gz", frequencies, fmt="%d", delimiter=",")
    np.savetxt("../ProcessedData/unlabeled_cooccur.csv.gz", cooccur, fmt="%d", delimiter=",")
main()