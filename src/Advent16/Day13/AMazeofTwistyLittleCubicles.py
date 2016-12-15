'''
Created on Dec 13, 2016

@author: venturf2

--- Day 13: A Maze of Twisty Little Cubicles ---

You arrive at the first floor of this new building to discover a much less
welcoming environment than the shiny atrium of the last one.
Instead, you are in a maze of twisty little cubicles, all alike.

Every location in this area is addressed by a pair of non-negative integers
(x,y). Each such coordinate is either a wall or an open space.
You can't move diagonally. The cube maze starts at 0,0 and seems to extend
infinitely toward positive x and y; negative values are invalid,
as they represent a location outside the building.
You are in a small waiting area at 1,1.

While it seems chaotic, a nearby morale-boosting poster explains,
the layout is actually quite logical.
You can determine whether a given x,y coordinate will be a wall or an open
space using a simple system:

Find x*x + 3*x + 2*x*y + y + y*y.
Add the office designer's favorite number (your puzzle input).
Find the binary representation of that sum;
count the number of bits that are 1.
If the number of bits that are 1 is even, it's an open space.
If the number of bits that are 1 is odd, it's a wall.
For example, if the office designer's favorite number were 10,
drawing walls as # and open spaces as .,
the corner of the building containing 0,0 would look like this:

  0123456789
0 .#.####.##
1 ..#..#...#
2 #....##...
3 ###.#.###.
4 .##..#..#.
5 ..##....#.
6 #...##.###
Now, suppose you wanted to reach 7,4.
The shortest route you could take is marked as O:

  0123456789
0 .#.####.##
1 .O#..#...#
2 #OOO.##...
3 ###O#.###.
4 .##OO#OO#.
5 ..##OOO.#.
6 #...##.###
Thus, reaching 7,4 would take a minimum of 11 steps
(starting from your current location, 1,1).

What is the fewest number of steps required for you to reach 31,39?

Your puzzle input is 1352.
'''
from heapq import heappop, heappush


def test_1():
    destination = (7, 4)
    actual_out = run(destination)
    actual_out = len(actual_out.split('),'))
    expected_out = 11
    assert actual_out == expected_out


def check_open(coord):
    x, y = coord
    out = x*x + 3*x + 2*x*y + y + y*y
    out += INPUT
    out = "{0:b}".format(out)
    return not out.count('1') % 2


def find_neighbors(coord):
    ''' (1, 1)
    x-1, x+1, y-1, y+1
    '''
    x, y = coord
    neighbors_test = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    neighbors = []
    for neighbor in neighbors_test:
        if check_open(coord):
            neighbors.append(neighbor)
    return neighbors


def run(destination):
    start, goal = (1, 1), destination
    pr_queue = []
    heappush(pr_queue, (0,
                        0,
                        "",
                        start))
    visited = set()
    while pr_queue:
        _, cost, path, current = heappop(pr_queue)
        if current == goal:
            return path
        if current in visited:
            continue
        visited.add(current)
        neighbors = find_neighbors(current)
        for neighbor in neighbors:
            heappush(pr_queue, (cost + 1,
                                cost + 1,
                                path + ', ' + str(neighbor),
                                neighbor))
    return "NO WAY!"

if __name__ == "__main__":
#     INPUT_TEST = 10
#     test_1()
    INPUT = 1352
    destination = (31, 39)
    out = run(destination)
    print len(out.split('),'))
