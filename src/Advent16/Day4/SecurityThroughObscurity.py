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

--- Part Two ---

With all the decoy data out of the way,
it's time to decrypt this list and get moving.

The room names are encrypted by a state-of-the-art shift cipher,
which is nearly unbreakable without the right software.
However, the information kiosk designers at Easter Bunny HQ were not expecting
to deal with a master cryptographer like yourself.

To decrypt a room name, rotate each letter forward through the alphabet a
number of times equal to the room's sector ID.
A becomes B, B becomes C, Z becomes A, and so on.
Dashes become spaces.

For example, the real name for qzmt-zixmtkozy-ivhz-343 is very encrypted name.

What is the sector ID of the room where North Pole objects are stored?
'''
from collections import Counter
import string


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


def test_shift():
    name = 'qzmt zixmtkozy ivhz'
    shift = 343
    actual_out = shift_name(name, shift)
    expected_out = 'very encrypted name'
    assert expected_out == actual_out


def reverse_dict(dict_old):
    dict_new = {}
    for key, value in dict_old.items():
        if value not in dict_new:
            dict_new[value] = [key]
        else:
            dict_new[value].append(key)
    return dict_new


def shift_name(name, shift):
    letters = list(string.ascii_lowercase)
    new_name = ''
    for letter in name:
        if letter == ' ':
            new_letter = letter
        else:
            indx = letters.index(letter)
            new_letter = letters[(shift + indx) % len(letters)]
        new_name += new_letter
    return new_name


def run(room):
    sector_id = room.split('-')[-1]
    sector_id, check = sector_id.split('[')
    check = check[:-1]
    name_raw = room.split('-')[:-1]
    name = ''.join(name_raw)
    name_raw = ' '.join(name_raw)
    values = Counter(name)
    check_test = ''
    dict_new = reverse_dict(values)
    counts = sorted(dict_new, reverse=True)
    for count in counts:
        letters = dict_new[count]
        check_test += ''.join(sorted(letters))
    if check_test.split(check)[0] == '':
        return True, int(sector_id), name_raw
    else:
        return False, False, False


if __name__ == "__main__":
    test_shift()
    with open('PuzzleInput.txt', 'r') as this_file:
        for room in this_file:
            room = room.replace('\n', '')
            test, sector_id, name_raw = run(room)
            if test:
                new_name = shift_name(name_raw, sector_id)
                if 'north' in new_name:
                    print(new_name, sector_id)
