import itertools
test = [[-1, -2], [30, 40], [25, 35]]
print(list(itertools.chain.from_iterable(test)))
 
#-> [-1, -2, 30, 40, 25, 35]
