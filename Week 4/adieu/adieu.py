import inflect
users = []
p = inflect.engine()
while True:
    try:
        user = input("Name: ")
        users.append(user)
    except EOFError:
        print(f"Adieu, adieu, to {p.join(users)}")
        break
