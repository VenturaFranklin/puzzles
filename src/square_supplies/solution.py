'''
Created on Jun 2, 2015

@author: venturf2
'''
from itertools import chain, combinations

def test():
    for number in [24,160,9984]:
        print answer(number)

# @profile
def answer(totalcoins):
    '''With the zombie cure injections ready to go,
    it's time to start treating our zombified rabbit friends (known as zombits)
    at our makeshift zombit treatment center. You need to run out really fast to buy
    some gauze pads but you only have 30 seconds before you need to be back.

    Luckily, the corner store has unlimited gauze pads in squares of all sizes.
    Jackpot! The pricing is simple - a square gauze pad of size K x K costs exactly K * K coins.
    For example, a gauze pad of size 3x3 costs 9 coins.

    You're in a hurry and the cashier takes a long time to process each transaction.
    You decide the fastest way to get what you need is to buy as few gauze pads as possible,
    while spending all of your coins (you can always cut up the gauze later if you need to).
    Given that you have n coins, what's the fewest number of gauze pads you can buy?

    Write a method answer(n), which returns the smallest number
    of square gauze pads that can be bought with exactly n coins.

    n will be an integer, satisfying 1 <= n <= 10000.

    Languages
    =========

    To provide a Python solution, edit solution.py
    To provide a Java solution, edit solution.java

    Test cases
    ==========

    Inputs:
        (int) n = 24
    Output:
        (int) 3

    Inputs:
        (int) n = 160
    Output:
        (int) 2
    '''
    cost=0
    x = 1
    costs=[]
    while cost < totalcoins:
        x += 1
        cost = x**2
        if cost < totalcoins:
            costs.append(cost)
    for combo in powerset(costs):
#         print combo
        if sum(combo) == totalcoins:
            return len(combo)

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)*3
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

test()
