from statistics import median

with open("./input10.txt") as file:
    chunks = [line.strip() for line in file]

OPEN_BRACKETS = {"(": ")", "[": "]", "{": "}", "<": ">"}
CORRUPTED_SCORE = {")": 3, "]": 57, "}": 1197, ">": 25137}
AUTOCOMPLETE_SCORE = {")": 1, "]": 2, "}": 3, ">": 4}


def find_corrupted_chunks(chunks):
    corrupted = []
    rest = []
    for chunk in chunks:
        corrupt = False
        stack = []
        for bracket in chunk:
            if bracket in OPEN_BRACKETS:
                stack.append(bracket)
            else:
                opening_bracket = stack.pop()
                if OPEN_BRACKETS[opening_bracket] != bracket:
                    corrupt = True
                    corrupted.append(bracket)
                    break

        if not corrupt:
            rest.append(chunk)

    return corrupted, rest


def get_corrupted_score(corrupted):
    return sum(CORRUPTED_SCORE[corrupt] for corrupt in corrupted)


def complete_chunks(chunks):
    complete = []
    for chunk in chunks:
        stack = []
        for bracket in chunk:
            if bracket in OPEN_BRACKETS:
                stack.append(bracket)
            else:
                stack.pop()

        to_complete = []
        for bracket in reversed(stack):
            to_complete.append(OPEN_BRACKETS[bracket])
        complete.append(to_complete)

    return complete


def get_autocomplete_score(complete):
    scores = []
    for item in complete:
        total = 0
        for bracket in item:
            total *= 5
            total += AUTOCOMPLETE_SCORE[bracket]
        scores.append(total)

    return median(scores)


if __name__ == "__main__":
    corrupted, rest = find_corrupted_chunks(chunks)
    part_1_score = get_corrupted_score(corrupted)
    print(f"Part 1\nCorrupted score: {part_1_score}")

    complete = complete_chunks(rest)
    part_2_score = get_autocomplete_score(complete)
    print(f"Part 2\nAutocomplete score: {part_2_score}")
