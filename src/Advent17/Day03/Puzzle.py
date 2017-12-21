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

--- Part Two ---
As a stress test on the system,
the programs here clear the grid and then store the value 1 in square 1.
Then, in the same allocation order as shown above,
they store the sum of the values in all adjacent squares, including diagonals.

So, the first few squares' values are chosen as follows:

Square 1 starts with the value 1.
Square 2 has only one adjacent filled square (with value 1),
so it also stores 1.
Square 3 has both of the above squares as neighbors
and stores the sum of their values, 2.
Square 4 has all three of the aforementioned squares as
neighbors and stores the sum of their values, 4.
Square 5 only has the first and fourth squares as neighbors,
so it gets the value 5.
Once a square is written, its value does not change.
Therefore, the first few squares would receive the following values:

147  142  133  122   59
304    5    4    2   57
330   10    1    1   54
351   11   23   25   26
362  747  806--->   ...
What is the first value written that is larger than your puzzle input?
'''
import math
import numpy as np


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


def manhattan_distance(x, y):
    return sum(abs(a-b) for a, b in zip(x, y))


def closest_perfect_sqr(n):
    odd = False
    while not odd:
        if n % n**0.5 == 0:
            power = math.pow((math.sqrt(n)), 2)
            odd = power % 2 == 1
        n += 1
    return power


N, SOUTH, W, E = (0, -1), (0, 1), (-1, 0), (1, 0) # directions
# turn_right = {NORTH: E, E: S, S: W, W: NORTH} # old -> new direction
turn_left = {SOUTH: E, E: N, N: W, W: SOUTH} # old -> new direction


def spiral(width, height):
    if width < 1 or height < 1:
        raise ValueError
    x, y = width // 2, height // 2 # start near the center
    dx, dy = SOUTH # initial direction
    matrix = [[None] * width for _ in range(height)]
    count = 0
    while True:
        count += 1
        matrix[y][x] = count # visit
        # try to turn right
        new_dx, new_dy = turn_left[dx,dy]
        new_x, new_y = x + new_dx, y + new_dy
        if (0 <= new_x < width and 0 <= new_y < height and
            matrix[new_y][new_x] is None): # can turn right
            x, y = new_x, new_y
            dx, dy = new_dx, new_dy
        else: # try to move straight
            x, y = x + dx, y + dy
            if not (0 <= x < width and 0 <= y < height):
                return matrix # nowhere to go


def run(test):
    power = closest_perfect_sqr(test)
    side = int(math.sqrt(power))
    a = spiral(side, side)
    a = np.array(a)
    loc = np.where(a==test)
    loc = (loc[0][0], loc[1][0])
    print(loc)
    loc2 = np.where(a==1)
    loc2 = (loc2[0][0], loc2[1][0])
    out = manhattan_distance(loc, loc2)
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
