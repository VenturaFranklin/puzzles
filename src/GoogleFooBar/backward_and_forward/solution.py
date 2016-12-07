'''venturafranklin submission for the backward_and_forward challenge
'''

def answer(num):
    '''Returns the smallest positive integer base b, at least 2,
    in which the integer n is a palindrome.
    The input n will satisfy "0 <= n <= 1000.'''
    for base in xrange(2, 36):
        test_string = baseconvert(num, base)
        if test_string == '':
            return base
        if is_palindrome(test_string):
            return base

def is_palindrome(test_string):
    '''Returns True when input test_string is a palindrome'''
    test_list = list(test_string)
    test = [x for i, x in enumerate(test_list)
            if x != test_list[-i-1]]
    return len(test) == 0

def baseconvert(num, base):
    """convert positive decimal integer num to equivalent
    in another base (2-36)
    http://code.activestate.com/recipes/65212/"""

    digits = "0123456789abcdefghijklmnopqrstuvwxyz"

    try:
        num = int(num)
        base = int(base)
    except ValueError:
        return ""

    if num < 0 or base < 2 or base > 36:
        return ""

    num_string = ""
    while 1:
        remainder = num % base
        num_string = digits[remainder] + num_string
        num = num / base
        if num == 0:
            break

    return num_string
