"""
Password checker program which validates password
"""

def main():
    password = input("Enter a password: ")
    get_password(password)


def get_password(password):
    while True:
        if len(password) < 8:
            print("Make sure your password is at least 8 letters")
        else:
            print("Your password seems fine")
            print(password.replace(password, '*' * len(password)))
            break

main()
