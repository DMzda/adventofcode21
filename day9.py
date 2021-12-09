from collections import namedtuple
from math import prod

Point = namedtuple("Point", ["x", "y", "value"])

with open("./input9.txt") as file:
    grid = []
    for y, line in enumerate(file):
        x_line = []
        for x, number in enumerate(line.strip()):
            x_line.append(Point(x, y, int(number)))
        grid.append(x_line)


def find_low_points(grid):
    low_points = []
    for line in grid:
        for point in line:
            if all(
                point.value < adjacent.value for adjacent in get_adjacent(grid, point)
            ):
                low_points.append(point)

    return low_points


def get_adjacent(grid, point):
    y_length = len(grid)
    x_length = len(grid[0])

    adjacent = []

    if (y_up := point.y - 1) >= 0:
        adjacent.append(grid[y_up][point.x])

    if (y_down := point.y + 1) < y_length:
        adjacent.append(grid[y_down][point.x])

    if (x_left := point.x - 1) >= 0:
        adjacent.append(grid[point.y][x_left])

    if (x_right := point.x + 1) < x_length:
        adjacent.append(grid[point.y][x_right])

    return adjacent


def get_risk_sum(low_points):
    return sum(point.value + 1 for point in low_points)


def find_basins(grid):
    basins = {point: {point} for point in find_low_points(grid)}
    checked = set()
    total_points = len(grid) * len(grid[0])

    while len(checked) < total_points:
        for line in grid:
            for point in line:
                if point in checked:
                    continue

                if point.value == 9:
                    checked.add(point)
                    continue

                adjacent = get_adjacent(grid, point)
                for low, basin in basins.items():
                    if any(adj in basin for adj in adjacent):
                        basins[low].add(point)
                        checked.add(point)

    return basins


def get_three_largest_basins(basins):
    sizes = [len(basin) for basin in basins.values()]
    sizes.sort(reverse=True)
    return sizes[:3]


if __name__ == "__main__":
    low_points = find_low_points(grid)
    risk = get_risk_sum(low_points)
    print(f"Part 1\nThe sum of the risk levels is: {risk}")

    basins = find_basins(grid)
    part_2 = prod(get_three_largest_basins(basins))
    print(f"Part 2\nThe product of the sizes of the three largest basins is: {part_2}")
