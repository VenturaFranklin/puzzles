'''
Created on Dec 2, 2016
@author: venturf2

http://adventofcode.com/2016/day/2
--- Day 2: Bathroom Security ---

You arrive at Easter Bunny Headquarters under cover of darkness.
However, you left in such a rush that you forgot to use the bathroom!
Fancy office buildings like this one usually have keypad locks on their
bathrooms, so you search the front desk for the code.

"In order to improve security," the document you find says,
"bathroom codes will no longer be written down. Instead, please memorize
and follow the procedure below to access the bathrooms."

The document goes on to explain that each button to be pressed can be
found by starting on the previous button and moving to adjacent buttons
on the keypad: U moves up, D moves down, L moves left, and R moves right.
Each line of instructions corresponds to one button, starting at the
previous button (or, for the first line, the "5" button);
press whatever button you're on at the end of each line.
If a move doesn't lead to a button, ignore it.

You can't hold it much longer, so you decide to figure out the code
as you walk to the bathroom. You picture a keypad like this:

1 2 3
4 5 6
7 8 9
Suppose your instructions are:

ULL
RRDDD
LURDL
UUUUD
You start at "5" and move up (to "2"), left (to "1"), and left (you can't,
and stay on "1"), so the first button is 1.
Starting from the previous button ("1"), you move right twice (to "3") and
then down three times (stopping at "9" after two moves and ignoring the third),
ending up with 9.
Continuing from "9", you move left, up, right, down, and left, ending with 8.
Finally, you move up four times (stopping at "2"),
then down once, ending with 5.
So, in this example, the bathroom code is 1985.

Your puzzle input is the instructions from the document you found at the front
desk. What is the bathroom code?

--- Part Two ---

You finally arrive at the bathroom (it's a several minute walk from the lobby
so visitors can behold the many fancy conference rooms and water coolers on
this floor) and go to punch in the code. Much to your bladder's dismay,
the keypad is not at all like you imagined it. Instead, you are confronted
with the result of hundreds of man-hours of bathroom-keypad-design meetings:

    1
  2 3 4
5 6 7 8 9
  A B C
    D
You still start at "5" and stop when you're at an edge, but given the same
instructions as above, the outcome is very different:

You start at "5" and don't move at all (up and left are both edges),
ending at 5.
Continuing from "5", you move right twice and down three times
(through "6", "7", "B", "D", "D"), ending at D.
Then, from "D", you move five more times (through "D", "B", "C", "C", "B"),
ending at B.
Finally, after five more moves, you end at 3.
So, given the actual keypad layout, the code would be 5DB3.

Using the same instructions in your puzzle input, what is the correct
bathroom code?
'''
import numpy as np
from numpy import array

directions = {
    'U': array([-1, 0]),
    'D': array([1, 0]),
    'R': array([0, 1]),
    'L': array([0, -1]),
    }
keypad1 = array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

keypad2 = array([[0, 0, 1, 0, 0],
                [0, 2, 3, 4, 0],
                [5, 6, 7, 8, 9],
                [0, 'A', 'B', 'C', 0],
                [0, 0, 'D', 0, 0]])


def test1_run():
    keypad = keypad1
    instructions = 'ULL\nRRDDD\nLURDL\nUUUUD'.split('\n')
    key = 5
    actual_out = []
    for instruction in instructions:
        key = run(key, instruction, keypad)
        actual_out.append(key)
    actual_out = ''.join(map(str, actual_out))
    expected_out = '1985'
    assert expected_out == actual_out


def test2_run():
    keypad = keypad2
    instructions = 'ULL\nRRDDD\nLURDL\nUUUUD'.split('\n')
    key = 5
    actual_out = []
    for instruction in instructions:
        key = run(key, instruction, keypad)
        actual_out.append(key)
    actual_out = ''.join(map(str, actual_out))
    expected_out = '5DB3'
    assert expected_out == actual_out


def run(start_key, instruction_line, keypad):
    current_position = array(zip(*np.where(keypad == str(start_key)))[0])
    max_pos = keypad.shape[0] - 1
    for direction in instruction_line:
        next_position = current_position + directions[direction]
        if ((next_position >= 0).all() and (next_position <= max_pos).all()):
            value = keypad[next_position[0]][next_position[1]]
            if value != '0':
                current_position = next_position
    return keypad[current_position[0]][current_position[1]]

if __name__ == "__main__":
    out = []
    key = 5
    with open('PuzzleInput.txt', 'r') as this_file:
        for instruction_line in this_file:
            instruction_line = instruction_line.replace('\n', '')
            key = run(key, instruction_line, keypad2)
            out.append(key)
    out = ''.join(map(str, out))
    print(out)
