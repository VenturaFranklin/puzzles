'''
Created on Dec 20, 2017

@author: venturf2

--- Day 11: Hex Ed ---
Crossing the bridge, you've barely reached the other side of the stream when a program comes up to you, clearly in distress. "It's my child process," she says, "he's gotten lost in an infinite grid!"

Fortunately for her, you have plenty of experience with infinite grids.

Unfortunately for you, it's a hex grid.

The hexagons ("hexes") in this grid are aligned such that adjacent hexes can be found to the north, northeast, southeast, south, southwest, and northwest:

  \ n  /
nw +--+ ne
  /    \
-+      +-
  \    /
sw +--+ se
  / s  \
You have the path the child process took. Starting where he started, you need to determine the fewest number of steps required to reach him. (A "step" means to move from the hex you are in to any adjacent hex.)

For example:

ne,ne,ne is 3 steps away.
ne,ne,sw,sw is 0 steps away (back where you started).
ne,ne,s,s is 2 steps away (se,se).
se,sw,se,sw,sw is 3 steps away (s,s,sw).
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
