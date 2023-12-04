import re

f = open("input.txt", "r")
lines = f.readlines()

input = [x for x in lines]

row = 0
parts = []
gear_indices = dict()
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
                    search_str = input[row - 1][min_x:max_x]
                    gear_index = search_str.index("*") if "*" in search_str else None
                    if gear_index is not None:
                        dic_val = gear_indices.get((row - 1, min_x + gear_index), [])
                        dic_val.append(int(curr_num_string))
                        gear_indices[(row - 1, min_x + gear_index)] = dic_val

                if row < len(input) - 1:
                    search_str = input[row + 1][min_x:max_x]
                    gear_index = search_str.index("*") if "*" in search_str else None
                    if gear_index is not None:
                        dic_val = gear_indices.get((row + 1, min_x + gear_index), [])
                        dic_val.append(int(curr_num_string))
                        gear_indices[(row + 1, min_x + gear_index)] = dic_val

                if start_index > 1 and val[start_index - 1] == "*":
                    dic_val = gear_indices.get((row, start_index - 1), [])
                    dic_val.append(int(curr_num_string))
                    gear_indices[(row, start_index - 1)] = dic_val

                if i != len(val) - 1 and val[i] == "*":
                    dic_val = gear_indices.get((row, i), [])
                    dic_val.append(int(curr_num_string))
                    gear_indices[(row, i)] = dic_val

                # if found_symbol and curr_num_string:
                #     parts.append(int(curr_num_string))

            start_index = None
            curr_num_string = ""

    row += 1

total = 0
for k, v in gear_indices.items():
    if len(v) == 2:
        total += v[0] * v[1]

print(total)
# print(sum([val * P for key, val in gear_indices.items() if len(val) == 2]))

# 514920 low
# 517917 high
