with open("./input1.txt") as file:
    report = [int(line) for line in file]

increases = 0
previous_number = report[0]
for number in report:
    if number > previous_number:
        increases += 1

    previous_number = number

print(f"Part 1: {increases}")

increases = 0
window = report[:3]
previous_sum = sum(window)
for number in report[3:]:
    window.pop(0)
    window.append(number)

    window_sum = sum(window)
    if window_sum > previous_sum:
        increases += 1

    previous_sum = window_sum

print(f"Part 2: {increases}")
