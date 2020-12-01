'''
Created on Dec 18, 2018
@author: venturf2

--- Day 17: Reservoir Research ---
You arrive in the year 18. If it weren't for the coat you got in 1018,
you would be very cold: the North Pole base hasn't even been constructed.

Rather, it hasn't been constructed yet. The Elves are making a little progress,
but there's not a lot of liquid water in this climate,
so they're getting very dehydrated. Maybe there's more underground?

You scan a two-dimensional vertical slice of the ground nearby and discover
that it is mostly sand with veins of clay.
The scan only provides data with a granularity of square meters,
but it should be good enough to determine how much water is trapped there.
In the scan, x represents the distance to the right,
and y represents the distance down.
There is also a spring of water near the surface at x=500, y=0.
The scan identifies which square meters are clay (your puzzle input).

For example, suppose your scan shows the following veins of clay:

x=495, y=2..7
y=7, x=495..501
x=501, y=3..7
x=498, y=2..4
x=506, y=1..2
x=498, y=10..13
x=504, y=10..13
y=13, x=498..504
Rendering clay as #, sand as ., and the water spring as +,
and with x increasing to the right and y increasing downward, this becomes:

   44444455555555
   99999900000000
   45678901234567
 0 ......+.......
 1 ............#.
 2 .#..#.......#.
 3 .#..#..#......
 4 .#..#..#......
 5 .#.....#......
 6 .#.....#......
 7 .#######......
 8 ..............
 9 ..............
10 ....#.....#...
11 ....#.....#...
12 ....#.....#...
13 ....#######...
The spring of water will produce water forever.
Water can move through sand, but is blocked by clay.
Water always moves down when possible,
and spreads to the left and right otherwise,
filling space that has clay on both sides and falling out otherwise.

For example, if five squares of water are created,
they will flow downward until they reach the clay and settle there.
Water that has come to rest is shown here as ~,
while sand through which water has passed
(but which is now dry again) is shown as |:

......+.......
......|.....#.
.#..#.|.....#.
.#..#.|#......
.#..#.|#......
.#....|#......
.#~~~~~#......
.#######......
..............
..............
....#.....#...
....#.....#...
....#.....#...
....#######...
Two squares of water can't occupy the same location.
If another five squares of water are created,
they will settle on the first five, filling the clay reservoir a little more:

......+.......
......|.....#.
.#..#.|.....#.
.#..#.|#......
.#..#.|#......
.#~~~~~#......
.#~~~~~#......
.#######......
..............
..............
....#.....#...
....#.....#...
....#.....#...
....#######...
Water pressure does not apply in this scenario.
If another four squares of water are created,
they will stay on the right side of the barrier,
and no water will reach the left side:

......+.......
......|.....#.
.#..#.|.....#.
.#..#~~#......
.#..#~~#......
.#~~~~~#......
.#~~~~~#......
.#######......
..............
..............
....#.....#...
....#.....#...
....#.....#...
....#######...
At this point, the top reservoir overflows.
While water can reach the tiles above the surface of the water,
it cannot settle there, and so the next five squares of water settle like this:

......+.......
......|.....#.
.#..#||||...#.
.#..#~~#|.....
.#..#~~#|.....
.#~~~~~#|.....
.#~~~~~#|.....
.#######|.....
........|.....
........|.....
....#...|.#...
....#...|.#...
....#~~~~~#...
....#######...
Note especially the leftmost |: the new squares of water can reach this tile,
but cannot stop there. Instead, eventually,
they all fall to the right and settle in the reservoir below.

After 10 more squares of water, the bottom reservoir is also full:

......+.......
......|.....#.
.#..#||||...#.
.#..#~~#|.....
.#..#~~#|.....
.#~~~~~#|.....
.#~~~~~#|.....
.#######|.....
........|.....
........|.....
....#~~~~~#...
....#~~~~~#...
....#~~~~~#...
....#######...
Finally, while there is nowhere left for the water to settle,
it can reach a few more tiles before overflowing
beyond the bottom of the scanned data:

......+.......    (line not counted: above minimum y value)
......|.....#.
.#..#||||...#.
.#..#~~#|.....
.#..#~~#|.....
.#~~~~~#|.....
.#~~~~~#|.....
.#######|.....
........|.....
...|||||||||..
...|#~~~~~#|..
...|#~~~~~#|..
...|#~~~~~#|..
...|#######|..
...|.......|..    (line not counted: below maximum y value)
...|.......|..    (line not counted: below maximum y value)
...|.......|..    (line not counted: below maximum y value)
How many tiles can be reached by the water?
To prevent counting forever, ignore tiles with a y coordinate smaller than the
smallest y coordinate in your scan data or larger than the largest one.
Any x coordinate is valid. In this example, the lowest y coordinate given is 1,
and the highest is 13, causing the water spring (in row 0)
and the water falling off the bottom of the render
(in rows 14 through infinity) to be ignored.

So, in the example above, counting both water at rest (~) and other sand tiles
the water can hypothetically reach (|),
the total number of tiles the water can reach is 57.

How many tiles can the water reach within the range of y values in your scan?

'''
import numpy as np
from operator import itemgetter


