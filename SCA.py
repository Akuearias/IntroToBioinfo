import numpy as np

def sca(seq1, seq2):
    if len(seq1) != len(seq2):
        raise ValueError("Sequences must be of equal length.")

    # Initialize counts
    counts = {nuc: [0, 0] for nuc in "ATCG"}
    total_positions = 0

    for i in range(len(seq1)):
        if seq1[i] != 'X' and seq2[i] != 'X':
            counts[seq1[i]][0] += 1
            counts[seq2[i]][1] += 1
            total_positions += 1

    # Convert counts to frequencies
    freqs1 = np.array([counts[nuc][0] for nuc in "ATCG"]) / total_positions
    freqs2 = np.array([counts[nuc][1] for nuc in "ATCG"]) / total_positions

    # Calculate covariance matrix
    cov_matrix = np.cov(freqs1, freqs2)

    return cov_matrix


# Example usage
seq1 = "ACATTGT"
seq2 = "AXXTACX"
try:
    cov_matrix = sca(seq1, seq2)
    print("Covariance matrix:\n", cov_matrix)
except ValueError as e:
    print(e)
