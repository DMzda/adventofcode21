from math import ceil, floor
import statistics

with open("./input7.txt") as file:
    positions = [int(number) for number in file.readline().split(",")]


def count_moves(positions, target):
    moves = 0
    for position in positions:
        moves += abs(target - position)

    return moves


def triangle(number):
    return sum(range(number + 1))


def count_moves_triangle(positions, target):
    moves = 0
    for position in positions:
        moves += triangle(abs(target - position))

    return moves


def find_least_moves(positions, around):
    left, *_, right = range(around - 10, around + 11)

    min_moves = 1_000_000_000_000_000
    min_position = 0
    for target in range(left, right):
        if (current := count_moves_triangle(positions, target)) < min_moves:
            min_moves = current
            min_position = target

    return min_position, min_moves


if __name__ == "__main__":
    median = int(statistics.median(positions))
    print(f"Part 1\nPosition: {median}, Fuel used: {count_moves(positions, median)}")

    mean = round(statistics.mean(positions))
    position, fuel_used = find_least_moves(positions, mean)
    print(f"Part 2\nPosition: {position}, Fuel used: {fuel_used}")
