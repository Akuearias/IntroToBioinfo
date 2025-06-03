import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
import random
from scipy.stats import linregress

# Define parameters
G = 100000  # Genome size
R = 100  # Read length
n = 5000  # Number of reads
k_values = np.arange(1, 11)  # k values from 1 to 10
alphabet = ['A', 'C', 'G', 'T']
probabilities = [0.25, 0.25, 0.25, 0.25]

# Generate random genome sequence
genome = ''.join(random.choices(alphabet, probabilities, k=G))

# Generate random reads of length R from the genome
reads = [genome[random.randint(0, G - R):random.randint(0, G - R) + R] for _ in range(n)]


# Function to calculate k-mer coverage for a given k
def calculate_kmer_coverage(n, R, k):
    # Use the formula C_k = n * (R - k + 1) / G
    return n * (R - k + 1) / G


# Calculate C_k for different k values using the updated formula
Ck_values = [calculate_kmer_coverage(n, R, k) for k in k_values]

# Perform linear regression to estimate slope and intercept using linregress
slope, intercept, r_value, p_value, std_err = linregress(k_values, Ck_values)

# Estimated C (coverage) and G (genome size)
C_estimated = intercept  # C is the intercept
G_estimated = n * R / C_estimated  # G = n * R / C

# Print estimated values for debugging
print(f"C_k values: {Ck_values}")
print(f"Intercept (C) from linear regression: {intercept}")
print(f"Number of reads (n): {n}")
print(f"Read length (R): {R}")
print(f"Slope: {slope}, R-squared: {r_value ** 2}, p-value: {p_value}")
print(f"Estimated Coverage (C): {C_estimated}")
print(f"Estimated Genome Size (G): {G_estimated}")

# Plot C_k vs k and the fitted line
plt.plot(k_values, Ck_values, 'o-', label='C_k values')
plt.plot(k_values, intercept + slope * k_values, label=f'Fitted line: slope={slope:.2f}, intercept={intercept:.2f}')
plt.xlabel('k-mer length (k)')
plt.ylabel('Coverage (C_k)')
plt.legend()
plt.grid(True)
plt.title('C_k vs k with fitted linear model')
plt.show()
