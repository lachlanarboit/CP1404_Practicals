"""
CP1404 Practical
Clean up inconsistent song file names
"""

import os

def main():
    """Clean up inconsistent song file names"""

    # Change to desired directory
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):


        for filename in filenames:
            new_name = get_fixed_filename(filename)
            print("Renaming {} to {}".format(filename, new_name))

            full_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, new_name)
            os.rename(full_name, new_name)

def get_fixed_filename(filename):

main()