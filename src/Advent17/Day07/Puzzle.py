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
'''


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
    out = rows
    return out


# def test_p20():
#     testing = '''5\t9\t2\t8\n9\t4\t7\t3\n3\t8\t6\t5'''
#     actual_out = run2(testing)
#     expected_out = 9
#     assert actual_out == expected_out, "{} != {}".format(actual_out,
#                                                          expected_out)


def run2(test):
    rows = test.split('\n')
    out = rows
    return out


if __name__ == "__main__":
    with open('input.txt', 'r') as this_file:
        text = this_file.read()
        out = run2(text[:-1])  # Because the final new line causes problems
    print(out)
