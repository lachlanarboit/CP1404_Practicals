"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""



def main():
    score_classifier()


def score_classifier():
    score = float(input("Enter score: "))
    if score < 0:
        print("Invalid score")
    else:
        if score > 100:
            print("Invalid score")
        if score > 90:
            print("Excellent")
        if score >= 50:
            print("Passable")
        if score < 50:
            print("Bad")
main()