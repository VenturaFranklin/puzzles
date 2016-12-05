'''
Created on Dec 4, 2016

@author: venturf2
http://adventofcode.com/2016/day/4

--- Day 4: Security Through Obscurity ---

Finally, you come across an information kiosk with a list of rooms. Of course,
the list is encrypted and full of decoy data, but the instructions to decode
the list are barely hidden nearby. Better remove the decoy data first.

Each room consists of an encrypted name (lowercase letters separated by dashes)
followed by a dash, a sector ID, and a checksum in square brackets.

A room is real (not a decoy) if the checksum is the five most common letters in
the encrypted name, in order, with ties broken by alphabetization. For example:

aaaaa-bbb-z-y-x-123[abxyz] is a real room because the most common letters are
a (5), b (3), and then a tie between x, y, and z, which are listed
alphabetically.
a-b-c-d-e-f-g-h-987[abcde] is a real room because although the letters are all
tied (1 of each), the first five are listed alphabetically.
not-a-real-room-404[oarel] is a real room.
totally-real-room-200[decoy] is not.
Of the real rooms from the list above, the sum of their sector IDs is 1514.

What is the sum of the sector IDs of the real rooms?
'''
from collections import Counter


def test1_run():
    rooms = [('aaaaa-bbb-z-y-x-123[abxyz]', True),
             ('a-b-c-d-e-f-g-h-987[abcde]', True),
             ('not-a-real-room-404[oarel]', True),
             ('totally-real-room-200[decoy]', False)]
    actual_out_final = 0
    for room, expected_out in rooms:
        actual_out, sector_id = run(room)
        assert expected_out == actual_out
        if actual_out:
            actual_out_final += sector_id
    expected_out_final = 1514
    assert expected_out_final == actual_out_final


def reverse_dict(dict_old):
    dict_new = {}
    for key, value in dict_old.items():
        if value not in dict_new:
            dict_new[value] = [key]
        else:
            dict_new[value].append(key)
    return dict_new


def run(room):
    sector_id = room.split('-')[-1]
    sector_id, check = sector_id.split('[')
    check = check[:-1]
    name = room.split('-')[:-1]
    name = ''.join(name)
    values = Counter(name)
    check_test = ''
    dict_new = reverse_dict(values)
    counts = sorted(dict_new, reverse=True)
    for count in counts:
        letters = dict_new[count]
        check_test += ''.join(sorted(letters))
    if check_test.split(check)[0] == '':
        return True, int(sector_id)
    else:
        return False, False


if __name__ == "__main__":
    out = 0
    with open('PuzzleInput.txt', 'r') as this_file:
        for room in this_file:
            room = room.replace('\n', '')
            test, sector_id = run(room)
            if test:
                out += sector_id
    print(out)
