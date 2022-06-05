from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
Fold = namedtuple("Fold", ["axis", "line"])

with open("./input13.txt") as file:
    input_dots, input_folds = file.read().split("\n\n")
    dots = set()
    for line in input_dots.strip().split():
        x, y = line.strip().split(",")
        dots.add(Point(int(x), int(y)))

    folds = []
    for line in input_folds.strip().split("\n"):
        axis, line = line.removeprefix("fold along ").split("=")
        folds.append(Fold(axis, int(line)))


def fold_once(dots, fold):
    folded_dots = set()
    for dot in dots:
        if fold.axis == "y":
            if dot.y > fold.line:
                folded_y = fold.line - (dot.y - fold.line)
                folded_dots.add(Point(dot.x, folded_y))
            else:
                folded_dots.add(dot)
        else:
            if dot.x > fold.line:
                folded_x = fold.line - (dot.x - fold.line)
                folded_dots.add(Point(folded_x, dot.y))
            else:
                folded_dots.add(dot)
    return folded_dots


def fold(dots, folds):
    for fold in folds:
        dots = fold_once(dots, fold)

    return dots


def print_dots(dots):
    max_x = max(dot.x for dot in dots)
    max_y = max(dot.y for dot in dots)

    to_print = ""
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if Point(x, y) in dots:
                to_print += "#"
            else:
                to_print += "."
        to_print += "\n"

    print(to_print)


if __name__ == "__main__":
    folded_once = fold_once(dots, folds[0])
    print(f"Part 1\nAfter one fold, there are {len(folded_once)} dots visible.")

    folded = fold(dots, folds)
    print(f"Part 2\nThe code is:")
    print_dots(folded)