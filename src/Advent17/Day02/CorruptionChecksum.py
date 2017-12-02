'''
Created on Dec 2, 2017

@author: venturf2

--- Day 2: Corruption Checksum ---

As you walk through the door, a glowing humanoid shape yells in your direction.
"You there! Your state appears to be idle.
Come help us repair the corruption in this spreadsheet - if we take another
millisecond, we'll have to display an hourglass cursor!"

The spreadsheet consists of rows of apparently-random numbers. To make sure the
recovery process is on the right track, they need you to calculate the
spreadsheet's checksum. For each row, determine the difference
between the largest value and the smallest value;
the checksum is the sum of all of these differences.

For example, given the following spreadsheet:

5 1 9 5
7 5 3
2 4 6 8
The first row's largest and smallest values are 9 and 1,
and their difference is 8.
The second row's largest and smallest values are 7 and 3,
and their difference is 4.
The third row's difference is 6.
In this example, the spreadsheet's checksum would be 8 + 4 + 6 = 18.

What is the checksum for the spreadsheet in your puzzle input?
'''


def test_p10():
    testing	=	'''5	1	9	5\n7	5	3\n2	4	6	8'''
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
    testing = ''''''
    actual_out = run2(testing)
    expected_out = 6
    assert actual_out == expected_out, "{} != {}".format(actual_out,
                                                         expected_out)


def run2(test):
    out = test
    return out


if __name__ == "__main__":
    with open('PuzzleInput.txt', 'r') as this_file:
        out = run(this_file.read())
    print(out)
