import itertools
test = [[-1, -2], [30, 40], [25, 35]]
print(list(itertools.chain.from_iterable(test)))
#-> [-1, -2, 30, 40, 25, 35]


# pip install more_itertools
import more_itertools
test = [[-1, -2], [1, 2, 3, [4, (5, [6, 7])]], (30, 40), [25, 35]]
print(list(more_itertools.collapse(test)))
#Output=> [-1, -2, 1, 2, 3, 4, 5, 6, 7, 30, 40, 25, 35]
