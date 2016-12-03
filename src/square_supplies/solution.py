'''
Created on Jun 2, 2015

@author: venturf2
'''
from itertools import chain, combinations

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
    cost = 0
    value = 1
    costs = []
    while cost <= totalcoins:
        value += 1
        cost = value**2
        if cost <= totalcoins:
            costs.append(cost)
#     for combo in powerset(costs):
# #         print combo
#         if sum(combo) == totalcoins:
#             return len(combo)
    combos=powerset(costs)
    combosums=map(sum_and_count,combos)
    return combosums
#     return min([item for item in combosums if item[0] == totalcoins])[1]

def sum_and_count(x):
    return sum(x),len(x)
    combos = powerset(costs)
    for combo in combos:
        if sum(combo) == totalcoins:
            return len(combo)

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)*3 #Time limit exceeded
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
    mylist = list(iterable)
    return chain.from_iterable(combinations_with_replacement(mylist, r=r)
                               for r in range(len(mylist)+1))
    mylist = list(iterable)
    return chain.from_iterable(combinations_with_replacement(mylist, r=r)
                               for r in range(len(mylist)+1))
