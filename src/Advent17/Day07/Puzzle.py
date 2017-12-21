'''
Created on Dec 20, 2017

@author: venturf2

--- Day 7: Recursive Circus ---
Wandering further through the circuits of the computer,
you come upon a tower of programs that have gotten themselves
into a bit of trouble. A recursive algorithm has gotten out of hand,
and now they're balanced precariously in a large tower.

One program at the bottom supports the entire tower.
It's holding a large disc,
and on the disc are balanced several more sub-towers.
At the bottom of these sub-towers, standing on the bottom disc,
are other programs, each holding their own disc, and so on.
At the very tops of these sub-sub-sub-...-towers,
many programs stand simply keeping the disc
below them balanced but with no disc of their own.

You offer to help,
but first you need to understand the structure of these towers.
You ask each program to yell out their name, their weight,
and (if they're holding a disc)
the names of the programs immediately above them balancing on that disc.
You write this information down (your puzzle input).
Unfortunately, in their panic, they don't do this in an orderly fashion;
by the time you're done, you're not sure which program gave which information.

For example, if your list is the following:

pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)
...then you would be able to recreate the structure
of the towers that looks like this:

                gyxo
              /
         ugml - ebii
       /      \
      |         jptl
      |
      |         pbga
     /        /
tknk --- padx - havc
     \        \
      |         qoyq
      |
      |         ktlj
       \      /
         fwft - cntj
              \
                xhth
In this example, tknk is at the bottom of the tower (the bottom program),
and is holding up ugml, padx, and fwft. Those programs are,
in turn, holding up other programs; in this example,
none of those programs are holding up any other programs,
and are all the tops of their own towers.
(The actual tower balancing in front of you is much larger.)

Before you're ready to help them,
you need to make sure your information is correct.
What is the name of the bottom program?

--- Part Two ---
The programs explain the situation: they can't get down.
Rather, they could get down,
if they weren't expending all of their energy trying to
keep the tower balanced. Apparently, one program has the wrong weight,
and until it's fixed, they're stuck here.

For any program holding a disc,
each program standing on that disc forms a sub-tower.
Each of those sub-towers are supposed to be the same weight,
or the disc itself isn't balanced.
The weight of a tower is the sum of the weights of the programs in that tower.

In the example above, this means that for ugml's disc to be balanced,
gyxo, ebii, and jptl must all have the same weight, and they do: 61.

However, for tknk to be balanced,
each of the programs standing on its disc and all
programs above it must each match.
This means that the following sums must all be the same:

ugml + (gyxo + ebii + jptl) = 68 + (61 + 61 + 61) = 251
padx + (pbga + havc + qoyq) = 45 + (66 + 66 + 66) = 243
fwft + (ktlj + cntj + xhth) = 72 + (57 + 57 + 57) = 243
As you can see, tknk's disc is unbalanced: ugml's
stack is heavier than the other two.
Even though the nodes above ugml are balanced,
ugml itself is too heavy:
it needs to be 8 units lighter for its stack to weigh
243 and keep the towers balanced.
If this change were made, its weight would be 60.

Given that exactly one program is the wrong weight,
what would its weight need to be to balance the entire tower?
'''
from collections import defaultdict


def test_p10():
    testing = '''pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)'''
    actual_out = run(testing)
    expected_out = 'tknk'
    assert actual_out == expected_out, "{} != {}".format(actual_out,
                                                         expected_out)


def run(test):
    rows = test.split('\n')
    subprogram_names = []
    supporting_programs = []
    for row in rows:
        if '->' in row:
            supporting_program, subprograms = row.split(' -> ')
            supporting_program = supporting_program.split(' (')[0]
            supporting_programs.append(supporting_program)
            subprograms = subprograms.split(', ')
            subprogram_names.extend(subprograms)
#     print(supporting_programs)
#     print(subprogram_names)
    return list(set(supporting_programs) - set(subprogram_names))[0]


def test_p20():
    testing = '''pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)'''
    actual_out = run2(testing)
    expected_out = 60
    assert actual_out == expected_out, "{} != {}".format(actual_out,
                                                         expected_out)


def find_weight(program, supporting_programs, program_weights):
    sub_programs = supporting_programs[program][0]
    total_weight = 0
    weights = []
    for sub_program in sub_programs:
        if sub_program not in supporting_programs:
            weight = program_weights[sub_program]
        else:
            weight = find_weight(sub_program, supporting_programs,
                                 program_weights)
        weights.append(weight)
        total_weight += weight
    print(weights)
    if not (len(set(weights)) <= 1):
        print(program, supporting_programs[program])
        print([(program_weights[prog], supporting_programs[prog][1]) for prog in supporting_programs[program][0]])
        raise SystemError
    total_weight += program_weights[program]
    supporting_programs[program].append(total_weight)
    return total_weight


def run2(test):
    rows = test.split('\n')
    supporting_programs = defaultdict(list)
    program_weights = {}
    for row in rows:
        if '->' in row:
            supporting_program, subprograms = row.split(' -> ')
            support, support_weight = supporting_program.split(' (')
            support_weight = int(support_weight[:-1])
            program_weights[support] = support_weight
            subprograms = subprograms.split(', ')
            supporting_programs[support].append(subprograms)
        else:
            program, weight = row.split(' (')
            weight = int(weight[:-1])
            program_weights[program] = weight
    weight = find_weight(run(test), supporting_programs, program_weights)
    return weight


if __name__ == "__main__":
    with open('input.txt', 'r') as this_file:
        text = this_file.read()
        out = run2(text[:-1])  # Because the final new line causes problems
    print(out)
