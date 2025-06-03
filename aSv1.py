def alignscore(seq1, seq2, scoring):
    n,m = len(seq1), len(seq2)
    if n < m:
        seq1 = seq1 + "_"*(m-n)
    elif m < n:
        seq2 = seq2 + "_"*(n-m)
    else:
        pass

    score = 0
    gap1 = False
    gap2 = False
    for i in range(n):
        if seq1[i] == seq2[i]:
            if gap1 or gap2:
                gap1 = False
                gap2 = False
            score += scoring["match"]
        elif seq1[i] == "_":
            if gap1:
                score += scoring["gap"]
            else:
                score += scoring["start_gap"] + scoring["gap"]
                gap1 = True
        elif seq2[i] == "_":
            if gap2:
                score += scoring["gap"]
            else:
                score += scoring["start_gap"] + scoring["gap"]
                gap2 = True
        else:
            score += scoring["mismatch"]
            gap1 = False
            gap2 = False

    return score

seq1 = "A_"
seq2 = "_A"

scoring1 = {"start_gap":-1, "gap":-1, "mismatch":-28, "match":17}
scoring2 = {"start_gap":0, "gap":0, "mismatch":0, "match":1}

print(f"scoring1: {alignscore(seq1, seq2, scoring1)}")
print(f"scoring2: {alignscore(seq1, seq2, scoring2)}")
