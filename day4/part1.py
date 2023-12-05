import re

f = open("input.txt", "r")
lines = f.readlines()

input = [x for x in lines]

total = 0
for reading in input:
    val = reading.strip()
    right_side = val.split(":")[1]
    numbers = right_side.split(" | ")
    wininng_numbers = set([int(x) for x in numbers[0].strip().split(" ") if x])
    my_nums = set([int(x) for x in numbers[1].strip().split(" ") if x])

    combined = wininng_numbers.intersection(my_nums)
    if combined:
        total += 2 ** (len(combined) - 1)


print(total)
