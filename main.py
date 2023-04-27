

def func(text, num=15):
    return text*num


def func2(string, sep = ' '):
    return string.split(sep)


def func3(string, additional='b'):
    return string + ' ' + len(string)*additional


if __name__ == '__main__':
    while True:
        print('-'*15)
        print('-'*3+'Beginning'+'-'*3)
        print('-' * 15)
        string1 = func(input("Enter a letter: "), int(input("Enter a number: ")))

        string2 = func3(string1)
        print(string2)

        string3 = func2(string2)
        print(string3)
        print('-'*15)
        print('-'*6+'End'+'-'*6)
        print('-' * 15)
        if input('Continue? ') not in ['y', 'Y', 'yes', 'Yes', 'YES']:
            break
