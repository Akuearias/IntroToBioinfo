import random


def generate_dna_sequence(length):

    bases = ['A', 'T', 'C', 'G']

    dna_sequence = ''.join(random.choice(bases) for _ in range(length))

    return dna_sequence


# 示例用法：生成长度为50的DNA序列
length = 5
dna_sequence = generate_dna_sequence(length)
print(dna_sequence)
