from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement

output = permutations([1, 2, 3])
print list(output)

output = combinations([1, 2, 3], 2)
print list(output)

output = combinations_with_replacement([1, 2, 3], 2)
print list(output)