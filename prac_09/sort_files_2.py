"""
CP1404 Practical
Sort files based on extension and user categorisation
"""
import os


def main():
    """Move files into where user wants to share them based on extension"""
    extension_to_category = {}
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        extension = filename.split('.')[-1]
        if extension not in extension_to_category:
            category = input("What category would you like to sort {} files into? ",format(extension))
            # Now map new extension to folder name
            extension_to_category[extension] = category
            try:
                os.mkdir(category)
            except FileExistsError:
                pass

        print("{}/{}".format(extension_to_category[extension], filename))
        os.rename(filename, "{}/{}".format(extension_to_category[extension], filename))

main()
