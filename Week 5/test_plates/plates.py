def main():
    user_input = input("Plate: ")

    if is_valid(user_input):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    return (
        starts_with_letters(s) and
        valid_length(s) and
        numbers_in_middle(s) and
        no_special_chars(s)
    )

def starts_with_letters(s):
    return not s[:2].isdigit()

def valid_length(s):
    return 2 <= len(s) <= 6

def numbers_in_middle(s):
    seen_digit = False

    for i in range(len(s)):
        if s[i].isdigit():
            if s[i] == "0" and not seen_digit:
                return False  # İlk sayı '0' olamaz
            seen_digit = True
        elif seen_digit:
            return False  # Bir sayıdan sonra harf gelirse geçersiz olur
    return True

def no_special_chars(s):
    return all(c not in "!,.?:; " for c in s)

if __name__ == "__main__":
    main()
