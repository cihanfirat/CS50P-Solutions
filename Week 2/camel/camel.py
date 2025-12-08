userInput = input("camelCase: ")

for letter in userInput:
    if letter.isupper():
        letter = letter.lower()
        letter = "_"+letter
    print(letter,end="")
