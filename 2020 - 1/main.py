# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Iterate of elements in list of numbers
# Add every element together to get the sum

# DRY principle:
# Don't repeat yourself

def part_one(list_of_numbers):
    # Iterate over all combinations
    for x in list_of_numbers:
        for y in list_of_numbers:
            # Iteratie 1: y = 1597
            # ...

            # Difference between =, == :
            # a == b | Check if 'a' is equal to 'b'
            # a = b | Set 'a' to 'b'
            if x + y == 2020:
                print(x, y, "\n", x * y)


def part_two(list_of_numbers):
    for x in list_of_numbers:
        for y in list_of_numbers:
            for z in list_of_numbers:
                if x + y + z == 2020:
                    print(x, y, z, "\n", x * y * z)


def sum(list_of_numbers):
    # Sum is initially 0
    sum = 0
    for x in list_of_numbers:
        # Add the new value to the sum
        sum = sum + x
    return sum


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Ben\nHallo')

    # Opening a file in read-only mode ("r")
    file = open("nummers.txt", "r")

    # Define empty list of values
    values = []

    # Parse all strings to integers and put into list
    for x in file:
        values.append(int(x))

    print(values)

    part_one(values)
    print("hierna komt ie hoor:")
    part_two(values)

    print(sum([5, 4, 3, 2, 1]))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
