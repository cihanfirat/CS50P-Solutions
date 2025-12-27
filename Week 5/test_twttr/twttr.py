
def main():
    user_input = input("Input: ")
    new_word=shorten(user_input)
    print("Output: " + new_word)

def shorten(message):
    word_without_vowels=""
    for letter in message:
        if not letter.lower() in ["a","e","i","o","u"]:
            word_without_vowels += letter

    return word_without_vowels

if __name__ == "__main__":
    main()
