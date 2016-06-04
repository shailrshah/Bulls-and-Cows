# Generate 4-digit random numbers, such that all 4 digits are unique
from itertools import permutations

result2 = [
    a * 10 + b * 1
    for a, b in permutations(range(10), 2)
    if a != 0
]
fh = open("random_numbers2.txt", "w")
for i in result2:
    print(i, file=fh)

result3 = [
    a * 100 + b * 10 + c * 1
    for a, b, c in permutations(range(10), 3)
    if a != 0
]
fh = open("random_numbers3.txt", "w")
for i in result3:
    print(i, file=fh)

result4 = [
    a * 1000 + b * 100 + c * 10 + d * 1
    for a, b, c, d in permutations(range(10), 4)
    if a != 0
]

fh = open("random_numbers4.txt", "w")
for i in result4:
    print(i, file=fh)

result5 = [
    a * 10000 + b * 1000 + c * 100 + d * 10 + e * 1
    for a, b, c, d, e in permutations(range(10), 5)
    if a != 0
]

fh = open("random_numbers5.txt", "w")
for i in result5:
    print(i, file=fh)

result6 = [
    a * 100000 + b * 10000 + c * 1000 + d * 100 + e * 10 + f * 1
    for a, b, c, d, e, f in permutations(range(10), 6)
    if a != 0
]

fh = open("random_numbers6.txt", "w")
for i in result6:
    print(i, file=fh)


result7 = [
    a * 1000000 + b * 100000 + c * 10000 + d * 1000 + e * 100 + f * 10 + g * 1
    for a, b, c, d, e, f, g in permutations(range(10), 7)
    if a != 0
]

fh = open("random_numbers7.txt", "w")
for i in result7:
    print(i, file=fh)

result8 = [
    a * 10000000 + b * 1000000 + c * 100000 + d * 10000 + e * 1000 + f * 100 + g * 10 + h * 1
    for a, b, c, d, e, f, g, h in permutations(range(10), 8)
    if a != 0
]

fh = open("random_numbers8.txt", "w")
for i in result8:
    print(i, file=fh)

result9 = [
    a * 100000000 + b * 10000000 + c * 1000000 + d * 100000 + e * 10000 + f * 1000 + g * 100 + h * 10 + i * 1
    for a, b, c, d, e, f, g, h, i in permutations(range(10), 9)
    if a != 0
]

fh = open("random_numbers9.txt", "w")
for i in result9:
    print(i, file=fh)


result10 = [
    a * 1000000000 + b * 100000000 + c * 10000000 + d * 1000000 + e * 100000 + f * 10000 + g * 1000 + h * 100 + i * 10 + j
    for a, b, c, d, e, f, g, h, i, j in permutations(range(10), 10)
    if a != 0
]

fh = open("random_numbers10.txt", "w")
for i in result10:
    print(i, file=fh)




