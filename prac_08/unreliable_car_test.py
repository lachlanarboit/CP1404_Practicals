"""
CP1404 Practical
Unreliable car class tests
"""

from prac_08.unreliable_car import UnreliableCar


def main():
    """Testing unreliable cars"""

    good_car = UnreliableCar("Usually reliable", 100, 85)
    bad_car = ("Not reliable", 100, 12)

    # Attempt to simulate driving cars, distance driven is random
    for i in range(1, 12):
        print("Attempting to drive {}km".format(i))
        print("{:12} drove {:2}km".format(good_car.name, good_car.drive(i)))
        print("{:12} drove {:2}km".format(bad_car.name, bad_car.drive(i)))

    print(good_car)
    print(bad_car)


main()
