f = open("input.txt", "r")
lines = f.readlines()

input = [x for x in lines]

total = 0
for reading in input:
    val = reading.strip()
    digits = [x for x in val if x.isnumeric()]
    first = digits[0]
    last = digits[-1]

    total += int(f"{first}{last}")

print(total)
