################################################################################################
#                SPLIT AND INTERACTIVELY PAGE A STRING OR FILE OF TEXT                         #
################################################################################################
import sys
import os


def more(text, numlines=15):
    # Use a breakpoint in the code line below to debug your script.
    lines = str.split(text, '\n')
    while lines:
        chunk = lines[:numlines]
        lines = lines[numlines:]
        for line in chunk:
            print(line)
        if lines and input('More?') not in ['y', 'Y']:
            break


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    more(open(sys.path).read(), 10)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
