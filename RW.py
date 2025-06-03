import matplotlib.pyplot as plt
import random
import numpy as np


class RandomWalk:
    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.positions = [0]

    def walk(self, positive, negative):
        steps = []
        for i in range(self.num_points):
            step = random.choices([1, -1], weights=[positive, negative])[0]
            steps.append(step)
        return steps


def MSS(points, pos, neg):
    RW = RandomWalk(num_points=points)
    walks = RW.walk(pos, neg)
    sums = []
    for i in range(1, RW.num_points + 1):
        sums.append(sum(walks[0:i]))
    return [sums.index(max(sums)), max(sums)]


rw = RandomWalk()
walks = rw.walk(0.5, 0.5)

sums = []
for i in range(1, rw.num_points + 1):
    sums.append(sum(walks[0:i]))

zeros = []
for s in range(len(sums)):
    if sums[s] == 0 and sums.index(max(sums)) - s > 0:
        zeros.append(s)

zero = zeros[-1]

E = []
for i in range(1, rw.num_points + 1):
    E.append(max(sum(walks[0:i]), 0))

ID = list(range(1, 5001))

plt.plot(ID, E)
plt.title('k-E')
plt.xlabel('k')
plt.ylabel('E')
plt.show()

plt.plot(ID, sums)
plt.title('k-S')
plt.xlabel('k')
plt.ylabel('S')
plt.show()

print("MSS start: {}; Maximum position: {}; Maximal scoring segment: {}".format(zero, E.index(max(E)), max(E)))

pos = 0.5
neg = 1 - pos
Points, MSSs = [], []

for points in range(1000, 21000, 1000):
    Points.append(points)

for points in Points:
    mss = 0
    for i in range(0, 10):
        mss = mss + MSS(points, pos, neg)[1]
    mss = mss / 10
    MSSs.append(mss)

slope, intercept = np.polyfit(Points, MSSs, 1)

np_Points = np.array(Points)
# 生成回归直线
y_fit = slope * np_Points + intercept

plt.scatter(Points, MSSs)
plt.plot(Points, y_fit, color='red')
plt.title('Relationship between S and sequence length')
plt.xlabel('sequence length')
plt.ylabel('MSS')
if slope > 0:
    print('Relationship between S and sequence length is positive correlation,'
          'with the regression equation: S = l * {} + {}'.format(slope, intercept))
elif slope < 0:
    print('Relationship between S and sequence length is negative correlation,'
          'with the regression equation: S = l * {} + {}'.format(slope, intercept))
else:
    print('S and sequence length has no correlation.')
plt.show()

poss = []
MSSs = []

for i in range(1, 10, 1):
    poss.append(i / 10)

for pos in poss:
    mss = 0
    neg = 1 - pos
    for i in range(0, 10):
        mss = mss + MSS(5000, pos, neg)[1]
    mss = mss / 10
    MSSs.append(mss)

slope, intercept = np.polyfit(poss, MSSs, 1)

np_poss = np.array(poss)
# 生成回归直线
y_fit = slope * np_poss + intercept

plt.scatter(poss, MSSs)
plt.plot(poss, y_fit, color='red')
plt.title('Relationship between S and positive probability')
plt.xlabel('positive probability')
plt.ylabel('MSS')
if slope > 0:
    print('Relationship between S and positive probability is positive correlation,'
          'with the regression equation: S = l * {} + {}'.format(slope, intercept))
elif slope < 0:
    print('Relationship between S and positive probability is negative correlation,'
          'with the regression equation: S = l * {} + {}'.format(slope, intercept))
else:
    print('S and positive probability has no correlation.')
plt.subplots_adjust(bottom=0.2)
plt.show()
