months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ").strip()
    try:
        month,day,year = date.split("/")
        if(int(month)>=1 and int(month)<=12) and (int(day)>=1 and int(day)<=31):
            break

    except:
        try:
            month,day,year = date.split(" ")

            if "," not in day:
                continue
            day = day.replace(",","")

            if month in months:
                month = months.index(month)+1


            if(int(month)>=1 and int(month)<=12) and (int(day)>=1 and int(day)<=31):
                break
        except:
            print()
            pass

print(f"{year}-{int(month):02}-{int(day):02}")
