'''
Created on May 31, 2015

@author: venturafranklin
'''

def answer(intervals):
    '''Takes a list of pairs [start, end] and returns the
    total amount of time that Dolly the Zombit was monitored
    by at least one minion. Each [start, end] pair represents
    the times when a minion started and finished monitoring the zombit.
    All values will be positive integers no greater than 2^30 - 1.
    You will always have end > start for each interval
    Test cases
    ==========

    Inputs:
        (int) intervals = [[1, 3], [3, 6]]
    Output:
        (int) 5

    Inputs:
        (int) intervals = [[10, 14], [4, 18], [19, 20], [19, 20], [13, 20]]
    Output:
        (int) 16
    '''
    totaltime = 0
    _, lastmax = (0, 0)
    while len(intervals) > 0:
        value = min(intervals, key=lambda t: t[0])
        value = intervals.pop(intervals.index(value))
        thismin, thismax = value
        if thismin > lastmax:
            totaltime += thismax-thismin
            _, lastmax = value
        else:
            if thismax > lastmax:
                totaltime += thismax-lastmax
                _, lastmax = value
    return totaltime
