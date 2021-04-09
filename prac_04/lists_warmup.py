"""
CP1404 Practical - Lists Warmup
"""

numbers = [3, 1, 4, 1, 5, 9, 2]
print(numbers)

"""
Values of expressions as requested for practical task
numbers[0] >> 3
numbers[-1] >> 2
numbers[3] >> 1
numbers[:-1] >> [3, 1, 4, 5, 9]
numbers[3:4] >> [1]
5 in numbers >> True
7 in numbers >> False
"3" in numbers >> 3
numbers + [6, 5, 3] >> error
"""

# PYTHON EXPRESSIONS TO CONVEY THE FOLLOWING
# Check if 9 is an element of numbers
if 9 in numbers:
    print("9 is an element of numbers")

# Change the first element of numbers to "ten"
numbers[0] = "ten"

# Change the last element of numbers to 1
numbers[-1] = 1

print("Format of numbers with last first and last element changed: {}".format(numbers))

# Get all the elements from numbers except the first two
print("All elements from numbers except the first two: {}".format(numbers[2:]))
