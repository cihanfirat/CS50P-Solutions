while True:
    try:
        x,y = (input("Fraction: ").split('/'))
        result = (int(x)/int(y))*100

        if not x.isdigit() or not y.isdigit() or int(x) > int(y) or int(y) == 0:
            pass
        else:
            if int(result)>=99:
                print("F")
                break
            elif int(result)<=1:
                print("E")
                break
            else:
                print(f"{round((result))}%")
                break

    except ValueError:
        pass
    except ZeroDivisionError:
        pass
    """
    if x==y:
        print("F")
        break
    if (int(x)/int(y))==0:
        print("E")
        break
    else:
        print(f"{result}%")
        break"""


