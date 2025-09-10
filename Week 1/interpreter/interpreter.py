userInput = input("Expression: ")
x,y,z = userInput.split(" ")

if y == "+":
    print(float(int(x)+int(z)))
elif y == "-":
    print(float(int(x)-int(z)))
elif y == "*":
    print(float(int(x)*int(z)))
else:
    print(float(int(x)/int(z)))
