"""
Created on Dec 1, 2020
@author: Franklin Ventura

--- Day 1:  Report Repair ---
Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456
In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?

--- Part Two ---
The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation.
They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?

"""
from pathlib import Path
from itertools import combinations
from math import prod


def run(instructions):
    instructions = map(int, instructions)
    combinations_list = list(combinations(instructions, 2))
    sums = [sum(comb) for comb in combinations_list]
    ind = sums.index(2020)
    values = combinations_list[ind]
    return prod(values)


def run2(instructions):
    instructions = map(int, instructions)
    combinations_list = list(combinations(instructions, 3))
    sums = [sum(comb) for comb in combinations_list]
    ind = sums.index(2020)
    values = combinations_list[ind]
    return prod(values)


if __name__ == "__main__":
    with open(Path(__file__).parent / "input.txt", "r") as this_file:
        instructions = []
        for instruction_line in this_file:
            instruction_line = instruction_line.replace("\n", "")
            instructions.append(instruction_line)
        # out = run(instructions)
        out = run2(instructions)
    print(out)
