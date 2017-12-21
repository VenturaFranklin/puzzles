'''
Created on Dec 20, 2017

@author: venturf2

--- Day 4: High-Entropy Passphrases ---
A new system policy has been put in place that requires all accounts
to use a passphrase instead of simply a password.
A passphrase consists of a series of words (lowercase letters)
separated by spaces.

To ensure security, a valid passphrase must contain no duplicate words.

For example:

aa bb cc dd ee is valid.
aa bb cc dd aa is not valid - the word aa appears more than once.
aa bb cc dd aaa is valid - aa and aaa count as different words.
The system's full passphrase list is available as your puzzle input.
How many passphrases are valid?
'''


def test_p10():
    testing = '''aa bb cc dd ee'''
    actual_out = run(testing)
    expected_out = True
    assert actual_out == expected_out, "{} != {}".format(actual_out,
                                                         expected_out)

def test_p11():
    testing = '''aa bb cc dd aa'''
    actual_out = run(testing)
    expected_out = False
    assert actual_out == expected_out, "{} != {}".format(actual_out,
                                                         expected_out)

def test_p12():
    testing = '''aa bb cc dd aaa'''
    actual_out = run(testing)
    expected_out = True
    assert actual_out == expected_out, "{} != {}".format(actual_out,
                                                         expected_out)

def run(test):
    out = test
    return out


# def test_p20():
#     testing = '''5\t9\t2\t8\n9\t4\t7\t3\n3\t8\t6\t5'''
#     actual_out = run2(testing)
#     expected_out = 9
#     assert actual_out == expected_out, "{} != {}".format(actual_out,
#                                                          expected_out)


# def run2(test):
#     out = test
#     return out


if __name__ == "__main__":
    with open('input.txt', 'r') as this_file:
        out = run(this_file.read())
    print(out)
