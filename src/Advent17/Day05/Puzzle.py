'''
Created on Dec 20, 2017

@author: venturf2

--- Day 5: A Maze of Twisty Trampolines, All Alike ---
An urgent interrupt arrives from the CPU: it's trapped in a maze of
jump instructions, and it would like assistance from any programs with
spare cycles to help find the exit.

The message includes a list of the offsets for each jump.
Jumps are relative: -1 moves to the previous instruction,
and 2 skips the next one. Start at the first instruction in the list.
The goal is to follow the jumps until one leads outside the list.

In addition, these instructions are a little strange;
after each jump, the offset of that instruction increases by 1.
So, if you come across an offset of 3,
you would move three instructions forward, but change it to a 4
for the next time it is encountered.

For example, consider the following list of jump offsets:

0
3
0
1
-3
Positive jumps ("forward") move downward;
negative jumps move upward. For legibility in this example,
these offset values will be written all on one line,
with the current instruction marked in parentheses.
The following steps would be taken before an exit is found:

(0) 3  0  1  -3  - before we have taken any steps.
(1) 3  0  1  -3  - jump with offset 0 (that is, don't jump at all).
    Fortunately, the instruction is then incremented to 1.
 2 (3) 0  1  -3  - step forward because of the instruction we just modified.
     The first instruction is incremented again, now to 2.
 2  4  0  1 (-3) - jump all the way to the end; leave a 4 behind.
 2 (4) 0  1  -2  - go back to where we just were; increment -3 to -2.
 2  5  0  1  -2  - jump 4 steps forward, escaping the maze.
In this example, the exit is reached in 5 steps.

How many steps does it take to reach the exit?
'''


def test_p10():
    testing = '''0
3
0
1
-3'''
    actual_out = run(testing)
    expected_out = 5
    assert actual_out == expected_out, "{} != {}".format(actual_out,
                                                         expected_out)


def run(test):
    rows = test.split('\n')
    rows = [int(row) for row in rows]
    new_loc = 0
    length = len(rows)
    count = 0
    while new_loc < length and new_loc >= 0:
        instruction = rows[new_loc]
        rows[new_loc] += 1
        new_loc += instruction
        count += 1
    return count


# def test_p20():
#     testing = '''5\t9\t2\t8\n9\t4\t7\t3\n3\t8\t6\t5'''
#     actual_out = run2(testing)
#     expected_out = 9
#     assert actual_out == expected_out, "{} != {}".format(actual_out,
#                                                          expected_out)
# 
# 
# 
# def run2(test):
#     rows = test.split('\n')
#     out = test
#     return out


if __name__ == "__main__":
    with open('input.txt', 'r') as this_file:
        text = this_file.read()
        out = run(text[:-1])  # Because the final new line causes problems
    print(out)
