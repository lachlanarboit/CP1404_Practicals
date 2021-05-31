"""
CP1404
State names
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales",
                "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria",
                "TAS": "Tasmania"}

state = input("Enter state abbreviation: ").upper()
while state != "":
    if state in CODE_TO_NAME:
        print(state, "is", CODE_TO_NAME[state])
    else:
        print("Invalid state abbreviation")
    state = input("Enter state abbreviation: ").upper()