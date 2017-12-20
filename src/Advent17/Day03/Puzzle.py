'''
Created on Dec 20, 2017

@author: venturf2

--- Day 3: Spiral Memory ---
You come across an experimental new kind of memory stored on an infinite
two-dimensional grid.

Each square on the grid is allocated in a spiral pattern starting at a
location marked 1 and then counting up while spiraling outward.
For example, the first few squares are allocated like this:

17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23---> ...
While this is very space-efficient (no squares are skipped),
requested data must be carried back to square 1
(the location of the only access port for this memory system)
by programs that can only move up, down, left, or right.
They always take the shortest path:
the Manhattan Distance between the location of the data and square 1.

For example:

Data from square 1 is carried 0 steps, since it's at the access port.
Data from square 12 is carried 3 steps, such as: down, left, left.
Data from square 23 is carried only 2 steps: up twice.
Data from square 1024 must be carried 31 steps.
How many steps are required to carry the data from the 
quare identified in your puzzle input all the way to the access port?

Your puzzle input is 265149.
'''


def test_p10():
    testing = 1
    actual_out = run(testing)
    expected_out = 0
    assert actual_out == expected_out, "{} != {}".format(actual_out,
                                                         expected_out)


def test_p11():
    testing = 12
    actual_out = run(testing)
    expected_out = 3
    assert actual_out == expected_out, "{} != {}".format(actual_out,
                                                         expected_out)


def test_p12():
    testing = 23
    actual_out = run(testing)
    expected_out = 2
    assert actual_out == expected_out, "{} != {}".format(actual_out,
                                                         expected_out)


def test_p13():
    testing = 1024
    actual_out = run(testing)
    expected_out = 31
    assert actual_out == expected_out, "{} != {}".format(actual_out,
                                                         expected_out)


def run(test):
    out = test
    return out


# def test_p20():
#     testing = 0
#     actual_out = run2(testing)
#     expected_out = 9
#     assert actual_out == expected_out, "{} != {}".format(actual_out,
#                                                          expected_out)
# 
# 
# 
# def run2(test):
#     out = test
#     return out


if __name__ == "__main__":
    out = run(265149)
    print(out)
