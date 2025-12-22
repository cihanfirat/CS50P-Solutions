import random


def main():
    score=0
    level = get_level()
    for _ in range(10):
        x=generate_integer(level)
        y=generate_integer(level)
        result = x+y
        attemps = 0

        while attemps<3:
            try:
                answer=int(input(f"{x} + {y} = "))
                if answer == result:
                    score+=1
                    break
                else:
                    print("EEE")
            except ValueError:
                    print("EEE")
            attemps +=1

        if attemps == 3:
            print(f"{x} + {y} = {result}")
    print(f"Score: {score}")

def get_level():
    while True:
        level = input("Level: ")
        if level in ["1","2","3"]:
            return int(level)



def generate_integer(level):
    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    elif level == 3:
        return random.randint(100,999)


if __name__ == "__main__":
    main()
