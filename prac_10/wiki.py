"""
Small script that prompts user for page title or search phrase, then prints summary of page. Use simple loop that
continues doing so until user enters blank input
"""
import wikipedia


def wiki_summary():
    """Print summary of the page chosen by user"""
    page_title = input("Enter a page title: ")
    while not page_title == "":
        try:
            print(wikipedia.summary(page_title))
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)
        page_title = input("Enter a page title: ")
    print("Finish!")


def wiki():
    """"Print the title, summary and URL of the page the user chooses"""
    page = input("Enter page: ")
    while not page == "":
        try:
            print("Title:", wikipedia.page(page).title)
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)
        print("Summary: \n", wikipedia.summary(page))
        print("URL:", wikipedia.page(page).url)
        page = input("Enter page: ")
    print("Finish!")


# wiki_summary()
wiki()