def test1_1_run():
    instructions = [
        'x=495, y=2..7',
        'y=7, x=495..501',
        'x=501, y=3..7',
        'x=498, y=2..4',
        'x=506, y=1..2',
        'x=498, y=10..13',
        'x=504, y=10..13',
        'y=13, x=498..504',
]
    expected_out = \
"""
......+.......
............#.
.#..#.......#.
.#..#..#......
.#..#..#......
.#.....#......
.#.....#......
.#######......
..............
..............
....#.....#...
....#.....#...
....#.....#...
....#######..."""
    actual_out = run(instructions)
    assert expected_out == actual_out


def parse_instructions(instruct):
    instructions = instruct.split(', ')
    info = {}
    max_info = {'x': 0, 'y': 0}
    min_info = {'x': 500000, 'y': 500000}
    for instruct in instructions:
        if 'x=' in instruct:
            dir = 'x'
            value = instruct.split('x=')[1]
        if 'y=' in instruct:
            dir = 'y'
            value = instruct.split('y=')[1]
        if '..' in value:
            values = value.split('..')
        else:
            values = [value]
        info[dir] = list(map(int, values))
        max_info[dir] = max(max_info[dir], *info[dir])
        min_info[dir] = min(min_info[dir], *info[dir])
    return info, (max_info['x'], max_info['y']), (min_info['x'], min_info['y']) 


def convert_out(line_in):
    line_in = list(line_in)
    return ['#' if x == 8 else '.' for x in line_in]


def draw_map(instructions):
    instruction_list, max_list, min_list = zip(*instructions)
    max_x = max(max_list, key=itemgetter(0))[0] + 1
    max_y = max(max_list, key=itemgetter(1))[1]
    min_x = min(min_list, key=itemgetter(0))[0] - 1
    min_y = 0  # min(min_list, key=itemgetter(1))[1]
    mapping = np.zeros((max_y + 1, max_x - min_x + 1))
    for instruct in instruction_list:
        mapping[instruct['y'][0]:instruct['y'][-1] + 1,
                instruct['x'][0] - min_x:instruct['x'][-1] - min_x + 1] = 8
    return map(convert_out, list(mapping))


def run(instructions):
    new_instructions = list(map(parse_instructions, instructions))
    test = list(draw_map(new_instructions))
    pass


def run2(instructions, current_freq=0, previous_freqs=None):
    if previous_freqs is None:
        previous_freqs = {current_freq}
    for instruct in instructions:
        current_freq += int(instruct)
        if current_freq in previous_freqs:
            return current_freq
        else:
            previous_freqs.append(current_freq)
    return run2(instructions, current_freq, previous_freqs)


if __name__ == "__main__":
    with open('PuzzleInput.txt', 'r') as this_file:
        instructions = []
        for instruction_line in this_file:
            instruction_line = instruction_line.replace('\n', '')
            instructions.append(instruction_line)
        out = run2(instructions)
    print(out)
