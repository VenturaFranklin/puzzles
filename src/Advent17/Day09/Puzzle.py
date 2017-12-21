'''
Created on Dec 20, 2017

@author: venturf2

--- Day 9: Stream Processing ---
A large stream blocks your path. According to the locals,
it's not safe to cross the stream at the moment because it's full of garbage.
You look down at the stream; rather than water,
you discover that it's a stream of characters.

You sit for a while and record part of the stream (your puzzle input).
The characters represent groups - sequences that begin with { and end with }.
Within a group, there are zero or more other things, separated by commas:
either another group or garbage. Since groups can contain other groups, a }
only closes the most-recently-opened unclosed group - that is,
they are nestable. Your puzzle input represents a single,
large group which itself contains many smaller ones.

Sometimes, instead of a group, you will find garbage.
Garbage begins with < and ends with >. Between those angle brackets,
almost any character can appear, including { and }.
Within garbage, < has no special meaning.

In a futile attempt to clean up the garbage,
some program has canceled some of the characters within it using !:
inside garbage, any character that comes after ! should be ignored,
including <, >, and even another !.

You don't see any characters that deviate from these rules.
Outside garbage, you only find well-formed groups,
and garbage always terminates according to the rules above.

Here are some self-contained pieces of garbage:

<>, empty garbage.
<random characters>, garbage containing random characters.
<<<<>, because the extra < are ignored.
<{!>}>, because the first > is canceled.
<!!>, because the second ! is canceled,
    allowing the > to terminate the garbage.
<!!!>>, because the second ! and the first > are canceled.
<{o"i!a,<{i<a>, which ends at the first >.
Here are some examples of whole streams and the number of groups they contain:

{}, 1 group.
{{{}}}, 3 groups.
{{},{}}, also 3 groups.
{{{},{},{{}}}}, 6 groups.
{<{},{},{{}}>}, 1 group (which itself contains garbage).
{<a>,<a>,<a>,<a>}, 1 group.
{{<a>},{<a>},{<a>},{<a>}}, 5 groups.
{{<!>},{<!>},{<!>},{<a>}}, 2 groups (since all but the last > are canceled).
Your goal is to find the total score for all groups in your input.
Each group is assigned a score which is one more
than the score of the group that immediately contains it.
(The outermost group gets a score of 1.)

{}, score of 1.
{{{}}}, score of 1 + 2 + 3 = 6.
{{},{}}, score of 1 + 2 + 2 = 5.
{{{},{},{{}}}}, score of 1 + 2 + 3 + 3 + 3 + 4 = 16.
{<a>,<a>,<a>,<a>}, score of 1.
{{<ab>},{<ab>},{<ab>},{<ab>}}, score of 1 + 2 + 2 + 2 + 2 = 9.
{{<!!>},{<!!>},{<!!>},{<!!>}}, score of 1 + 2 + 2 + 2 + 2 = 9.
{{<a!>},{<a!>},{<a!>},{<ab>}}, score of 1 + 2 = 3.
What is the total score for all groups in your input?
'''


def test_p10():
    testing = '''{}'''
    actual_out = run(testing)
    expected_out = 1
    assert actual_out == expected_out, "{} != {}".format(actual_out,
                                                         expected_out)


def test_p11():
    testing = '''{{{}}}'''
    actual_out = run(testing)
    expected_out = 6
    assert actual_out == expected_out, "{} != {}".format(actual_out,
                                                         expected_out)


def test_p12():
    testing = '''{{},{}}'''
    actual_out = run(testing)
    expected_out = 5
    assert actual_out == expected_out, "{} != {}".format(actual_out,
                                                         expected_out)


def test_p13():
    testing = '''{{{},{},{{}}}}'''
    actual_out = run(testing)
    expected_out = 16
    assert actual_out == expected_out, "{} != {}".format(actual_out,
                                                         expected_out)


def test_p14():
    testing = '''{<a>,<a>,<a>,<a>}'''
    actual_out = run(testing)
    expected_out = 1
    assert actual_out == expected_out, "{} != {}".format(actual_out,
                                                         expected_out)


def test_p15():
    testing = '''{{<ab>},{<ab>},{<ab>},{<ab>}}'''
    actual_out = run(testing)
    expected_out = 9
    assert actual_out == expected_out, "{} != {}".format(actual_out,
                                                         expected_out)


def test_p16():
    testing = '''{{<!!>},{<!!>},{<!!>},{<!!>}}'''
    actual_out = run(testing)
    expected_out = 9
    assert actual_out == expected_out, "{} != {}".format(actual_out,
                                                         expected_out)


def test_p17():
    testing = '''{{<a!>},{<a!>},{<a!>},{<ab>}}'''
    actual_out = run(testing)
    expected_out = 3
    assert actual_out == expected_out, "{} != {}".format(actual_out,
                                                         expected_out)


def test_p18():
    testing = '''{<{},{},{{}}>}'''
    actual_out = run(testing)
    expected_out = 1
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
        text = this_file.read()
        out = run(text[:-1])  # Because the final new line causes problems
    print(out)
