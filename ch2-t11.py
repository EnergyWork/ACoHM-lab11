import numpy as np
import matplotlib.pyplot as plt
import time
from threading import Thread
import pylab
from matplotlib import mlab
import math

TIMES = 10000
TIMES_2 = 210
N = 1000
THEOR = 8*12/1000
arr = np.zeros(N-8*12)
arr2 = np.ones(8*12)
cube = np.concatenate((arr, arr2))
np.random.shuffle(cube)
res = []

def foo(t=-1):
    stats = [0, 0]
    s = np.random.randint(0, 999, size=TIMES)
    for i in s:
        if cube[i] == 1:
            stats[0] += 1
        else:
            stats[1] += 1
    f = stats[0] / TIMES
    res.append(f)
    print(t, stats, f'Статистически: {stats[0] / TIMES}')

def get_interval(ps, intervals):
    for i in range(1, len(intervals)):
        if ps >= intervals[i-1] and ps < intervals[i]:
            return i-1
    else: 
        return i-1
        # raise Exception(f'Не все р были распределены по интервалам: {ps}')

def statistics():
    st = time.time()
    for t in range(TIMES_2):
        foo(t)
    print(f'Теоретически: {THEOR}')
    print(f'--- {time.time() - st} sec ---')

    draw()
    draw2()

def draw2():
    max_stat_p = max(res); print(max_stat_p)
    min_stat_p = min(res); print(min_stat_p)
    step = (max_stat_p - min_stat_p) / 7; print(step)
    intervals = np.arange(min_stat_p, max_stat_p + step, step)
    print(intervals)
    arr3 = [ 0 for _ in range(7) ]
    for ps in res:
        arr3[get_interval(ps, intervals)] += ps
    print(arr3)
    
    pylab.figure(2)
    lb = ['{xx} - {yy}'.format(xx=truncate(intervals[i], 3), yy=truncate(intervals[i-1], 3)) for i in range(len(intervals))]
    #print(lb)
    ind = range(1, len(arr3) + 1)
    pylab.bar(ind, arr3)
    pylab.xticks(ind, lb, fontsize=7, rotation=45)
    #pylab.legend(lb, loc='upper center', bbox_to_anchor=(0, 0), ncol=1)
    pylab.show()

def draw():
    pylab.figure(1)
    pylab.plot(res, 'o', markersize=1.5)
    pylab.axhline(y=THEOR, color='r', linewidth=1)
    pylab.grid(True)
    pylab.xlabel('Номер попытки')
    pylab.ylabel('Вероятность')
    pylab.legend(['Статистически', 'Теоретически'], loc='lower left', bbox_to_anchor=(-0.02, -0.27), ncol=2)
    pylab.subplots_adjust(left=0.14, right=0.93, top=0.87, bottom=0.2)
    # pylab.show()

def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper

if __name__ == "__main__":
    # foo()
    statistics()
    # stoppp = input('Программа приостановлена')
