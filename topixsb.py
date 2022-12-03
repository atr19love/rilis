import os,httpx
import json
import random
import time
import sys
import NamaBerwarna
import displaywarna
import cpm as cpm
from colr import color

v="0.5"
persi=httpx.get("https://raw.githubusercontent.com/atr19love/rilis/master/versi.txt").text
newsc=httpx.get("https://raw.githubusercontent.com/atr19love/rilis/master/topixsb.py").text
if v!=persi:
    with open("topixsb.py", "w") as file1:
        file1.write(newsc)
    print(f"Updateing TopixSB Termux Tools {persi} Version")


def usetoken(code):
    head={"type":"topixsb"}
    param={"code":code}
    servers=json.loads(httpx.post("https://topixsb.dev/vipcode",params=param,headers=head).text)
    print(servers[1])
    return(servers)

codex=input("code akses :")
codetok=usetoken(codex)

def c(colr, tex):
    try:
        w = {
            "RED": [255, 0, 0],
            "GREEN": [0, 255, 0],
            "CYAN": [0, 255, 255]
        }
        return color(tex,
                     fore=(w[colr.upper()][0],
                           w[colr.upper()][1],
                           w[colr.upper()][2]),
                     back=(0, 0, 0))
    except:
        return tex

namacar={
  "1": "Smart fortwo",
  "2": "Daihatsu sirion",
  "3": "Lada vaz-2107",
  "4": "Civic ek9",
  "5": "Nissan 2000 gtr",
  "6": "Lada priora",
  "7": "Tofas dogan",
  "8": "Vaz 2114",
  "9": "Ford transit",
  "10": "Jeep wrangler rubicon",
  "11": "Mazda rx 8",
  "12": "Mini cooper",
  "13": "Peugeot 308",
  "14": "VW scirocco",
  "15": "Hyundai veloster",
  "16": "Ferarri 250 GT california",
  "17": "Benz w113",
  "18": "Mazda mx 5 miata",
  "19": "Hummer h1",
  "20": "Dodge charger",
  "21": "Dodge challanger 1960",
  "22": "Honda s2000",
  "23": "Chrysler 300 srt8",
  "24": "Bmw m135i",
  "25": "Benz 190e/w201",
  "26": "Bmw z4",
  "27": "Bmw e36 m3",
  "28": "Lexus gs 350",
  "29": "Tofas kartal",
  "30": "Audi sport quattro",
  "31": "Mitsubishi lancer evo 9",
  "32": "Subaru impreza",
  "33": "Lada niva",
  "34": "Civic type r",
  "35": "Ford mustang boss",
  "36": "Chevloret bel air",
  "37": "Toyota supra mk4",
  "38": "Benz w140",
  "39": "Civic fn2",
  "40": "Audi tt",
  "41": "Bmw m3",
  "42": "Civic Fd",
  "43": "Ford crown victoria",
  "44": "Bmw m5 e28",
  "45": "Cadillac escalade",
  "46": "Ford f150 svt raptor",
  "47": "Bmw 525 e34",
  "48": "Subaru brz / toyota gt86",
  "49": "Cadillac cts v",
  "50": "Bmw m5 e39",
  "51": "Bmw m3 e92",
  "52": "Nissan 350z / fairlady",
  "53": "Nissan skyline R32",
  "54": "Nissan skyline r34",
  "55": "Nissan silvia",
  "56": "Mazda rx7",
  "57": "Nissan 180 sx",
  "58": "Toyota ae86",
  "59": "Toyota mark 2",
  "60": "Hudson hornet",
  "61": "Lancer evo x",
  "62": "Subaru impreza wrx sti",
  "63": "Bmw m5 e60",
  "64": "Toyota camry",
  "65": "Benz g class 2005",
  "66": "Infiniti g37",
  "67": "Dodge charger srt hellcat",
  "68": "Benz c63 amg",
  "69": "Vw golf mk2",
  "70": "Vw golf mk7",
  "71": "Bmw x5 m",
  "72": "Ford explorer",
  "73": "Chevrolet camaro zl1",
  "74": "Bmw m2 cs",
  "75": "Audi s5 sportback",
  "76": "Audi rs4",
  "77": "Ford mustang gt",
  "78": "Bmw m5 f10",
  "79": "Porsche cayenne",
  "80": "Toyota vellfire / Alphard",
  "81": "Range rover",
  "82": "Benz cl65 amg",
  "83": "Bmw m4 f82",
  "84": "Benz amg gt",
  "85": "Porsche panamera turbo",
  "86": "Ford mustang",
  "87": "Land cruiser",
  "88": "Mercedes gle",
  "89": "Ferrrari 458 italia",
  "90": "Bmw m6 f13",
  "91": "Porsche 911",
  "92": "Bmw i8",
  "93": "Ford gt",
  "94": "Scania",
  "95": "Kenworth t680",
  "96": "Daf truck",
  "97": "Towing",
  "98": "Lexus lfa",
  "99": "Bmw x6",
  "100": "Lambo gallardo",
  "101": "Audi rs6",
  "102": "Supra mk5",
  "103": "Bmw m4 2021 competition",
  "104": "Bmw m5 f90",
  "105": "Benz e36",
  "106": "Dodge challenger srt demon",
  "107": "Hilux",
  "108": "Sierra 1500 denali",
  "109": "Benz s65 amg",
  "110": "Audi r8 v8",
  "111": "Acura nsx",
  "112": "Lamborghini huracan",
  "113": "Corvette c7",
  "114": "Corvette c8",
  "115": "Dodge viper",
  "116": "Nissan gtr r35",
  "117": "Benz s class",
  "118": "Audi r8 v10",
  "119": "Ferarri f12",
  "120": "Rolls Royce Phantom",
  "121": "Lamborghini urus",
  "122": "Lamborghini aventador",
  "123": "Rolls royce Boat Tail",
  "124": "Bentley continental gt",
  "125": "Benz amg gt63",
  "126": "Jeep grand cherokee",
  "127": "Benz g class 2020",
  "128": "Bmw m8",
  "129": "Buggy",
  "130": "Mclaren p1",
  "131": "Mclaren 720s",
  "132": "Lamborghini veneno",
  "133": "Lamborghini aventador svj",
  "134": "Bugatti veyron",
  "135": "Koenisegg agera r",
  "136": "F1",
  "137": "F1 New"
}

