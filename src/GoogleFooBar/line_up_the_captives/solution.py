'''
Created on Jun 7, 2015

@author: venturafranklin
'''
def answer(fromwest, fromeast, num):
    '''
    To help plan this caper you need to calculate how many ways
    the rabbits can be lined up such that a viewer on one end sees
    x rabbits, and a viewer on the other end sees y rabbits, because
    some taller rabbits block the view of the shorter ones.

    For example, if the rabbits were arranged in line with heights
    30 cm, 10 cm, 50 cm, 40 cm, and then 20 cm, a guard looking from
    the left side would see 2 rabbits (30 and 50 cm) while a guard looking from
    the right side would see 3 rabbits (20, 40 and 50 cm). 

    Write a method answer(x,y,n) which returns the number of possible
    ways to arrange n rabbits of unique heights along an east to west
    line, so that only x are visible from the west, and only y are visible
    from the east. The return value must be a string representing the number in base 10.

    If there is no possible arrangement, return "0".

    The number of rabbits (n) will be as small as 3 or as large as 40
    The viewable rabbits from either side (x and y) will be as small as
    1 and as large as the total number of rabbits (n).

    Test cases
    ==========

    Inputs:
        (int) x = 2
        (int) y = 2
        (int) n = 3
    Output:
        (string) "2"

    Inputs:
        (int) x = 1
        (int) y = 2
        (int) n = 6
    Output:
        (string) "24"
    '''
    pass
