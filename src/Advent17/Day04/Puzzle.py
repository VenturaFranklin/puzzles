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

--- Part Two ---
For added security, yet another system policy has been put in place.
Now, a valid passphrase must contain no two words that are anagrams of
each other - that is, a passphrase is invalid if any word's letters can be
rearranged to form any other word in the passphrase.

For example:

abcde fghij is a valid passphrase.
abcde xyz ecdab is not valid - the letters from the
    third word can be rearranged to form the first word.
a ab abc abd abf abj is a valid passphrase,
    because all letters need to be used when forming another word.
iiii oiii ooii oooi oooo is valid.
oiii ioii iioi iiio is not valid - any of these words can be
    rearranged to form any other word.
Under this new system policy, how many passphrases are valid?
'''
# from collections import Counter


def test_p10():
    testing = '''aa bb cc dd ee
aa bb cc dd aa
aa bb cc dd aaa'''
    actual_out = run(testing)
    expected_out = 2
    assert actual_out == expected_out, "{} != {}".format(actual_out,
                                                         expected_out)


def run(passphrases):
    count = 0
    passphrases = passphrases.split("\n")
    for passphrase in passphrases:
        words = passphrase.split(" ")
        print(words)
        valid = int(len(set(words)) == len(words))
        count += valid
    return count


def test_p20():
    testing = '''abcde fghij
abcde xyz ecdab
a ab abc abd abf abj
iiii oiii ooii oooi oooo
oiii ioii iioi iiio'''
    actual_out = run2(testing)
    expected_out = 3
    assert actual_out == expected_out, "{} != {}".format(actual_out,
                                                         expected_out)


def run2(test):
    out = test
    return out


if __name__ == "__main__":
    with open('input.txt', 'r') as this_file:
        text = this_file.read()
        out = run(text[:-1])  # Because the final new line causes problems
    print(out)
