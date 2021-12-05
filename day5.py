from collections import namedtuple

Segment = namedtuple("Segment", ["start", "end"])
Coordinate = namedtuple("Coordinate", ["x", "y"])

with open("./input5.txt") as file:
    segments = []
    for line in file:
        pair = line.strip().split(" -> ")
        start = Coordinate(int(pair[0].split(",")[0]), int(pair[0].split(",")[1]))
        end = Coordinate(int(pair[1].split(",")[0]), int(pair[1].split(",")[1]))
        segments.append(Segment(start, end))


def find_overlaps(segments, skip_diagonals=False):
    overlaps = {}
    for segment in segments:
        start = segment.start
        end = segment.end

        if not skip_diagonals and start.x != end.x and start.y != end.y:
            x_direction = 1 if start.x < end.x else -1
            y_direction = 1 if start.y < end.y else -1

            for gap in range(0, abs(end.x - start.x) + 1):
                coord = Coordinate(
                    start.x + (gap * x_direction), start.y + (gap * y_direction)
                )
                overlaps[coord] = overlaps.get(coord, 0) + 1

        elif start.x == end.x:
            step = 1 if start.y < end.y else -1
            for y in range(start.y, end.y + step, step):
                coord = Coordinate(start.x, y)
                overlaps[coord] = overlaps.get(coord, 0) + 1

        elif start.y == end.y:
            step = 1 if start.x < end.x else -1
            for x in range(start.x, end.x + step, step):
                coord = Coordinate(x, start.y)
                overlaps[coord] = overlaps.get(coord, 0) + 1

    return overlaps


def at_least_two(overlaps):
    result = 0
    for value in overlaps.values():
        if value >= 2:
            result += 1

    return result


if __name__ == "__main__":
    overlaps_no_diagonals = find_overlaps(segments, True)
    part_1 = at_least_two(overlaps_no_diagonals)
    print(f"Part 1\nAt least 2 overlaps: {part_1}")

    overlaps = find_overlaps(segments)
    part_2 = at_least_two(overlaps)
    print(f"Part 2\nAt least 2 overlaps: {part_2}")
