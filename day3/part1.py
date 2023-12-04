import re

f = open("input.txt", "r")
lines = f.readlines()

input = [x for x in lines]

row = 0
parts = []
for reading in input:
    val = reading.strip()
    curr_num_string = ""
    start_index = None
    for i in range(len(val)):
        if val[i].isnumeric():
            curr_num_string += val[i]
            if not start_index:
                start_index = i

        if not val[i].isnumeric() or (val[i].isnumeric() and i == len(val) - 1):
            found_symbol = False
            if start_index:
                min_x = max(0, start_index - 1)
                max_x = min(len(val) - 1, i + 1)
                if row > 0:
                    print(input[row - 1][min_x : i + 1])
                    symbols = [
                        x
                        for x in input[row - 1][min_x:max_x]
                        if not x.isnumeric() and x != "."
                    ]
                    if symbols:
                        found_symbol = True

                if row < len(input) - 1:
                    symbols = [
                        x
                        for x in input[row + 1][min_x:max_x]
                        if not x.isnumeric() and x != "."
                    ]
                    if symbols:
                        found_symbol = True

                if (start_index > 1 and val[start_index - 1] != ".") or (
                    i != len(val) - 1 and val[i] != "."
                ):
                    found_symbol = True

                if found_symbol and curr_num_string:
                    parts.append(int(curr_num_string))

            start_index = None
            curr_num_string = ""

    row += 1

print(sum(parts))

# 514920 low
# 517917 high
