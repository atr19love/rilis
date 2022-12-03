import httpx,json,time

v="0.1"
print(f"This version is {v}")
print("Untuk sementara ketik python backup.py")
g=input("")
if g!="g":
    exit()
servers=httpx.get("https://raw.githubusercontent.com/atr19love/rilis/master/versi.txt").text
if servers!=v:
    newsc=httpx.get("https://raw.githubusercontent.com/atr19love/rilis/master/topixsb.py").text
    with open("topixsb.py", "w") as file1:
        file1.write(newsc)
    print(f"Updateing TopixSB Termux Tools {servers} Version")