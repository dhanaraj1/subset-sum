'''
http://stackoverflow.com/questions/3420937/algorithm-to-find-which-number-in-a-list-sum-up-to-a-certain-number

'''
import itertools

from itertools import chain, combinations
import sys
from timeit import default_timer as timer


def memoization(x_list, target):
    memo = dict()
    result, _ = g(x_list, x_list, target, memo)
    return (sum(result), result)


def g(v, w, S, memo):
    subset = []
    id_subset = []
    for i, (x, y) in enumerate(zip(v, w)):
        # Check if there is still a solution if we include v[i]
        if f(v, i + 1, S - x, memo) > 0:
            subset.append(x)
            id_subset.append(y)
            S -= x
    return subset, id_subset


def f(v, i, S, memo):
    if i >= len(v):
        return 1 if S == 0 else 0
    if (i, S) not in memo:    # <-- Check if value has not been calculated.
        count = f(v, i + 1, S, memo)
        count += f(v, i + 1, S - v[i], memo)
        memo[(i, S)] = count  # <-- Memoize calculated result.
    return memo[(i, S)]       # <-- Return memoized value.


data = []
with open("data/numbers/numbers-50.txt") as file:
    for line in file:
        line = line.strip()
        data.append(int(line))

target = 10000000

print "numero de elementos = |S| = ", len(data)
print "target = ", target

start = timer()
bf = memoization(data, target)
end = timer()


print "Tiempo de Ejecucion: ", (end - start)