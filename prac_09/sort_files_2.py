"""
CP1404 Practical
Sort files based on extension and user categorisation
"""
import os


def main():
    """Move files into where user wants to share them based on extension"""
    # This directory will allow us to map extensions to the destination folder names
    extension_to_category = {}
    os.chdir("FilesToSort")
    for filename in os.chdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        extension = filename('.')[-1]
        if extension not in extension_to_category:
            category = input("What category would you like to sort {} files into? ",format(extension))
            # Now map new extension to folder name
            extension_to_category[extension] = category
            try:
                os.mkdir(category)
            except FileExistsError:
                pass

        os.rename(filename, "{}/{}".format(extension_to_category[extension], filename))

main()