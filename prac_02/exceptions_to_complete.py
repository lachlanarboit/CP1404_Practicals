"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

finished = False
result = 0
while not finished:
    try:
        value = int(input("Enter an integer: "))
        if value != 0:
            print("Not an integer!")
        else break:
    except:  # TODO - add something after except
        print("Please enter a valid integer.")
print("Valid result is:", result)