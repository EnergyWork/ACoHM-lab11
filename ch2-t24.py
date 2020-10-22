import math
import copy
import numpy as np
import matplotlib.pyplot as plt

"""
Урна содержит N белых и N черных шаров. Вынимаются n раз по два шара, не возвращая вынутых шаров обратно.
Какова вероятность того, что всегда будут выниматься пары разноцветных шаров?
"""

N = 5 # int(input('input N > ')) # N white and N black
n = 3 # int(input('input n > ')) # take n times
TIMES = 1001

# C(n по k) = k! / (n! (k - n)!)
def C(n, k):
    return (math.factorial(k) / (math.factorial(n) * math.factorial(k-n)))

def p(times, h):
    tmp_h = h
    p = 1
    for _ in range(times):
        p *= C(1, tmp_h) * C(1, tmp_h) / C(2, 2*tmp_h)
        tmp_h -= 1
    return p

def foo1():
    for j in range(1, n+1):
        print(f'N = {N}; n = {j}; p = {p(j, N)}')

foo1()

stats = []
def foo2(it):
    mydict = { x : 0 for x in range(1, n + 2) }
    arr = []
    t = TIMES
    for _ in range(TIMES):
        i = 1
        while i < n+1:
            tmp_p = p(i, N)
            res = np.random.choice(np.array([1, 0]), 1,  p=[tmp_p, 1 - tmp_p]) # 1 - разноцветные, 0 - не разноцветные
            if res[0] == 1:
                i += 1
            else:
                mydict[i] += 1
                break
        else:
            mydict[list(mydict)[-1]] += 1
    
    for value in mydict.values():
        arr.append(1 - value / t)
        t -= value
    else:
        arr.pop()
    stats.append(arr)
    print(it, mydict, arr,  f'Статистически: {mydict[list(mydict)[-1]] / (mydict[list(mydict)[-1]] + mydict[list(mydict)[-2]])}') 

for t in range(100):
    foo2(t)

plt.plot(stats, 'o')
plt.grid(True)
plt.xlabel('Попытки проверки теоретической вероятности и статистической')
plt.ylabel('Вероятность на разноцветные')
plt.title('Статистическая вероятность разноцветных шаров на каждом n')
plt.legend(['Первая попытка', 'Вторая попытка', 'Третья попытка'], loc='lower left', bbox_to_anchor=(-0.02, -0.27), ncol=3)
plt.subplots_adjust(left=0.1, right=0.93, top=0.87, bottom=0.2)
plt.show()
