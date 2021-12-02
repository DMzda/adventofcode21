with open("./input2.txt") as file:
    commands = []
    for line in file:
        command = line.split()
        commands.append((command[0], int(command[1])))


def part_1(commands):
    h_position = 0
    depth = 0

    for command in commands:
        match command:
            case "forward", by:
                h_position += by
            case "down", by:
                depth += by
            case "up", by:
                depth -= by

    return h_position, depth


def part_2(commands):
    aim = 0
    h_position = 0
    depth = 0

    for command in commands:
        match command:
            case "forward", by:
                h_position += by
                depth += aim * by
            case "down", by:
                aim += by
            case "up", by:
                aim -= by

    return h_position, depth


if __name__ == "__main__":
    h_position, depth = part_1(commands)
    print(
        f"Part 1\nHorizontal position: {h_position}, Depth: {depth}\nAnswer: {h_position * depth}"
    )

    h_position, depth = part_2(commands)
    print(
        f"Part 2\nHorizontal position: {h_position}, Depth: {depth}\nAnswer: {h_position * depth}"
    )
