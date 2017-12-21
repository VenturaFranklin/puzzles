'''
Created on Dec 20, 2017

@author: venturf2

Puzzle Description
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
