from collections import Counter
from itertools import pairwise

with open("./input14e.txt") as file:
    input_template, input_rules = file.read().split("\n\n")
    template = input_template.strip()

    start_rules = {}
    for line in input_rules.strip().split("\n"):
        pair, to = line.split(" -> ")
        start_rules[pair] = to


def expand_three(template, rules):
    threes = []
    for i in range(0, len(template) - 1, 3):
        threes.append(template[i + 1:i + 4])

    new_template = template[0] + rules[template[:2]]
    next_start = ""

    for index, three in enumerate(threes):
        if three not in rules:
            result = three[0]

            for pair in pairwise(three):
                result += rules["".join(pair)] + pair[1]

            rules[three] = result

        next_start += three[0]

        if index > 0:
            new_template += rules[next_start]
        new_template += rules[three]
        next_start = three[-1]

        # threes[index - 1][-1] + three[0]


    # new_template = template[0] + rules[template[:2]]
    # new_template += rules[threes[0]]
    #
    # for three_pair in pairwise(threes):
    #     end_first = three_pair[0][-1]
    #     start_second = three_pair[1][0]
    #     new_template += rules[end_first + start_second]
    #     new_template += rules[three_pair[1]]

    return new_template, rules


# def expand(template, rules):
#     new_template = template[0]
#     for pair in zip(template, template[1:]):
#         print(pair, rules["".join(pair)] + pair[1])
#         new_template += rules["".join(pair)] + pair[1]
#
#     return new_template


def apply_steps(template, rules, steps):
    for step in range(steps):
        template, rules = expand_three(template, rules)
        print(step, len(rules))

    return template


def get_score(template):
    counts = Counter(template)
    commons = counts.most_common()
    max_num = commons[0][1]
    min_num = commons[-1][1]

    return max_num - min_num


if __name__ == "__main__":
    processed_template = apply_steps(template, start_rules, 10)
    score = get_score(processed_template)
    print(f"Part 1\nThe result is {score}")

    processed_template = apply_steps(template, start_rules, 40)
    score = get_score(processed_template)
    print(f"Part 2\nThe result is {score}")

    # print(apply_steps(template, rules, 2))