def tes():
    pass


# while True:
#     tes()
#     input()
# exit()


def cariid(urutan):
    with open('nomer_car.json', 'r', encoding='utf-8') as openfile:
        data = json.load(openfile)
    for mydatacar in data["result"]:
        if mydatacar["urutan"] == urutan:
            return mydatacar["id"]


def cariurutan(cariid):
    with open('nomer_car.json', 'r', encoding='utf-8') as openfile:
        data = json.load(openfile)
    for mydatacar in data["result"]:
        if mydatacar["id"] == cariid:
            return [1,mydatacar["urutan"]]
    return [0,cariid]

def cekdatalivery(carid):
    path = "cpm/cars/livery/"
    dir_list = os.listdir(path)
    dir_list = sorted(dir_list, key=len, reverse=False)
    if str(carid) in dir_list:
        return True
    else:
        return False


def savewscar(carid, data):
    datacarname = str(carid)
    itrliverydata = 1
    while True:
        # print(datacarname)
        if cekdatalivery(datacarname) == False:
            break
        else:
            datacarname = f"{carid}_"+str(itrliverydata)
            itrliverydata += 1
    print(f"bisa di save {datacarname}")
    dataforsave = {
        "data": data["thisCarData"]
    }
    dataforsave["data"]["Vynils"] = data["thisCarVynils"]
    # print(dataforsave)
    with open(f'cpm/cars/livery/{datacarname}', 'w', encoding='utf-8') as f:
        json.dump(dataforsave, f, ensure_ascii=False, indent=4)
    return datacarname

def modifspekbalap(datacar):
    datacar["data"]["floats"][0] = float(1)
    datacar["data"]["floats"][1] = float(99)
    datacar["data"]["floats"][2] = float(8000)
    datacar["data"]["floats"][3] = float(2300)
    datacar["data"]["floats"][4] = float(7889)
    datacar["data"]["floats"][7] = float(3)
    datacar["data"]["floats"][16] = float(0.0000000000000000000000000001)
    return datacar

