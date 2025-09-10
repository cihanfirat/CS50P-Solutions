user = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
user = user.strip()
if user.lower() in ["42","forty-two","forty two","Forty Two"]:
    print("Yes")
else:
    print("No")
