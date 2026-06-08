words = [
    "interpreter",
    "variable",
    "function",
    "library",
    "syntax",
    "list",
    "syntax",
    "dictionary",
    "syntax",
    "module",
    "class",
    "module",
    "decorator"
]

search_word = input("Enter a word to search: ")
word_found = False
frequency = 0

i = 0

while i < len(words):
    if words[i] == search_word:
        if word_found != True:
            word_found = True
            frequency += 1
        else:
            frequency += 1
    i += 1

        
if word_found:
    print(f"Found the word {search_word} {frequency} times")
else:
    print("Word not found")