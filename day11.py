from dataclasses import dataclass


@dataclass(eq=False)
class Point:
    x: int
    y: int
    value: int | None = None
    flashed: bool = False

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point):
            return False

        return self.x == other.x and self.y == other.y

    def __str__(self) -> str:
        return f"({self.x}, {self.y}) = {self.value}"


def read_grid():
    with open("./input11.txt") as file:
        grid = []
        for y, line in enumerate(file):
            x_line = []
            for x, number in enumerate(line.strip()):
                x_line.append(Point(x, y, int(number)))
            grid.append(x_line)
    return grid


def get_adjacent(grid, point):
    y_length = len(grid)
    x_length = len(grid[0])

    adjacent = []

    for y in range(max(0, point.y - 1), min(y_length, point.y + 2)):
        for x in range(max(0, point.x - 1), min(x_length, point.x + 2)):
            if point == Point(x, y):
                continue

            adjacent.append(grid[y][x])

    return adjacent


def simulate_steps(grid, steps):
    flashes = 0
    for step in range(steps):
        for line in grid:
            for point in line:
                point.value += 1

        has_tens = True
        flashed = []
        while has_tens:
            has_tens = False
            for line in grid:
                for point in line:
                    if point.value > 9:
                        has_tens = True
                        point.flashed = True
                        flashed.append(point)
                        flashes += 1
                        point.value = 0

                        adjacent = get_adjacent(grid, point)
                        for point in adjacent:
                            if not point.flashed:
                                point.value += 1

        if len(flashed) == len(grid) * len(grid[0]):
            return grid, flashes, step + 1

        for point in flashed:
            point.flashed = False

    return grid, flashes, steps


if __name__ == "__main__":
    sim_grid, flashes, step = simulate_steps(read_grid(), 100)

    for line in sim_grid:
        for point in line:
            print(point.value, end="")
        print()

    print(f"Part 1\nThere are {flashes} flashes after {step} steps.")

    sim_grid, flashes, step = simulate_steps(read_grid(), 1_000_000)
    print(f"Part 2\nAll octopuses flash on step {step}.")
