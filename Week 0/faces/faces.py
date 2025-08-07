def convert(inputText):
    newMsg1 = inputText.replace(":)","🙂")
    newMsg2 = newMsg1.replace(":(","🙁")
    return newMsg2

def main():
    inputText=input()
    result = convert(inputText)
    print(result)

main()
