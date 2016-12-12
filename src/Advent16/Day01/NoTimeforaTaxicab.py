'''
Created on Dec 2, 2016
@author: venturf2

http://adventofcode.com/2016/day/1
--- Day 1: No Time for a Taxicab ---

Santa's sleigh uses a very high-precision clock to guide its movements,
and the clock's oscillator is regulated by stars. Unfortunately,
the stars have been stolen... by the Easter Bunny. To save Christmas,
Santa needs you to retrieve all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each
day in the advent calendar; the second puzzle is unlocked when you complete
the first. Each puzzle grants one star. Good luck!

You're airdropped near Easter Bunny Headquarters in a city somewhere.
"Near", unfortunately, is as close as you can get - the instructions
on the Easter Bunny Recruiting Document the Elves intercepted start here,
and nobody had time to work them out further.

The Document indicates that you should start at the given coordinates
(where you just landed) and face North. Then, follow the provided sequence:
either turn left (L) or right (R) 90 degrees, then walk forward the given
number of blocks, ending at a new intersection.

There's no time to follow such ridiculous instructions on foot, though, so you
take a moment and work out the destination. Given that you can only walk on
the street grid of the city, how far is the shortest path to the destination?

For example:

Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5 blocks away.
R2, R2, R2 leaves you 2 blocks due South of your starting position, which is 2
blocks away.
R5, L5, R5, R3 leaves you 12 blocks away.
How many blocks away is Easter Bunny HQ?

--- Part Two ---

Then, you notice the instructions continue on the back of the Recruiting
Document. Easter Bunny HQ is actually at the first location you visit twice.

For example, if your instructions are R8, R4, R4, R8, the first location
you visit twice is 4 blocks away, due East.

How many blocks away is the first location you visit twice?
'''
from numpy import array
import numpy as np
import matplotlib.pyplot as plt

directions = {
    'N': [0, array([0, 1])],
    'E': [90, array([1, 0])],
    'S': [180, array([0, -1])],
    'W': [270, array([-1, 0])],
    0: 'N',
    90: 'E',
    180: 'S',
    270: 'W',
    360: 'N',
    -90: 'W'
    }
changes = {
    'R': 90,
    'L': -90
    }

x, y = 0, 0

direction = 0


def get_direction(current_dir, change):
    degree = directions[current_dir][0]
    change_degree = changes[change]
    new_degree = change_degree + degree
    direction = directions[new_degree]
    return direction, directions[direction][1]


def test1_1_run():
    instructions = ['R2', 'L3']
    expected_out = 5
    actual_out = run(instructions)
    assert expected_out == actual_out


def test1_2_run():
    instructions = ['R2', 'R2', 'R2']
    expected_out = 2
    actual_out = run(instructions)
    assert expected_out == actual_out


def test1_3_run():
    instructions = ['R5', 'L5', 'R5', 'R3']
    expected_out = 12
    actual_out = run(instructions)
    assert expected_out == actual_out


def test2_1_run2():
    instructions = ['R8', 'R4', 'R4', 'R8']
    actual_out = run(instructions)
    expected_out = [4, 0]
    assert expected_out == actual_out


def ccw(A, B, C):
    return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])


# Return true if line segments AB and CD intersect
def intersect(line1, line2):
    A, B = line1[0], line1[1]
    C, D = line2[0], line2[1]
    if np.array_equal(A, D):
        return False
    return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)


def find_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
        raise Exception('lines do not intersect')

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return [x, y]


def intersect_compare(new_line, lines):
    if len(lines) == 0:
        return False
    for line in lines:
        if intersect(new_line, line):
            return find_intersection(new_line, line)
    return False


def run(instructions):
    current_dir = 'N'
    current_position = array([0, 0])
    lines = []
    line = [current_position, ]
    for instruction in instructions:
        change = instruction[0]
        distance = instruction[1:]
        current_dir, array_change = get_direction(current_dir, change)
        array_change = int(distance) * array_change
        new_position = current_position + array_change
        line = [current_position, new_position]
        plt.plot((current_position[0], new_position[0]),
                 (current_position[1], new_position[1]))
        intersection = intersect_compare(line, lines)
        lines.append(line)
        if not intersection:
            current_position = new_position
        else:
            return intersection
    return abs(current_position[0])+abs(current_position[1])

if __name__ == "__main__":
    with open('PuzzleInput.txt', 'r') as this_file:
        for instruction_line in this_file:
            instruction_line = instruction_line.replace('\n', '')
            instructions = instruction_line.split(', ')
            out = run(instructions)
    print(out)
    plt.show()
