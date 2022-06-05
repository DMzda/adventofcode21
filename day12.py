from collections import defaultdict

with open("./input12.txt") as file:
    graph = defaultdict(list)
    for line in file:
        start, end = line.strip().split("-")

        graph[start].append(end)
        graph[end].append(start)


def find_path(graph, start, small_visits=1):
    incomplete = [[start]]
    complete = []

    while incomplete:
        current_path = incomplete.pop()
        current_cave = current_path[-1]

        for cave in graph[current_cave]:
            if cave == "end":
                found = current_path + [cave]
                complete.append(found)
                continue

            if cave.islower():
                if cave == "start":
                    continue

                visits = current_path.count(cave)
                if visits >= small_visits or will_have_extra_small_cave_visits(current_path, cave):
                    continue

            to_check = current_path + [cave]
            incomplete.append(to_check)

    return complete


def will_have_extra_small_cave_visits(path, small_cave):
    smalls = [cave for cave in path if cave.islower()]
    twos = 0
    counts = defaultdict(int)
    counts[small_cave] += 1
    for cave in smalls:
        counts[cave] += 1

    return sum(count > 1 for count in counts.values()) > 1


if __name__ == "__main__":
    paths = find_path(graph, "start")
    print(f"Part 1\nThere are {len(paths)} paths.")

    paths = find_path(graph, "start", 2)
    print(f"Part 2\nThere are {len(paths)} paths.")
