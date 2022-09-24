# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Ben\nHallo')
    file = open("nummers.txt", "r")

    values = []
    # Array heeft fixed size
    # List is dynamisch

    # Parse all strings to integers and put into list
    for x in file:
        values.append(int(x))

    # Iterate over all combinations
    for x in values:
        for y in values:
            # Difference between =, == :
            # a == b | Check if 'a' is equal to 'b'
            # a = b | Set 'a' to 'b'
            if x + y == 2020:
                print(x, y, x*y)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
