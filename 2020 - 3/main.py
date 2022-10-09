def expand_terrain(line):
    return line * number_of_expansions


if __name__ == '__main__':

    file = open("real terrain.txt", "r")

    slope_x = 3
    slope_y = 1

    terrain = []

    # Parse all strings to integers and put into list
    for every_line in file:
        # remove all newline characters at beginning and end of string
        every_line = every_line.strip()
        terrain.append(every_line)
    print("Terrain in een list:\n", terrain)

    required_width = slope_x * (len(terrain) / slope_y)
    print("Required width:\n", required_width)

    first_row = terrain[0]
    width = len(first_row)
    depth = len(terrain)

    number_of_expansions = int(required_width / width) + 1
    print("Number of expansions:\n", number_of_expansions)

    # 1. Remove newline characters from rows ✔
    # 2. expand universe with new_terrain ✔

    # Again set the pointer to the beginning
    # file.seek(0, 0)

    # map(function, array)
    # https://www.geeksforgeeks.org/python-map-function/
    terrain = list(map(lambda line_in_terrain: line_in_terrain * number_of_expansions, terrain))
    print("Terrain =", terrain)

    # universe = []

    # for every_line in file:
    #     # remove all newline characters at beginning and end of string
    #     every_line = every_line.strip()
    #     universe.append(every_line * number_of_expansions)
    #
    # print("\nUniverse in een list:\n", universe)

    # Loop over every row in terrain

    # where's dem trees?
    # Starting position
    x = 0
    y = 0

    # 0= [0, 0]
    # 1= [3, 1]
    # 2= [6, 2]
    # 3= [9, 3]
    # 4= [12, 4]
    trees = 0

    while y < depth:
        print("y =\n", y, len(terrain))
        print("x =\n", x, len(terrain[0]))
        if terrain[y][x] == '#':
            trees = trees + 1
            # trees += 1
            # trees -= 1
        x += slope_x
        y += slope_y

    # for loop in C:
    # for (y = 0; y < depth; y += slope_y) {
    #   for (x = 0; x < width; x += slope_x) {

    print("trees:\n", trees)

    # for line in terrain:
    #     # line = terrain[y]
    #     # character = line[x]
    #     if terrain[y][x] == '#':
    #         trees = trees + 1
    #         # trees += 1
    #         # trees -= 1
    #         x += slope_x #
    #         y += slope_y
    #     for y in terrain:
