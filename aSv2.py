def calculate_alignment_score(seq1, seq2, match=17, mismatch=-28, gap_open=-1, gap_extend=-1):
    score = 0
    gap = False
    gap_length = 0

    for a, b in zip(seq1, seq2):
        if a == '-' or b == '-':
            print(a,b)
            if not gap:
                gap = True
                gap_length = 1
            else:
                gap_length += 1
            print(gap_length)
        else:
            if gap:
                score += gap_open + gap_extend * gap_length
                print(gap_length)
                gap = False
                gap_length = 0

            if a == b:
                score += match
            else:
                score += mismatch

    if gap:
        print(gap_length,gap_open,gap_extend)
        score += gap_open + gap_extend * gap_length

    return score

seq1 = "A_"
seq2 = "_A"

alignment_score = calculate_alignment_score(seq1, seq2)
print(f"The alignment score for the sequences is: {alignment_score}")
