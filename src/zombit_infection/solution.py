'''
Created on Jun 1, 2015

@author: venturf2
'''
def answer(population, ycoord, xcoord, strength):
    '''
    #===========================================================================
    # Accessing a list in python in you want x,y position
    # you have to think reverse
    # population = [[6, 7, 2, 7, 6],
    #               [6, 3, 1, 4, 7]]
    # The first element is the ROW the second the COLUMN
    # population[0] = [6, 7, 2, 7, 6]
    # population[ROW][COLUMN]
    #     population[0][1] = 7
    #     population[1][0] = 6
    # So for this definition population[y][x]
    #===========================================================================

    population = A 2D non-empty array of positive integers.
    (The dimensions of the array are not necessarily equal.)
    Each cell represents one rabbit, and the value of the
    cell represents that rabbit's Resistance.
    All cells contain a rabbit.
    x = The X-Coordinate (column) of "Patient Z" in the population array.
    y = The Y-Coordinate (row) of "Patient Z" in the population array.
    strength = A constant integer value representing the Strength of the virus.

    Here are the rules of the simulation:
    First, the virus will attempt to infect Patient Z.
    Patient Z will only be infected if the infection's Strength
    equals or exceeds Patient Z's Resistance.
    From then on, any infected rabbits will attempt to infect any uninfected neighbors
    (cells that are directly - not diagonally - adjacent in the array).
    They will succeed in infecting any neighbors with a Resistance
    lower than or equal to the infection's Strength.
    This will continue until no further infections are possible
    (i.e., every uninfected rabbit adjacent to an infected rabbit has
    a Resistance greater than the infection's Strength.)

    You will write a function answer(population, x, y, strength),
    which outputs a copy of the input array representing the state
    of the population at the end of the simulation, in which any
    infected cells value has been replaced with -1.
    The Strength and Resistance values will be between 0 and 10000.
    The population grid will be at least 2x2 and no larger than 50x50.
    The x and y values will be valid indices in the population arrays,
    with numbering beginning from 0.

    Test cases
    ==========

    Inputs:
        (int) population = [[1, 2, 3],
                            [2, 3, 4],
                            [3, 2, 1]]
        (int) x = 0
        (int) y = 0
        (int) strength = 2
    Output:
        (int) [[-1, -1, 3],
                [-1, 3, 4],
                [3, 2, 1]]

    Inputs:
        (int) population = [[6, 7, 2, 7, 6],
                            [6, 3, 1, 4, 7],
                            [0, 2, 4, 1, 10],
                            [8, 1, 1, 4, 9],
                            [8, 7, 4, 9, 9]]
        (int) x = 2
        (int) y = 1
        (int) strength = 5
    Output:
        (int) [[6, 7, -1, 7, 6],
               [6, -1, -1, -1, 7],
               [-1, -1, -1, -1, 10],
               [8, -1, -1, -1, 9],
               [8, 7, -1, 9, 9]]

    '''
    testing = []
    tested = []
    testing.append((xcoord, ycoord))
    xshape, yshape = len(population)-1, len(population[0])-1
    while len(testing):
        coords = testing.pop()
        xcoord, ycoord = coords
        resistance = population[xcoord][ycoord]
        tested.append(coords)
        if resistance <= strength:
            population[xcoord][ycoord] = -1
            for neighbor in neighbor_list(xcoord, ycoord, xshape, yshape):
                if neighbor not in tested and neighbor not in testing:
                    testing.append(neighbor)
    return population

def neighbor_list(xcoord, ycoord, xshape, yshape):
    '''from x,y tuple return list of neighbor coordinates
    not diagonally and within the shape of array'''
    newcoordlist = [(xcoord+i, ycoord+j) for i in (-1, 0, 1)
                    for j in (-1, 0, 1) if i == 0 or j == 0]
    newlist = newcoordlist[:]
    for coord in newlist:
        xcoord, ycoord = coord
        if xcoord < 0 or ycoord < 0:
            newcoordlist.pop(newcoordlist.index(coord))
        elif xcoord > xshape or ycoord > yshape:
            newcoordlist.pop(newcoordlist.index(coord))
    return newcoordlist
