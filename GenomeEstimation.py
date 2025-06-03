import random
from collections import Counter
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


# (i) 生成长度为 G 的随机序列
def generate_weighted_sequence(G, probabilities):
    bases = ['A', 'T', 'C', 'G']
    sequence = ''.join(random.choices(bases, weights=probabilities, k=G))
    return sequence


def calculate_base_frequencies(sequence):
    length = len(sequence)
    base_counts = Counter(sequence)  # 统计每个碱基的出现次数
    # 计算频率
    frequencies = {base: base_counts[base] / length for base in ['A', 'T', 'C', 'G']}
    return frequencies


def calculate_ck(n, R, k, G):
    return n*(R-k+1)/G


G = 1000000
prob = [.25, .25, .25, .25]
genome = generate_weighted_sequence(G, prob)

n = 100
R = 200000
K = np.arange(4, 51, 1)

random_seqs = []
for i in range(n):
    seq = genome[random.randint(0, G-R):random.randint(0, G-R) + R]
    random_seqs.append(seq)

Cks = [calculate_ck(n, R, k, G) for k in K]

slope, intercept, r_value, p_value, std_err = linregress(K, Cks)

C_estimated = intercept

G_estimated = n*R/C_estimated

plt.scatter(K, Cks, color='b')
plt.plot(K, intercept + slope * K)

plt.show()
