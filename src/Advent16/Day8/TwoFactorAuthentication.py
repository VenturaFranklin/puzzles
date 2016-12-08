'''
Created on Dec 8, 2016

@author: venturf2
http://adventofcode.com/2016/day/8

--- Day 8: Two-Factor Authentication ---

You come across a door implementing what you can only assume is an
implementation of two-factor authentication after a long game of
requirements telephone.

To get past the door, you first swipe a keycard
(no problem; there was one on a nearby desk).
Then, it displays a code on a little screen,
and you type that code on a keypad. Then, presumably, the door unlocks.

Unfortunately, the screen has been smashed. After a few minutes,
you've taken everything apart and figured out how it works.
Now you just have to work out what the screen would have displayed.

The magnetic strip on the card you swiped encodes a series of instructions
for the screen; these instructions are your puzzle input.
The screen is 50 pixels wide and 6 pixels tall, all of which start off,
and is capable of three somewhat peculiar operations:

rect AxB turns on all of the pixels in a rectangle at the top-left of the
screen which is A wide and B tall.
rotate row y=A by B shifts all of the pixels in row A (0 is the top row)
right by B pixels. Pixels that would fall off the right end appear
at the left end of the row.
rotate column x=A by B shifts all of the pixels in column A
(0 is the left column) down by B pixels. Pixels that would fall off the
bottom appear at the top of the column.
For example, here is a simple sequence on a smaller screen:

rect 3x2 creates a small rectangle in the top-left corner:

###....
###....
.......
rotate column x=1 by 1 rotates the second column down by one pixel:

#.#....
###....
.#.....
rotate row y=0 by 4 rotates the top row right by four pixels:

....#.#
###....
.#.....
rotate column x=1 by 1 again rotates the second column down by one pixel,
causing the bottom pixel to wrap back to the top:

.#..#.#
#.#....
.#.....
As you can see, this display technology is extremely powerful,
and will soon dominate the tiny-code-displaying-screen market.
That's what the advertisement on the back of the display
tries to convince you, anyway.

There seems to be an intermediate check of the voltage used by the display:
after you swipe your card, if the screen did work,
how many pixels should be lit?
'''
from numpy import array, roll, zeros, count_nonzero


def test_1():
    instructions = '''rect 3x2
rotate column x=1 by 1
rotate row y=0 by 4
rotate column x=1 by 1'''
    main_array = zeros((3, 7))
    actual_out = run(instructions, main_array)
    expected_out = array([[0, 1, 0, 0, 1, 0, 1],
                          [1, 0, 1, 0, 0, 0, 0],
                          [0, 1, 0, 0, 0, 0, 0]])
    assert actual_out.all() == expected_out.all()


def run(instructions, main_array):
    instructions = instructions.split('\n')
    for instruction in instructions:
        if 'rect' in instruction:
            a, b = instruction.split(' ')[1].split('x')
            main_array[0:int(b), 0:int(a)] = 1
        else:
            direction, shift = instruction.split('=')
            direction = int(direction[-1] == 'y')
            start, shift = shift.split(' by ')
            start, shift = int(start), int(shift)
            shifted = roll(main_array, shift, direction)
            if direction:
                shifted_row = shifted[start]
                main_array[start] = shifted_row
            else:
                shifted_col = shifted[:, start]
                main_array[:, start] = shifted_col
    return main_array

if __name__ == "__main__":
#     test_1()
    main_array = zeros((6, 50))
    with open('PuzzleInput.txt', 'r') as this_file:
        out = run(this_file.read(), main_array)
    print(count_nonzero(out))

