import sys
from pyfiglet import Figlet
figlet = Figlet()

if(len(sys.argv)!=3 and len(sys.argv)!=1):
        sys.exit("Invalid usage")

elif(len(sys.argv)==1):
        user = input("Input: ")
        print(figlet.renderText(user))

elif(len(sys.argv)==3 and (sys.argv[1]=="-f" or sys.argv[1]== "--font") and (sys.argv[2] in figlet.getFonts())):
        figlet.setFont(font=sys.argv[2])
        user = input("Input: ")
        print(figlet.renderText(user))

elif(len(sys.argv)==3 and (sys.argv[1]!="-f" or sys.argv[1])!= "--font"):
        sys.exit("Invalid usage")


