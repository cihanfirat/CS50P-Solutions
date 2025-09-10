def main():
    userInput = input("What time is it? ")
    res = convert(userInput)

    if res >= 7 and res <=8:
        print("breakfast time")
    elif res >= 12 and res <=13:
        print("lunch time")
    elif res >= 18 and res <=19:
        print("dinner time")
    else:
        return

def convert(time):
    hour,minute = time.split(":")
    hour = float(hour)
    minute = float(int(minute)/60)
    return hour+minute


if __name__ == "__main__":
    main()
