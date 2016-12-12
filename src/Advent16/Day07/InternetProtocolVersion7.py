'''
Created on Dec 6, 2016

@author: venturf2
http://adventofcode.com/2016/day/5

--- Day 7: Internet Protocol Version 7 ---

While snooping around the local network of EBHQ, you compile a list of IP
addresses (they're IPv7, of course; IPv6 is much too limited).
You'd like to figure out which IPs support TLS (transport-layer snooping).

An IP supports TLS if it has an Autonomous Bridge Bypass Annotation, or ABBA.
An ABBA is any four-character sequence which consists of a pair of two
different characters followed by the reverse of that pair,
such as xyyx or abba. However, the IP also must not have an ABBA within any
hypernet sequences, which are contained by square brackets.

For example:

abba[mnop]qrst supports TLS (abba outside square brackets).
abcd[bddb]xyyx does not support TLS (bddb is within square brackets,
even though xyyx is outside square brackets).
aaaa[qwer]tyui does not support TLS
(aaaa is invalid; the interior characters must be different).
ioxxoj[asdfgh]zxcvbn supports TLS
(oxxo is outside square brackets, even though it's within a larger string).
How many IPs in your puzzle input support TLS?

--- Part Two ---

You would also like to know which IPs support SSL (super-secret listening).

An IP supports SSL if it has an Area-Broadcast Accessor, or ABA,
anywhere in the supernet sequences (outside any square bracketed sections),
and a corresponding Byte Allocation Block, or BAB,
anywhere in the hypernet sequences.
An ABA is any three-character sequence which consists of the same character
twice with a different character between them, such as xyx or aba.
A corresponding BAB is the same characters but in reversed positions:
yxy and bab, respectively.

For example:

aba[bab]xyz supports SSL (aba outside square brackets with corresponding
bab within square brackets).
xyx[xyx]xyx does not support SSL (xyx, but no corresponding yxy).
aaa[kek]eke supports SSL (eke in supernet with corresponding kek in hypernet;
the aaa sequence is not related,
because the interior character must be different).
zazbz[bzb]cdb supports SSL (zaz has no corresponding aza,
but zbz has a corresponding bzb, even though zaz and zbz overlap).

How many IPs in your puzzle input support SSL?
'''


def test_1():
    ip_test_list = [('abba[mnop]qrst', True),
                    ('abcd[bddb]xyyx', False),
                    ('aaaa[qwer]tyui', False),
                    ('ioxxoj[asdfgh]zxcvbn', True)]
    for test in ip_test_list:
        test_ip, expected_out = test
        actual_out = run(test_ip)
        assert actual_out == expected_out


def test_2():
    ip_test_list = [('aba[bab]xyz', True),
                    ('xyx[xyx]xyx', False),
                    ('aaa[kek]eke', True),
                    ('zazbz[bzb]cdb', True)]
    for test in ip_test_list:
        test_ip, expected_out = test
        actual_out = run(test_ip)
        assert actual_out == expected_out


def split_ip(test_ip):
    splits = test_ip.split('[')
    all_splits = {'hypernet': [],
                  'supernet': []}
    for spl in splits:
        if ']' in spl:
            this_split = spl.split(']')
            all_splits['hypernet'].append(this_split[0])
            all_splits['supernet'].append(this_split[1])
        else:
            all_splits['supernet'].append(spl)
    return all_splits


def abba(test):
    first = test[::2]
    second = test[1::2][::-1]
    if first[0] == first[1]:
        return False
    else:
        return first == second


def aba(test):
    return (test[0] == test[2]) & (test[0] != test[1])


def aba_bab(abas, test):
    for aba in abas:
        if (aba[0] == test[1]) & (aba[1] == test[0]):
            return True
    return False


def subgroups(this_string, sub_len=3):
    return [this_string[i:i+sub_len] for i in range(len(this_string))
            if i+sub_len <= len(this_string)]


def run(test_ip):
    splits = split_ip(test_ip)
    abas = []
    for test_split in splits['supernet']:
        for test in subgroups(test_split):
            if aba(test):
                abas.append(test)
    for test_split in splits['hypernet']:
        for test in subgroups(test_split):
            if aba(test):
                if aba_bab(abas, test):
                    return True
    return False

if __name__ == "__main__":
    count = 0
    with open('PuzzleInput.txt', 'r') as this_file:
        for test_ip in this_file:
            test_ip = test_ip.replace('\n', '')
            if run(test_ip):
                count += 1
    print(count)
