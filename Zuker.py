import argparse

import numpy as np
import pandas as pd


def gap_penalty(g, alpha, beta):
    # ... affine gap penalty for gap of length g:
    return 0 if g == 0 else -alpha - beta * g


def sigma(a, b, ids, mms):
    # ... simple scoring for identities (ids) and mismatches (mms):
    return ids if a == b else mms


def score_gNW(A, B, ids, mms, alpha, beta):
    '''
    Sequence A is of length m (labeling rows)
    Sequence B is of length n (labeling columns)
    '''

    m = len(A)
    n = len(B)

    # Adding a blank space at the beginning of the string:
    A = ' ' + A
    B = ' ' + B

    # Initializing the score matrix:
    score_matrix = np.zeros([m + 1, n + 1], dtype=int)

    # Setting initial conditions:
    score_matrix[0, :] = [gap_penalty(j, alpha, beta) for j in range(score_matrix.shape[1])]
    score_matrix[:, 0] = [gap_penalty(i, alpha, beta) for i in range(score_matrix.shape[0])]

    # Calculations:
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            d = [score_matrix[i - 1, j - 1] + sigma(A[i], B[j], ids, mms)]
            g = [score_matrix[i - k, j - l] + gap_penalty(k + l, alpha, beta) for k in range(0, i + 1) for l in
                 range(0, j + 1)]
            if g:
                g = [max(g)]
            score_matrix[i, j] = max(d + g)

    print("\ngNW score matrix (for debugging):\n")
    smdf = pd.DataFrame(score_matrix)
    smdf.set_axis(list(A), axis=0)
    smdf.set_axis(list(B), axis=1)
    print(smdf)
    print("")

    return score_matrix[m, n]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-seq1', type=str, default='ATT', help="Sequence 1 (string)")
    parser.add_argument('-seq2', type=str, default='CA', help="Sequence 2 (string)")
    parser.add_argument('-ids', type=int, default=2, help="Identity score (positive INT)")
    parser.add_argument('-mms', type=int, default=2, help="Mismatch score (non-positive INT)")
    parser.add_argument('-alpha', type=int, default=1, help="alpha (non-negative INT)")
    parser.add_argument('-beta', type=int, default=1, help="beta (non-negative INT)")
    args = parser.parse_args()
    os = score_gNW(args.seq1, args.seq2, args.ids, args.mms, args.alpha, args.beta)

    print("The optimal gNW alignment score of sequences:\n", args.seq1, "\n", args.seq2)
    print("for scoring scheme ids=", args.ids, " mms=", args.mms, " w(g)=", -args.alpha, "-", args.beta, "*g")
    print("is ", os)
