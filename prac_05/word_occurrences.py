"""
CP1404 Practical
Word Occurrences
"""

word_to_count = {}
text = input("Text: ")
words = text.split()
for word in words:
    frequency = word_to_count.get(word, 0)
    word_to_count[word] = frequency + 1

# Print words and their frequencies in alphabetical order
words = list(word_to_count.keys())
words.sort()

max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, word_to_count[word]))