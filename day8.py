import itertools
from collections import namedtuple
from copy import deepcopy
from string import ascii_lowercase

Entry = namedtuple("Entry", ["signals", "output"])
UNIQUES = {2: 1, 3: 7, 4: 4, 7: 8}  # 1, 7, 4, 8
SEGMENTS = {
    0: set("abcefg"),
    1: set("cf"),
    2: set("acdeg"),
    3: set("acdfg"),
    4: set("bcdf"),
    5: set("abdfg"),
    6: set("abdefg"),
    7: set("acf"),
    8: set("abcdefg"),
    9: set("abcdfg"),
}

#  a
# b c
#  d
# e f
#  g

with open("./input8.txt") as file:
    entries = []
    for line in file:
        split_line = line.strip().split(" | ")
        split_line[0] = split_line[0].split()
        split_line[1] = split_line[1].split()

        entries.append(Entry(split_line[0], split_line[1]))


def count_1478(entries):
    count = 0
    for entry in entries:
        for value in entry.output:
            if len(value) in UNIQUES:
                count += 1

    return count


def solve(entry):
    solved = {letter: set(ascii_lowercase[:7]) for letter in ascii_lowercase[:7]}

    for segment in entry.signals:
        if (length := len(segment)) in UNIQUES:
            possible = SEGMENTS[UNIQUES[length]]
            for letter in segment:
                solved[letter].intersection_update(possible)

    current_solve = deepcopy(solved)

    while True:
        for letter, current in solved.items():
            for other_letter, compare in solved.items():
                if letter == other_letter:
                    continue

                if len(res := current - compare) == 1:
                    current_solve[letter] = res

                if current == compare:
                    for c_letter, c_current in solved.items():
                        if letter == c_letter:
                            continue

                        diff = c_current - current
                        if diff:
                            current_solve[c_letter].intersection_update(diff)

                if len(current) == 1:
                    for c_letter, c_current in solved.items():
                        if letter == c_letter:
                            continue

                        current_solve[c_letter] = c_current - current

        if solved == current_solve:
            break

        if all(len(value) == 1 for value in current_solve.values()):
            break
        else:
            solved = deepcopy(current_solve)

    product = list(itertools.product(*current_solve.values()))
    can_work = []
    for test in product:
        # remove duplicates
        if len(test) == len(set(test)):
            can_work.append(test)

    for test in can_work:
        mapping = {}
        for index, segment in enumerate(test):
            mapping[ascii_lowercase[index]] = segment

        if result := test_solution(mapping, entry.output):
            return mapping, result


def test_solution(test, output):
    result = []
    for item in output:
        segments = set()
        for letter in item:
            segments.add(test[letter])

        for number, number_segments in SEGMENTS.items():
            if segments == number_segments:
                result.append(number)

    if len(result) == 4:
        return int("".join(str(number) for number in result))


if __name__ == "__main__":
    count = count_1478(entries)
    print(f"Part 1\nNumber of 1s, 4s, 7s and 8s in output: {count}")
    # acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf
    # correct = {"d": "a", "e": "b", "a": "c", "f": "d", "g": "e", "b": "f", "c": "g"}
    # print(test_solution(correct, entries[0].output))

    total = 0
    for entry in entries:
        _, result = solve(entry)
        total += result
    print(f"Part 2\nOutput values total: {total}")
