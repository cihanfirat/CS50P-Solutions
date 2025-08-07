c = 300000000
def main():
    kg = int(input("m: "))
    calculateE(kg)

def calculateE(kg):
    print("E: " + str(kg*(c*c)))

main()
