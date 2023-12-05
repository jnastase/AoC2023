import re

f = open("input.txt", "r")
lines = f.readlines()

input = [x for x in lines]


card_values = {}

total = 0
card = 1
for reading in input:
    val = reading.strip()

    right_side = val.split(":")[1]
    numbers = right_side.split(" | ")
    wininng_numbers = set([int(x) for x in numbers[0].strip().split(" ") if x])
    my_nums = set([int(x) for x in numbers[1].strip().split(" ") if x])

    plays = card_values.get(card, 1)
    for play in range(plays):
        combined = wininng_numbers.intersection(my_nums)
        total += 1
        if combined:
            additional_cards = input[card : card + len(combined)]
            for value in range(len(additional_cards)):
                next_card = card_values.get(card + (value + 1), 1)
                next_card += 1
                card_values[card + (value + 1)] = next_card

    card += 1

print(total)