def sirine(datacar):
    datacar["data"]["floats"][0] = float(1)
    return datacar
    
if __name__ == "__main__":
    vip=True
    # vip = False
    # if input("topix?") == "y":
    #     vip = True
    disp = ""
    while True:
        print(disp)
        menus = f"""
=========================
        Topix SB CPM TOOLS {persi}
=========================
0. tes
1. edit account
2. create account
number (x exit): """
        inp = input(menus)
        if inp == "x" or inp == "X":
            break
        elif inp == "0":
            pass

        elif inp == "1":
            print(c("cyan", "=================== verifyPassword"))
            while True:
                teslogin = cpm.verifyPassword(
                    input("email : "), input("password : "))
                if teslogin != None:
                    break
            print(c("cyan", "=================== getAccountInfo"))
            cpm.getAccountInfo()
            print(c("cyan", "=================== GetPlayerRecords"))
            vrs = cpm.GetPlayerRecords()
            print(c("cyan", "=================== TestGetAllCars"))
            os.system('rm -rf player/cars')
            os.mkdir('player/cars')
            cpm.TestGetAllCars()
            print(c("cyan", "=================== GetCarHash"))
            cpm.GetCarHash()
            print(c("cyan", "=================== SavePlayerRecords7"))
            print(c("red", "==========[ INFO ]==========="))
            try:
                print(f' >> Nickname : {displaywarna.disp(vrs["Name"])}')
            except:
                print(f' >> Nickname : {vrs["Name"]}')
            try:
                print(f' >> ID       : {vrs["localID"]}')
                print(f' >> Money    : {vrs["money"]}')
                print(f' >> Coin     : {vrs["coin"]}')
            except:
                print("Data sebagian belum ada")
            print(c("red", "=============================="))
            menusedit = """Enter To Show Information
1. manual edit save
2. inject all cars
3. change cars to mod/ori
4. comingsoon
5. edit player cars
6. unlock klakson [FREE]
7. inject livery car
8. edit money [FREE]
9. edit coin
10. edit ID
11. reset animation
12. reset friend list
13. Rainbow Name
14. Inject Rank
15. Instant King Rank
16. Remove Unknown Cars
"""
            while True:
                inp = input(menusedit)
                if inp == "x" or inp == "X":
                    break
                elif inp == "":
                    print(c("cyan", "=================== GetPlayerRecords"))
                    vrs = cpm.GetPlayerRecords()
                    time.sleep(1)
                    with open('player/data.json', 'r', encoding='utf-8') as openfile:
                        data = json.load(openfile)
                    print(c("cyan", "==========[ INFO ]==========="))
                    try:
                        print(
                            f' >> Nickname : {displaywarna.disp(vrs["Name"])}')
                    except:
                        print(f' >> Nickname : {vrs["Name"]}')
                    try:
                        print(f' >> ID       : {vrs["localID"]}')
                        print(f' >> Money    : {vrs["money"]}')
                        print(f' >> Coin     : {vrs["coin"]}')
                    except:
                        print("Data sebagian belum ada")
                    print(c("cyan", "=============================="))
                elif inp == "1":
                    if codetok[0]!=1:
                        print(f"--> {codetok}")
                        print(c("red", "Need Access Code"))
                    else:
                        codetok=usetoken(codex)
                        with open('player/data.json', 'r', encoding='utf-8') as openfile:
                            data = json.load(openfile)
                        with open('player/carhash.json', 'r', encoding='utf-8') as openfile:
                            datacar = json.load(openfile)

                        if cpm.SavePlayerRecords7(data) and cpm.SaveCarHash(datacar):
                            disp = "Sukses"
                        else:
                            disp = "Gagal"
                elif inp == "2":
                    if codetok[0]!=1:
                        print(c("red", "Need Access Code"))
                    else:
                        codetok=usetoken(codex)
                        spek99=input("spek 99 [y/n]: ")
                        print(c("cyan", "=================== GetPlayerRecords"))
                        vrs = cpm.GetPlayerRecords()
                        with open('player/data.json', 'r', encoding='utf-8') as openfile:
                            data = json.load(openfile)
                        with open('data_mod.json', 'r', encoding='utf-8') as openfile:
                            datamod = json.load(openfile)
                        with open('carhash_mod.json', 'r', encoding='utf-8') as openfile:
                            datacar = json.load(openfile)

                        datamod["data"]["allData"] = data["data"]["allData"]
                        datamod["data"]["Name"] = data["data"]["Name"]
                        datamod["data"]["localID"] = data["data"]["localID"]
                        datamod["data"]["FriendsID"] = data["data"]["FriendsID"]
                        data = datamod

                        with open('player/data.json', 'w', encoding='utf-8') as f:
                            json.dump(data, f, ensure_ascii=False, indent=4)
                        with open('player/carhash.json', 'w', encoding='utf-8') as f:
                            json.dump(datacar, f, ensure_ascii=False, indent=4)

                        if cpm.SavePlayerRecords7(data) and cpm.SaveCarHash(datacar):
                            disp = "Sukses"
                        else:
                            disp = "Gagal"

                        path = "cpm/cars/mod/"
                        dir_list = os.listdir(path)
                        dir_list = sorted(dir_list, key=len, reverse=False)
                        for idcar in dir_list:
                            sys.stdout.write(f"  >> Inject Car id [{idcar}]    \r")
                            sys.stdout.flush()
                            with open(f'cpm/cars/mod/{idcar}', 'r', encoding='utf-8') as openfile:
                                datacar = json.load(openfile)
                            if spek99=="y":
                                datacar=modifspekbalap(datacar)
                            if cpm.SaveCars(datacar):
                                disp = "Sukses"
                            else:
                                disp = "Gagal"
                elif inp == "3":
                    if codetok[0]!=1:
                        print(c("red", "Need Access Code"))
                    else:
                        codetok=usetoken(codex)
                        if input(" 1:ori 2:mod = ") == "2":
                            tipe = "mod"
                        else:
                            tipe = "ori"
                        idcar = input("ID CAR : ")
                        with open(f'cpm/cars/{tipe}/{idcar}', 'r', encoding='utf-8') as openfile:
                            datacar = json.load(openfile)
                        if cpm.SaveCars(datacar):
                            disp = "Sukses"
                        else:
                            disp = "Gagal"
                elif inp == "4":
                    print("bt emot batu detailing pc dean :v")
                elif inp == "5":
                    if codetok[0]!=1:
                        print(c("red", "Need Access Code"))
                    else:
                        codetok=usetoken(codex)
                        dir_list = sorted(os.listdir("player/cars/"), key=len, reverse=False)
                        print("\n  [ Urutan Cars yang tersedia ]")
                        dir_urut=[]
                        for idnya in dir_list:
                            urt=cariurutan(idnya)
                            if urt!=None:
                                dir_urut.append({"urut":urt,"id":idnya})

                        dir_urut=sorted(dir_urut ,key=lambda k:k["urut"])
                        for urid in dir_urut:
                            try:
                                print(f'urutan : {urid["urut"]}\t[{urid["id"]}] {namacar[str(urid["urut"])]}')
                            except:
                                pass

                        urutcar = input("\nurutan car : ")
                        idcar = cariid(int(urutcar))
                        if idcar == None:
                            print("ga ada data id car")
                        else:
                            print(f"ID CAR NYA ADALAH {idcar}")
                            with open(f'player/cars/{idcar}', 'r', encoding='utf-8') as openfile:
                                datacar = json.load(openfile)
                            menuscar = """

        [ Menu Edit ]
    1. Police on
    2. Police off
    3. Inject livery
    4. Bongkar Spek
    5. Magnet cars
    6. w16 engine and set-up other
    7. chrome Car
    Save & Exit = q
    choice :
    """

                            while True:
                                caredit = input(menuscar)
                                if caredit == "q":
                                    break
                                elif caredit == "1":
                                    datacar["data"]["floats"][0] = 1
                                elif caredit == "2":
                                    datacar["data"]["floats"][0] = 0
                                elif caredit == "3":
                                    try:
                                        with open(f'cpm/cars/livery/{urutcar}', 'r', encoding='utf-8') as openfile:
                                            datacar = json.load(openfile)
                                    except:
                                        print(
                                            f"Belum punya data livery mobil ke {urutcar}")
                                elif caredit == "4":
                                    print("mulai dari HP")
                                    datacar["data"]["floats"][1] = float(
                                        input("HP\t:"))
                                    datacar["data"]["floats"][2] = float(
                                        input("inner HP\t:"))
                                    datacar["data"]["floats"][3] = float(
                                        input("NM\t:"))
                                    datacar["data"]["floats"][4] = float(
                                        input("inner NM\t:"))
                                    datacar["data"]["floats"][7] = float(
                                        input("Grip\t:"))
                                    datacar["data"]["floats"][16] = float(
                                        input("Shift Time\t:"))

                                    with open(f'player/cars/{idcar}', 'w', encoding='utf-8') as f:
                                        json.dump(datacar, f, ensure_ascii=False, indent=4)
                                elif caredit == "5":
                                    orivectors=[
    {'x': 2, 'z': 2, 'y': 2},
    {'y': 2, 'x': 2, 'z': 2},
    {'z': 2, 'x': 2, 'y': 2},
    {'z': 2, 'x': 2, 'y': 2},
    {'z': 2, 'y': 2, 'x': 2},
    {'x': 2, 'y': 2, 'z': 2},
    {'z': 1, 'x': -2, 'y': -2},
    {'z': 2, 'y': 2, 'x': 2},
    {'z': 2, 'y': 2, 'x': 2},
    {'z': 2, 'x': 2, 'y': 2},
    {'y': 2, 'z': 2, 'x': 2},
    {'x': 2, 'z': 2, 'y': 2},
    {'z': 2, 'y': 2, 'x': 2},
    {'z': 0, 'y': -2, 'x': -2},
    {'y': 2, 'z': 2, 'x': 2},
    {'z': 0, 'y': -2, 'x': -2},
    {'x': 0, 'z': 2, 'y': 0},
    {'z': 1, 'y': 1, 'x': 1},
    {'z': 2, 'y': 2, 'x': 2},
    {'z': 2, 'y': 2, 'x': 2},
    {'z': 2, 'y': 2, 'x': 2}]
                                
                                    tnya=input("1.ori\n2.magnet\nChoose Number: ")
                                    if tnya=="x":
                                        break
                                    try:
                                        po=int(tnya)
                                        if po ==1: datacar["data"]["vectors"]=orivectors
                                        elif po ==2: datacar["data"]["vectors"][6]["x"]=float(99999999999)
                                        else:
                                            print("wrong input")
                                        with open(f'player/cars/{idcar}', 'w', encoding='utf-8') as f:
                                            json.dump(datacar, f, ensure_ascii=False, indent=4)
                                    except:
                                        pass
                                elif caredit == "6":
                                    bp=[]
                                    for bpp in datacar["data"]["BoughtParts"]:
                                        bp.append(1)
                                    datacar["data"]["BoughtParts"]=bp
                                    datacar["data"]["floats"][17]=1
                                    datacar["data"]["floats"][18]=1

                                    with open(f'player/cars/{idcar}', 'w', encoding='utf-8') as f:
                                        json.dump(datacar, f, ensure_ascii=False, indent=4)
                                        pass
                                elif caredit == "7":
                                    bp=[]
                                    for bpp in datacar["data"]["BoughtParts"]:
                                        bp.append(1)
                                    datacar["data"]["BoughtParts"]=bp
                                    datacar["data"]["floats"][17]=1
                                    datacar["data"]["floats"][18]=1
                                    #chrome
                                    datacar["data"]["vectors"][12]={"x": -5,"z": -5,"y": -5}

                                    with open(f'player/cars/{idcar}', 'w', encoding='utf-8') as f:
                                        json.dump(datacar, f, ensure_ascii=False, indent=4)
                            if cpm.SaveCars(datacar):
                                disp = "Sukses"
                            else:
                                disp = "Gagal"
                elif inp == "6":
                    print(c("cyan", "=================== GetPlayerRecords"))
                    vrs = cpm.GetPlayerRecords()
                    with open('player/data.json', 'r', encoding='utf-8') as openfile:
                        data = json.load(openfile)
                    data["data"]["floats"][27] = 1
                    data["data"]["floats"][28] = 1
                    data["data"]["floats"][29] = 1
                    data["data"]["floats"][30] = 1
                    data["data"]["floats"][31] = 1

                    if cpm.SavePlayerRecords7(data):
                        disp = "Sukses"
                    else:
                        disp = "Gagal"
                elif inp == "7":
                    if codetok[0]!=1:
                        print(c("red", "Need Access Code"))
                    else:
                        codetok=usetoken(codex)
                        foldername=input("Nama Folder : ")
                        spek99=input("spek 99 [y/n]: ")
                        modeliv=input("modeliv : ")
                        isikosong=input("isi livery kosong dgn yg pertama? y/n: ").lower()
                        dir_list = os.listdir(f"cpm/cars/{foldername}/")
                        dir_list.sort(key=int)
                        terdesign=0
                        loopcar=0
                        for idcar in dir_list:
                            if modeliv!="":
                                if "_" in idcar:
                                    kidcar=int(idcar.split("_")[0])
                                    if idcar.split("_")[1]==modeliv:
                                        # print("________________________________")
                                        # print(f"[{kidcar}:{loopcar}]")
                                        if int(kidcar)==int(loopcar):
                                            print(f'>> file : {idcar}\tloop : {loopcar} ')
                                            # kmode=idcar.split("_")[1]
                                            with open(f'cpm/cars/{foldername}/{idcar}', 'r', encoding='utf-8') as openfile:
                                                datacar = json.load(openfile)
                                            if spek99=="y":
                                                datacar=modifspekbalap(datacar)
                                            if cpm.SaveCars(datacar)==True:
                                                terdesign+=1
                                            loopcar+=1
                                        else:
                                            tambahlup=0
                                            loopcar-=1
                                            while int(kidcar)!=int(loopcar):
                                                print(f'>~ file : {int(kidcar)}\tloop : {str(loopcar+tambahlup)}')
                                                kidcar-=1
                                                tambahlup+=1
                                                try:
                                                    if isikosong=="y":
                                                        with open(f'cpm/cars/{foldername}/{kidcar}', 'r', encoding='utf-8') as openfile:
                                                            datacar = json.load(openfile)
                                                        if spek99=="y":
                                                            datacar=modifspekbalap(datacar)
                                                    else:
                                                        print("Tidak di di isi livery pertama")
                                                except:
                                                    print(f"ID_Car {kidcar} tidak di temukan")
                                                if cpm.SaveCars(datacar)==True:
                                                    terdesign+=1
                                                time.sleep(1)
                                            loopcar+=tambahlup+1
                            else:
                                if "_" not in idcar:
                                    with open(f'cpm/cars/{foldername}/{idcar}', 'r', encoding='utf-8') as openfile:
                                        datacar = json.load(openfile)
                                    print(f'>> file : {idcar} ')
                                    datacar=sirine(datacar)
                                    if spek99=="y":
                                        datacar=modifspekbalap(datacar)
                                    if cpm.SaveCars(datacar)==True:
                                            terdesign+=1
                        print(f"Livery yang terpasang : {terdesign}")
                elif inp == "8":
                    codetok=usetoken(codex)
                    print(c("cyan", "=================== GetPlayerRecords"))
                    vrs = cpm.GetPlayerRecords()
                    muniy = input("Money : ")
                    with open('player/data.json', 'r', encoding='utf-8') as openfile:
                        data = json.load(openfile)
                    data["data"]["money"] = int(muniy)
                    if cpm.SavePlayerRecords7(data):
                        disp = "Sukses"
                    else:
                        disp = "Gagal"
                elif inp == "9":
                    if codetok[0]!=1:
                        print(c("red", "Need Access Code"))
                    else:
                        codetok=usetoken(codex)
                        print(c("cyan", "=================== GetPlayerRecords"))
                        vrs = cpm.GetPlayerRecords()
                        muniy = input("Coin : ")
                        with open('player/data.json', 'r', encoding='utf-8') as openfile:
                            data = json.load(openfile)
                        data["data"]["coin"] = int(muniy)
                        if cpm.SavePlayerRecords7(data):
                            disp = "Sukses"
                        else:
                            disp = "Gagal"
                elif inp == "10":
                    if codetok[0]!=1:
                        print(c("red", "Need Access Code"))
                    else:
                        codetok=usetoken(codex)
                        print(c("cyan", "=================== GetPlayerRecords"))
                        vrs = cpm.GetPlayerRecords()
                        muniy = input("localID : ")
                        with open('player/data.json', 'r', encoding='utf-8') as openfile:
                            data = json.load(openfile)
                        data["data"]["localID"] = muniy
                        if cpm.SavePlayerRecords7(data):
                            disp = "Sukses"
                        else:
                            disp = "Gagal"
                elif inp == "11":
                    if codetok[0]!=1:
                        print(c("red", "Need Access Code"))
                    else:
                        codetok=usetoken(codex)
                        print(c("cyan", "=================== GetPlayerRecords"), 0)
                        vrs = cpm.GetPlayerRecords()
                        with open('player/data.json', 'r', encoding='utf-8') as openfile:
                            data = json.load(openfile)
                        data["data"]["animations"] = []
                        if cpm.SavePlayerRecords7(data):
                            disp = "Sukses"
                        else:
                            disp = "Gagal"
                elif inp == "12":
                    if codetok[0]!=1:
                        print(c("red", "Need Access Code"))
                    else:
                        codetok=usetoken(codex)
                        print(c("cyan", "=================== Reset Friend List"))
                        vrs = cpm.GetPlayerRecords()
                        with open('player/data.json', 'r', encoding='utf-8') as openfile:
                            data = json.load(openfile)
                        data["data"]["FriendsID"] = []
                        if cpm.SavePlayerRecords7(data):
                            disp = "Sukses"
                        else:
                            disp = "Gagal"
                elif inp == "13":
                    if codetok[0]!=1:
                        print(c("red", "Need Access Code"))
                    else:
                        codetok=usetoken(codex)
                        print(c("cyan", "=================== Rainbow Name"))
                        with open('player/data.json', 'r', encoding='utf-8') as openfile:
                            data = json.load(openfile)
                        data["data"]["Name"] = NamaBerwarna.generate()
                        if cpm.SavePlayerRecords7(data):
                            disp = "Sukses"
                            vrs = cpm.GetPlayerRecords()
                        else:
                            disp = "Gagal"
                elif inp == "14":
                    if codetok[0]!=1:
                        print(c("red", "Need Access Code"))
                    else:
                        codetok=usetoken(codex)
                        print(c("cyan", "=================== Inject Rank")) 
                        contoh={
                                "t_distance":0,
                                "time":0,
                                "speed_banner":0,
                                "gifts":0,
                                "treasure":0,
                                "cars":0,
                                "race_win":0,
                                "levels":0,
                                "drift":0,
                                "run":0,
                                "police":0,
                                "block_post":0,
                                "real_estate":0,
                                "fuel":0,
                                "car_trade":0,
                                "car_exchange":0,
                                "burnt_tire":0,
                                "car_fix":0,
                                "car_wash":0,
                                "offroad":0,
                                "passanger_distance":0,
                                "reactions":0,
                                "drift_max":0,
                                "taxi":0,
                                "delivery":0,
                                "cargo":0,
                                "push_ups":0,
                                "slicer_cut":0,
                                "car_collided":0,
                                "new_type":0
                                }
                        isidata={
                            "RatingData":{}
                            }
                        itr=1
                        for x in contoh:
                            print(f"{itr}. {x}")
                            itr+=1
                        while True:
                            while True:
                                time.sleep(0.2)
                                try:
                                    inp=input("edit [num value] exit=q: ")
                                    if inp=="q":break
                                    nums=inp.split(" ")[0]
                                    palue=inp.split(" ")[1]
                                    if palue == "inf":
                                        palue=float("3E38")
                                    break
                                except:
                                    pass
                            if inp=="q":break
                            itr=1
                            for x in contoh:
                                if int(nums)==itr:
                                    isidata["RatingData"][x]=float(palue)
                                itr+=1
                            print(json.dumps(isidata,indent=2))
                        
                        if cpm.SetUserRatingCall(isidata)!=False:
                            disp = "Sukses"
                        else:
                            disp = "Gagal"
                    
                elif inp == "15":
                    if codetok[0]!=1:
                        print(c("red", "Need Access Code"))
                    else:
                        codetok=usetoken(codex)
                        print(c("cyan", "=================== Istant King Rank")) 
                        contoh={
                                "t_distance":10000,
                                "time":30000,
                                "speed_banner":1000,
                                "gifts":100,
                                "treasure":100,
                                "cars":137,
                                "race_win":1000,
                                "levels":82,
                                "drift":1000,
                                "run":500,
                                "police":1000,
                                "block_post":1000,
                                "real_estate":12,
                                "fuel":10000,
                                "car_trade":100,
                                "car_exchange":100,
                                "burnt_tire":100,
                                "car_fix":100,
                                "car_wash":100,
                                "offroad":1000,
                                "passanger_distance":1000,
                                "reactions":2000,
                                "drift_max":1000,
                                "taxi":1000,
                                "delivery":1000,
                                "cargo":1000,
                                "push_ups":957,
                                "slicer_cut":1,
                                "car_collided":1,
                                "new_type":0
                                }
                        isidata={
                            "RatingData":contoh
                            }
                        
                        if cpm.SetUserRatingCall(isidata)!=False:
                            disp = "Sukses"
                        else:
                            disp = "Gagal"
                elif inp == "16":
                    if codetok[0]!=1:
                        print(c("red", "Need Access Code"))
                    else:
                        codetok=usetoken(codex)
                        dir_list = sorted(os.listdir("player/cars/"), key=len, reverse=False)
                        print("\n  [ Urutan Cars yang tersedia ]")
                        dir_urut=[]
                        for idnya in dir_list:
                            urt=cariurutan(idnya)
                            if urt[0]==1:
                                dir_urut.append({"urut":urt[1],"id":idnya})
                            else:
                                print(idnya)
                                xxcx=cpm.RemoveCarFromDatabase(int(idnya))
                                print(f'reqRemove : {xxcx}')

                        dir_urut=sorted(dir_urut ,key=lambda k:k["urut"])
                        for urid in dir_urut:
                            try:
                                print(f'urutan : {urid["urut"]}\t[{urid["id"]}] {namacar[str(urid["urut"])]}')
                            except:
                                pass

        elif inp == "2":
            if codetok[0]!=1:
                print(c("red", "Need Access Code"))
            else:
                codetok=usetoken(codex)
                print("Create Account")
                if cpm.signupNewUser(input(" Email : "), input(" Password : ")):
                    with open('data_basic.json', 'r') as openfile:
                        data = json.load(openfile)
                    data["data"]["Name"] = "Player#" + str(random.randint(11111, 99999))
                    data["data"]["localID"] = "TSB" + str(random.randint(11111, 99999))

                    print(c("red", "=============================="))
                    try:
                        print(
                            f' >> Nickname : {displaywarna.disp(data["data"]["Name"])}')
                    except:
                        print(f' >> Nickname : {data["data"]["Name"]}')
                    try:
                        print(f' >> ID       : {data["data"]["localID"]}')
                        print(f' >> Money    : {data["data"]["money"]}')
                        print(f' >> Coin     : 0')
                    except:
                        print("Data sebagian belum ada")
                    print(c("red", "=============================="))
                    with open('carhash_basic.json', 'r') as openfile:
                        datacar = json.load(openfile)
                    if cpm.SavePlayerRecords7(data) and cpm.SaveCarHash(datacar):
                        disp = "Sukses"
                    else:
                        disp = "Gagal"
                else:
                    disp = "Email sudah terdaftar"
        else:
            print("Wrong...!")
