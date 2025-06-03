import pandas as pd
import numpy as np


def gap_penalty(g, alpha, beta):
    return 0 if g == 0 else -alpha - beta * g


def sigma(a, b, ids, mms):
    return ids if a == b else mms


def score_NW(A, B, ids, mms, alpha, beta):
    m = len(A)
    n = len(B)

    A = ' ' + A
    B = " " + B

    score_matrix = np.zeros([m+1, n+1], dtype=int)

    score_matrix[0, :] = [gap_penalty(j, alpha, beta) for j in range(score_matrix.shape[1])]
    score_matrix[:, 0] = [gap_penalty(j, alpha, beta) for j in range(score_matrix.shape[0])]

    for i in range(1, m+1):
        for j in range(1, n+1):
            d = [score_matrix[i-1, j-1] + sigma(A[i], B[j], ids, mms)]
            h = [score_matrix[i-1, j-1-k] + sigma(A[i], B[j-k], ids, mms) + gap_penalty(k, alpha, beta) for k in
                 range(1, j)]
            v = [score_matrix[i-1-l, j-1] + sigma(A[i-l], B[j], ids, mms) + gap_penalty(l, alpha, beta) for l in
                 range(1, i)]
            score_matrix[i, j] = max(d+h+v)

    smdf = pd.DataFrame(score_matrix)
    smdf.set_axis(list(A), axis=0)
    smdf.set_axis(list(B), axis=1)
    print(smdf)
    print("")

    print(score_matrix[m, n])


if __name__ == '__main__':
    n = 14
    m = 14
    mat = np.zeros([n + 1, m + 1], dtype=int)

    mat[0, :] = np.ones(m + 1)
    mat[:, 0] = np.ones(n + 1)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            mat[i][j] += sum(mat[i - 1, 0:j])
            mat[i][j] += sum(mat[0:i - 1, j - 1])

    print("\n")
    print(mat)
    print("\n")

    print(mat[-1][-1])

    score_NW("ATG_ATTCGCG___", '__GCA__CGAGCCC', ids=3, mms=-1, alpha=2, beta=2)
