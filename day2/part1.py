f = open("input.txt", "r")
lines = f.readlines()

input = [x for x in lines]

total = 0
game_number = 1
for reading in input:
    val = reading.strip()
    right_side = val.split(":")[1]
    sets = right_side.split(";")

    valid = True
    for roll in sets:
        if not valid:
            break
        cubes = roll.split(",")
        for cube in cubes:
            vals = cube.strip().split(" ")
            num = int(vals[0])
            color = vals[1]
            if color == "red" and num > 12:
                valid = False
            if color == "blue" and num > 14:
                valid = False
            if color == "green" and num > 13:
                valid = False

    if valid:
        total += game_number
    game_number += 1

print(total)
