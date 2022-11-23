import httpx

servers=httpx.get("https://raw.githubusercontent.com/atr19love/rilis/master/versi.txt").text
newsc=httpx.get("https://raw.githubusercontent.com/atr19love/rilis/master/topixsb.py").text
with open("topixsb.py", "w") as file1:
    file1.write(newsc)
print(f"Updateing TopixSB Termux Tools {servers} Version")
exit()