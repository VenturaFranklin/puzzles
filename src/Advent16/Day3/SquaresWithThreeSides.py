'''
Created on Dec 2, 2016

@author: venturf2

--- Day 3: Squares With Three Sides ---

Now that you can think clearly, you move deeper into the labyrinth of hallways
and office furniture that makes up this part of Easter Bunny HQ.
This must be a graphic design department; the walls are covered in
specifications for triangles.

Or are they?

The design document gives the side lengths of each triangle it describes,
but... 5 10 25? Some of these aren't triangles.
You can't help but mark the impossible ones.

In a valid triangle, the sum of any two sides must be larger
than the remaining side. For example, the "triangle" given above is impossible,
because 5 + 10 is not larger than 25.

In your puzzle input, how many of the listed triangles are possible?
'''


def test1_run():
    sides = [5, 10, 25]
    actual_out = run(sides)
    expected_out = False
    assert actual_out == expected_out


def run(sides):
    sides = map(int, sides)
    sides.sort()
    l1, l2, l3 = sides
    if (l1 > l2+l3) or (l2 > l1+l3) or (l3 > l1+l2):
        return False
    elif (l1 == l2+l3) or (l2 == l1+l3) or (l3 == l1+l2):
        return False
    else:
        return True

if __name__ == "__main__":
#     test1_run()
    count = 0
    with open('PuzzleInput.txt', 'r') as this_file:
        for side in this_file:
            side = side.replace('\n', '')
            side = side.strip()
            side = side.split('  ')
            side = map(str.strip, side)
            if '' in side:
                side.remove('')
            print(side)
            if run(side):
                count += 1
    print(count)
