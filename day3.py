with open("./input3.txt") as file:
    report = [line.strip() for line in file]


def power_consumption(report):
    counts = [0] * len(report[0])

    for number in report:
        for index, bit in enumerate(number):
            if bit == "1":
                counts[index] += 1

    threshold = len(report) / 2
    gamma = ""
    epsilon = ""
    for count in counts:
        if count > threshold:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

    return int(gamma, 2), int(epsilon, 2)


def life_support_rating(report):
    oxygen = gas_rating(report, "1")
    co2 = gas_rating(report, "0")

    return oxygen, co2


def gas_rating(report, to_keep, index=0):
    num_reports = len(report)
    if num_reports == 1:
        return int(report[0], 2)

    count = 0
    for number in report:
        if number[index] == "1":
            count += 1

    if count >= (num_reports / 2):
        keep = to_keep
    else:
        keep = "0" if to_keep == "1" else "1"

    return gas_rating(
        [number for number in report if number[index] == keep], to_keep, index + 1
    )


if __name__ == "__main__":
    gamma, epsilon = power_consumption(report)
    print(
        f"Part 1\nGamma rate: {gamma:b} {gamma}, Epsilon rate: {epsilon:b} {epsilon}\nPower consumption: {gamma * epsilon}"
    )

    oxygen, co2 = life_support_rating(report)
    print(
        f"Part 2\nOxygen rating: {oxygen:b} {oxygen}, CO2 rating: {co2:b} {co2}\nLife support rating: {oxygen * co2}"
    )
