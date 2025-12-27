def main():
    userInput = input("Greeting: ")
    print(f"${value(userInput)}")


def value(greeting):

    if "hello" in greeting.lower():
        return 0
    elif greeting.lower().startswith("h"):
        return 20
    else:
        return 100



if __name__ == "__main__":
    main()
