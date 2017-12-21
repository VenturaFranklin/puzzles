'''
Created on Dec 20, 2017

@author: venturf2

--- Day 8: I Heard You Like Registers ---
You receive a signal directly from the CPU.
Because of your recent assistance with jump instructions,
it would like you to compute the result of a series of unusual
register instructions.

Each instruction consists of several parts:
the register to modify, whether to increase or decrease that register's value,
the amount by which to increase or decrease it, and a condition.
If the condition fails, skip the instruction without modifying the register.
The registers all start at 0. The instructions look like this:

b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10
These instructions would be processed as follows:

Because a starts at 0, it is not greater than 1, and so b is not modified.
a is increased by 1 (to 1) because b is less than 5 (it is 0).
c is decreased by -10 (to 10)
    because a is now greater than or equal to 1 (it is 1).
c is increased by -20 (to -10) because c is equal to 10.
After this process, the largest value in any register is 1.

You might also encounter <= (less than or equal to) or != (not equal to).
However, the CPU doesn't have the bandwidth
to tell you what all the registers are named,
and leaves that to you to determine.

What is the largest value in any register after
completing the instructions in your puzzle input?
'''
from collections import defaultdict
import operator
ops = {
    '<': operator.lt,
    '<=': operator.le,
    '==': operator.eq,
    '!=': operator.ne,
    '>=': operator.ge,
    '>': operator.gt
    }

def test_p10():
    testing = '''b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10'''
    actual_out = run(testing)
    expected_out = 1
    assert actual_out == expected_out, "{} != {}".format(actual_out,
                                                         expected_out)


def run(test):
    rows = test.split('\n')
    values = defaultdict(int)
    for row in rows:
        instructions, condition = row.split(' if ')
        var_check, op, test = condition.split(' ')
        var_check_val = values[var_check]
        if 'inc' in instructions:
            change = 1
            direction = ' inc '
        else:
            change = -1
            direction = ' dec '
        if ops[op](var_check_val, int(test)):
            var_change, val = instructions.split(direction)
            values[var_change] += int(val) * change
    print(values)
    return max([val for val in values.values()])


# def test_p20():
#     testing = '''5\t9\t2\t8\n9\t4\t7\t3\n3\t8\t6\t5'''
#     actual_out = run2(testing)
#     expected_out = 9
#     assert actual_out == expected_out, "{} != {}".format(actual_out,
#                                                          expected_out)


def run2(test):
    rows = test.split('\n')
    out = rows
    return out


if __name__ == "__main__":
    with open('input.txt', 'r') as this_file:
        text = this_file.read()
        out = run(text[:-1])  # Because the final new line causes problems
    print(out)
