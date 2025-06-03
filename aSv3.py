import argparse

def calculate_alignment_score(seq1, seq2, number1, number2, match_score, mismatch_score):
    score = 0
    gap1 = 0  # Track gaps in seq1
    gap2 = 0  # Track gaps in seq2

    for i in range(len(seq1)):
        if seq1[i] == '_':
            gap1 += 1
            if gap2 > 0:
                score += (number1 + number2 * gap2)  # Apply custom gap penalty for seq2
                gap2 = 0  # Reset seq2 gap length
        elif seq2[i] == '_':
            gap2 += 1
            if gap1 > 0:
                score += (number1 + number2 * gap1)  # Apply custom gap penalty for seq1
                gap1 = 0  # Reset seq1 gap length
        else:
            # Process gap penalty if a gap just ended
            if gap1 > 0:
                score += (number1 + number2 * gap1)  # Apply custom gap penalty for seq1
                gap1 = 0  # Reset seq1 gap length
            if gap2 > 0:
                score += (number1 + number2 * gap2)  # Apply custom gap penalty for seq2
                gap2 = 0  # Reset seq2 gap length

            # Scoring for match/mismatch
            if seq1[i] == seq2[i]:
                score += match_score  # Match
            else:
                score += mismatch_score  # Mismatch

    # Process any remaining gap penalty at the end
    if gap1 > 0:
        score += (number1 + number2 * gap1)
    if gap2 > 0:
        score += (number1 + number2 * gap2)

    return score

if __name__ == '__main__':
    # Setting up argument parser
    parser = argparse.ArgumentParser(description="Calculate alignment score between two sequences.")
    parser.add_argument('-seq1', type=str, required=True, help="First sequence (e.g., AC_T)")
    parser.add_argument('-seq2', type=str, required=True, help="Second sequence (e.g., A_GT)")
    parser.add_argument('-match', type=int, required=True, help="Score for a match (e.g., +1)")
    parser.add_argument('-mismatch', type=int, required=True, help="Score for a mismatch (e.g., -1)")
    parser.add_argument('-start_gap', type=int, required=True, help="Custom start_gap in the format number1 (e.g., -1)")
    parser.add_argument('-gap_extend', type=int, required=True, help="Custom gap in the format number2 (e.g., -1)")

    # Parse the arguments
    args = parser.parse_args()

    # Calculate the alignment score
    alignment_score = calculate_alignment_score(args.seq1, args.seq2, args.start_gap, args.gap_extend, args.match, args.mismatch)

    # Output the score
    print(f"Alignment Score: {alignment_score}")
