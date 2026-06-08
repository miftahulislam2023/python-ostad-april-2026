# Search in List
# Linear Search

words = [
    "interpreter",
    "variable",
    "function",
    "library",
    "syntax",
    "list",
    "dictionary",
    "module",
    "class",
    "decorator"
]

search_word = input("Enter a word to search: ")
word_found = False

for word in words:
    if word == search_word:
        word_found = True
        
if word_found:
    print(f"Found the word {search_word}")
else:
    print("Word not found")