from parse import parse


# min-max letter: password\n
def valid_passwords(corrupted_database):
    entries = []

    # Parse all strings to integers and put into list
    for every_line in corrupted_database:
        entries.append(every_line)


    # parse("It's {}, I love it!", "It's spam, I love it!")
    goeden = 0
    for entry in entries:
        # == (Equality)
        # != (Not equal)
        # < (Less than)
        # > (Greater than)
        # <= (Less than or equal)
        # >= (Greater than or equal)
        minimum, maximum, letter, password = parse("{}-{} {}: {}\n", entry)
        # 1. How often does 'letter' appear in 'password'

        if int(minimum) <= password.count(letter) <= int(maximum):
            print(entry, 'valid\n')
            goeden = goeden + 1
        else:
            print(entry, 'invalid\n')

    return goeden


def valid_passwords_2(corrupted_database):
    entries = []

    # Parse all strings to integers and put into list
    for every_line in corrupted_database:
        entries.append(every_line)

    goeden = 0

    for entry in entries:
        # == (Equality)
        # != (Not equal)
        # < (Less than)
        # > (Greater than)
        # <= (Less than or equal)
        # >= (Greater than or equal)
        position_1, position_2, letter, password = parse("{}-{} {}: {}\n", entry)
        #s = 'python is fun'
        #c = 'n'

        position_1_zero_based = int(position_1) - 1
        position_2_zero_based = int(position_2) - 1

        entry_positions = ([pos for pos, char in enumerate(password) if char == letter])
        if (entry_positions.count(position_1_zero_based) or entry_positions.count(position_2_zero_based))\
                and not (entry_positions.count(position_1_zero_based) and entry_positions.count(position_2_zero_based)):
            # Correct
            goeden = goeden + 1

    return goeden

#    password
#    positie = password.find(letter+1)
#    return goeden


def test():
    example_file = open("example requirements.txt", "r")
    if valid_passwords(example_file) == 2:
        print("het klopt")
    else:
        print("klopt helemaal nie")


def test_2():
    example_file = open("example requirements.txt", "r")
    if valid_passwords_2(example_file) == 1:
        print("het klopt")
    else:
        print("klopt helemaal nie")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Opening a file in read-only mode ("r")
    file = open("password requirements.txt", "r")
    print('keepvogeeel, keepvogeèeeeel..:', valid_passwords_2(file))

    print("Test:\n")
    test_2()


# s = 'python is fun'
# c = 'n'
# print([pos for pos, char in enumerate(s) if char == c])





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
