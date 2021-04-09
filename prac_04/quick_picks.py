"""
CP1404 Practical - Quickpicks
"""

import random

numbers_per_line = 6
minimum = 1
maximum = 45


def main():
    number_quickpicks = int(input("How many quick picks? "))
    for i in range(number_quickpicks):
        quickpick = []
        for j in range(numbers_per_line):
            number = random.randint(minimum, maximum)
            while number in quickpick:
                number = random.randint(minimum, maximum)
            quickpick.append(number)
        print(" ".join("{:2}".format(number) for number in quickpick))

main()