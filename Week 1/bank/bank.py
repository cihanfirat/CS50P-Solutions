userInput = input("Greeting: ")

if "hello" in userInput.lower():
    print("$0")
elif userInput.lower().startswith("h"):
    print("$20")
else:
    print("$100")
