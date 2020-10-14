import numpy as np
import matplotlib.pyplot as plt
import time

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

def statistics():
    st = time.time()
    for t in range(TIMES_2):
        foo(t)
    print(f'Теоретически: {THEOR}')
    print(f'--- {time.time() - st} sec ---')

    mas = np.array(res)
    # mas = sorted(mas)
    mas = np.reshape(mas, (7, 30))
    print(mas)
    mas2 = [sum(x) for x in mas]
    print(mas2)
    plt.bar(range(len(mas2)), mas2)
    plt.show()

def draw():
    plt.plot(res, 'o', markersize=1.5)
    plt.axhline(y=THEOR, color='r', linewidth=1)
    plt.grid(True)
    plt.xlabel('Номер попытки')
    plt.ylabel('Вероятность')
    plt.legend(['Статистически', 'Теоретически'], loc='lower left', bbox_to_anchor=(-0.02, -0.27), ncol=2)
    plt.subplots_adjust(left=0.14, right=0.93, top=0.87, bottom=0.2)
    plt.show()

if __name__ == "__main__":
    # foo()
    statistics()
    # draw()
