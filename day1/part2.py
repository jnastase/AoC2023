import re

name_to_val_dic = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def name_to_num(val):
    if val.isnumeric():
        return val

    return name_to_val_dic[val.lower()]


f = open("input.txt", "r")
lines = f.readlines()

input = [x for x in lines]

total = 0
for reading in input:
    val = reading.strip()
    matches = re.findall("(\d)|(one|two|three|four|five|six|seven|eight|nine)", val)
    first_digit, first_word = matches[0]

    last_digit = None
    last_word = None
    val_reversed = ""
    # build string in reverse because a sequence of "twone" going forward will only get "two" and not "one"
    # not an issue for the first but one for the end of the string
    for i in range(len(val)):
        val_reversed = val[-(i + 1)] + val_reversed
        matches = re.findall(
            "(\d)|(one|two|three|four|five|six|seven|eight|nine)", val_reversed
        )
        if matches:
            last_digit, last_word = matches[0]
            break

    first = first_digit if first_digit else first_word
    last = last_digit if last_digit else last_word

    # print(matches)
    print(f"{val}: {first}, {last}")

    total += int(f"{name_to_num(first)}{name_to_num(last)}")

print(total)
