import random
import matplotlib.pyplot as plt


def generate_random_sequence(length, p, q):
    base = ["Y", "R"]
    probabilities = [p, q]
    seq = ''.join(random.choices(base, probabilities, k=length))
    return seq


attempts = 20000
l = range(100, 1001, 1)
i = 1
averages = []
YRRY_moment = []
for length in l:
    for j in range(attempts):
        seq = generate_random_sequence(length, 0.5, 0.5)
        i += 1
        if seq[-4:] == "YRRY":
            YRRY_moment.append(i)
            i = 0
            break
        j += 1
    averages.append(sum(YRRY_moment) / len(YRRY_moment))

plt.plot(l, averages, marker='o', linestyle='-', color='b')

plt.title('Average distribution')
plt.xlabel('length')
plt.ylabel('average')
plt.show()


