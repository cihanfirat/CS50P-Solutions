menu={}
while True:
    try:
        user = input("")
    except EOFError:
        break
    else:
        if user not in menu:
            menu[user] = 1

        else:
            menu[user]+=1

items = []
for key,value in menu.items():
    items.append((value,key.upper()))

items.sort(key=lambda item : item[1])

for count,item in items:
    print(count,item)
