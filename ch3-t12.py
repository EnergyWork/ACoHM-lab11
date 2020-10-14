"""
Случайная точка бросается в круг. 
Какова вероятность того, что она попадет внутрь квадрата, вписанного в круг?
Sкв / S кр = pi / 2 = 0.637
"""

import math
import random
import matplotlib.pyplot as plt

R = 5
TIMES = 10000 
TIMES_T = 50

def in_rect(point, storona):
    return True if math.fabs(point[0]) <= storona and math.fabs(point[1]) <= storona else False

def foo(t1=-1):
    points = []
    for t in range(TIMES):
        x = 2 * math.pi * random.uniform(-R, R)
        r = R * math.sqrt(random.random())
        points.append([r * math.cos(x), r * math.sin(x)])
    
    stats = [0, 0]
    for point in points:
        if in_rect(point, math.sqrt(R**2/2)):
            stats[0] += 1
        else:
            stats[1] += 1
    print(t1, stats, f'Статистически: {stats[0] / TIMES}')

    if t1 == TIMES_T - 1:
        print(f'(Tеоретически: {2 / math.pi})')
        draw(points)

def draw(points):
    cir = plt.Circle((0, 0), radius=R, color='r', fill=False)
    tmp = math.sqrt(R**2/2)
    rec = plt.Rectangle((-tmp, -tmp), tmp*2, tmp*2, fill=False)
    ax = plt.gca()
    ax.add_patch(cir)
    ax.add_patch(rec)
    plt.axis('scaled')
    plt.scatter([x[0] for x in points], [y[1] for y in points], s=0.5)
    plt.show()

def check():
    for t in range(TIMES_T):
        foo(t)

if __name__ == "__main__":
    check()