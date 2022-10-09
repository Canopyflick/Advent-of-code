def trees_check(slope_x, slope_y):
    # Again set the pointer to the beginning
    file.seek(0, 0)

    terrain = []

    # Parse all strings to integers and put into list
    for every_line in file:
        # remove all newline characters at beginning and end of string
        every_line = every_line.strip()
        terrain.append(every_line)

    required_width = slope_x * (len(terrain) / slope_y)

    first_row = terrain[0]
    width = len(first_row)
    depth = len(terrain)

    number_of_expansions = int(required_width / width) + 1

    # map(function, array)
    # https://www.geeksforgeeks.org/python-map-function/
    terrain = list(map(lambda line_in_terrain: line_in_terrain * number_of_expansions, terrain))

    required_width = slope_x * (len(terrain) / slope_y)

    x = 0
    y = 0
    trees = 0

    while y < depth:
        if terrain[y][x] == '#':
            trees = trees + 1
            # trees += 1
            # trees -= 1
        x += slope_x
        y += slope_y

    # for loop in C:
    # for (y = 0; y < depth; y += slope_y) {
    #   for (x = 0; x < width; x += slope_x) {

    print("Trees on route for slope Right", slope_x, "Down,", slope_y, ":", trees)
    return trees


if __name__ == '__main__':
    file = open("real terrain.txt", "r")

    answer = trees_check(1, 1) * trees_check(3, 1) * trees_check(5, 1) * trees_check(7, 1) * trees_check(1, 2)
    print("All trees multiplied:\n", answer)