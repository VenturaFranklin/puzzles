'''
Created on Dec 20, 2017

@author: venturf2

--- Day 14: Disk Defragmentation ---
Suddenly, a scheduled job activates the system's disk defragmenter. Were the situation different, you might sit and watch it for a while, but today, you just don't have that kind of time. It's soaking up valuable system resources that are needed elsewhere, and so the only option is to help it finish its task as soon as possible.

The disk in question consists of a 128x128 grid; each square of the grid is either free or used. On this disk, the state of the grid is tracked by the bits in a sequence of knot hashes.

A total of 128 knot hashes are calculated, each corresponding to a single row in the grid; each hash contains 128 bits which correspond to individual grid squares. Each bit of a hash indicates whether that square is free (0) or used (1).

The hash inputs are a key string (your puzzle input), a dash, and a number from 0 to 127 corresponding to the row. For example, if your key string were flqrgnkx, then the first row would be given by the bits of the knot hash of flqrgnkx-0, the second row from the bits of the knot hash of flqrgnkx-1, and so on until the last row, flqrgnkx-127.

The output of a knot hash is traditionally represented by 32 hexadecimal digits; each of these digits correspond to 4 bits, for a total of 4 * 32 = 128 bits. To convert to bits, turn each hexadecimal digit to its equivalent binary value, high-bit first: 0 becomes 0000, 1 becomes 0001, e becomes 1110, f becomes 1111, and so on; a hash that begins with a0c2017... in hexadecimal would begin with 10100000110000100000000101110000... in binary.

Continuing this process, the first 8 rows and columns for key flqrgnkx appear as follows, using # to denote used squares, and . to denote free ones:

##.#.#..-->
.#.#.#.#   
....#.#.   
#.#.##.#   
.##.#...   
##..#..#   
.#...#..   
##.#.##.-->
|      |   
V      V   
In this example, 8108 squares are used across the entire 128x128 grid.

Given your actual key string, how many squares are used?

Your puzzle input is hfdlxzhv.
'''


def test_p10():
    testing = '''5\t1\t9\t5\n7\t5\t3\n2\t4\t6\t8'''
    actual_out = run(testing)
    expected_out = 18
    assert actual_out == expected_out, "{} != {}".format(actual_out,
                                                         expected_out)


def run(test):
    rows = test.split('\n')
    out = 0
    for row in rows:
        cols = row.split('\t')
        print(cols)
        cols = [int(x) for x in cols]
        print(cols)
        diff = max(cols) - min(cols)
        out += diff
    return out


def test_p20():
    testing = '''5\t9\t2\t8\n9\t4\t7\t3\n3\t8\t6\t5'''
    actual_out = run2(testing)
    expected_out = 9
    assert actual_out == expected_out, "{} != {}".format(actual_out,
                                                         expected_out)



def run2(test):
    rows = test.split('\n')
    out = 0
    for row in rows:
        cols = row.split('\t')
        cols = [int(x) for x in cols]
        val = [divisible(x) for x in itertools.combinations(cols, 2)
               if divisible(x) > 0][0]
        out += val
    return out


if __name__ == "__main__":
    with open('PuzzleInput.txt', 'r') as this_file:
        out = run2(this_file.read())
    print(out)
