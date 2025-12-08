def main():
    user_input = input("Plate: ")

    if (is_valid(user_input) and
         max_characters(user_input) and
           middle_number(user_input) and
             no_others(user_input)):
        print("Valid")
    else:
        print("Invalid")


def is_valid(user_input):
    if user_input[:2].isdigit():
        return False
    return True

def max_characters(user_input):
    if len(user_input)<2 or len(user_input)>6:
        return False
    return True

def middle_number(user_input):

    seen_digit = False

    for i in range(len(user_input)):
        if user_input[i].isdigit():
            if user_input[i] == "0" and not seen_digit:
                return False  # First number cannot be '0'
            seen_digit = True
        elif seen_digit:
            return False  # If a letter appears after a number, it's invalid

    return True

def no_others(user_input):
    for letter in user_input:
        if letter in ["!",",",".",":",";","?"," "]:
            return False
    return True


main()
