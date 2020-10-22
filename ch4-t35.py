import matplotlib.pyplot as plt
import random
import numpy as np
import math
import pylab
from matplotlib import mlab

"""
После бросания 10 правильных игральных костей была обнаружена по крайней мере одна единица. 
Какова вероятность, что появилось две или более единиц?

Ответ: применя формулу условной веpоятности получим (6^10-3*5^10)/(6^10-5^10)

"""

TIMES = 1000
ps = np.array([])

class Cube:
    'Возвращает случайное число из диапазона 1-6'
    def get(self, n=None):
        if n is not None:
            return np.array([np.random.randint(1, 6) for _ in np.arange(n)])
        else:
            return np.random.randint(1, 6)

def get_p():
    units = np.array([np.sum(Cube().get(10) == 1) for _ in np.arange(TIMES)])
    res = np.sum(units > 1)
    return res / np.size(units)

def test(t=-1):
    p = get_p()
    global ps 
    ps = np.append(ps, p)
    print(t, 'Статистически:', p)

for t in np.arange(100):
    test(t)

THEOR = (6**10 - 3 * 5**10) / (6**10 - 5**10)
print('Теоретически:', THEOR)

def get_interval(ps, intervals):
    for i in range(1, len(intervals)):
        if ps >= intervals[i-1] and ps < intervals[i]:
            return i-1
    else: 
        return i-1

def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper

# first graphics
pylab.figure(1)
pylab.plot(ps, 'o', markersize=1.5)
pylab.axhline(y=THEOR, color='r', linewidth=1)
pylab.grid(True)
pylab.xlabel('Номер попытки')
pylab.ylabel('Вероятность')
pylab.legend(['Статистически', 'Теоретически'], loc='lower left', bbox_to_anchor=(-0.02, -0.27), ncol=2)
pylab.subplots_adjust(left=0.14, right=0.93, top=0.87, bottom=0.2)

# second graphic
max_stat_p = max(ps); print(max_stat_p)
min_stat_p = min(ps); print(min_stat_p)
step = (max_stat_p - min_stat_p) / 7; print(step)
intervals = np.arange(min_stat_p, max_stat_p + step, step)
print(intervals)
arr3 = [ 0 for _ in range(7) ]
for pss in ps:
    arr3[get_interval(pss, intervals)] += pss
print(arr3)

pylab.figure(2)
lb = ['{xx} - {yy}'.format(xx=truncate(intervals[i], 3), yy=truncate(intervals[i-1], 3)) for i in range(len(intervals))]
#print(lb)
ind = range(1, len(arr3) + 1)
pylab.bar(ind, arr3)
pylab.xticks(ind, lb, fontsize=7, rotation=45)
#pylab.legend(lb, loc='upper center', bbox_to_anchor=(0, 0), ncol=1)
pylab.show()
