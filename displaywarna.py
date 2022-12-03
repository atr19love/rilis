
from colr import color


def disp(clrnama):
    clrfirsttime = True
    clrVnama = clrnama.split("[")
    clrdisps = clrVnama[0]
    for clrx in clrVnama:
        if clrfirsttime == False:
            clrcode1 = f"{clrx[0:2]}"
            clrcode2 = f"{clrx[2:4]}"
            clrcode3 = f"{clrx[4:6]}"
            clrcode1 = (int(clrcode1, 16))
            clrcode2 = (int(clrcode2, 16))
            clrcode3 = (int(clrcode3, 16))
            clrhuruf = clrx[7:8]
            clrdisps += color(clrhuruf,
                              fore=(clrcode1,
                                    clrcode2,
                                    clrcode3),
                              back=(0, 0, 0))
        if clrfirsttime:
            clrfirsttime = False

    clrdisps += clrVnama[len(clrVnama)-1][8:len(clrVnama[len(clrVnama)-1])]
    return(clrdisps)
