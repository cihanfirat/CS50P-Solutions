import random

while True:
    try:
        level = input("Level: ")
        level=int(level)
        answer = random.randint(1,level)

    except (TypeError,ValueError):
        pass

    else:
        while True:
            try:
                guess = (input("Guess: "))
                guess = int(guess)

            except (TypeError,ValueError):
                pass

            else:
                if guess < 0:
                    pass
                elif guess < answer:
                    print("Too small!")
                    pass
                elif guess > answer:
                    print("Too large!")
                    pass
                else:
                    print("Just Right!")
                    break
        break
