f = open("input.txt", "r")
lines = f.readlines()

input = [x for x in lines]

total = 0
game_number = 1
for reading in input:
    val = reading.strip()
    right_side = val.split(":")[1]
    sets = right_side.split(";")

    red = 0
    blue = 0
    green = 0
    for roll in sets:
        cubes = roll.split(",")
        for cube in cubes:
            vals = cube.strip().split(" ")
            num = int(vals[0])
            color = vals[1]
            if color == "red" and num > red:
                red = num
            if color == "blue" and num > blue:
                blue = num
            if color == "green" and num > green:
                green = num

    product = red * blue * green
    total += product

print(total)
