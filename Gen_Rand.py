# Generate 4-digit random numbers, such that all 4 digits are unique
from itertools import permutations

result = [
    a * 1000 + b * 100 + c * 10 + d * 1
    for a, b, c, d in permutations(range(10), 4)
    if a != 0
]

fh = open("random_numbers.txt", "w")
for i in result:
    print(i, file=fh)
