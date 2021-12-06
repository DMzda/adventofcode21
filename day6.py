with open("./input6.txt") as file:
    start = [int(number) for number in file.readline().split(",")]


def simulate(start, days):
    state = {i: 0 for i in range(9)}

    for fish in start:
        state[fish] += 1

    for day in range(days):
        new_state = {i: 0 for i in range(9)}

        for fish, number in state.items():
            if fish == 0:
                new_state[8] = number
                new_state[6] += number
                continue

            new_state[fish - 1] += number

        state = new_state

    return state


def total_fish(state):
    return sum(state.values())


if __name__ == "__main__":
    state = simulate(start, 80)
    total = total_fish(state)
    print(f"Part 1\nState: {state}\nTotal fish: {total}")

    state = simulate(start, 256)
    total = total_fish(state)
    print(f"Part 2\nState: {state}\nTotal fish: {total}")
