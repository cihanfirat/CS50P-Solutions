fileName = input("File name: ")
fileName = fileName.lower()

if ".gif" in fileName:
    print("image/gif")

elif ".jpg" in fileName:
    print("image/jpeg")

elif ".jpeg" in fileName:
    print("image/jpeg")

elif ".png" in fileName:
    print("image/png")

elif ".pdf" in fileName:
    print("application/pdf")

elif ".txt" in fileName:
    print("text/plain")

elif ".zip" in fileName:
    print("application/zip")

else:
    print("application/octet-stream")
