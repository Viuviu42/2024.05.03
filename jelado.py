class Jel:
    def __init__(self,h,min,sec,x,y):
        self.h = int(h)
        self.min = int(min)
        self.sec = int(sec)
        self.x = int(x)
        self.y = int(y)

def eltelt(sh, smin, ssec, eh, emin, esec):
    return (eh*60*60+emin*60+esec)-(sh*60*60+smin*60+ssec)

file = open("jel.txt","rt")
jel = []
count = 0

for i in file:
    row = i.strip().split(" ")
    jel.append(Jel(row[0], row[1], row[2],row[3],row[4]))

xmin = xmax = jel[0].x
ymax = ymin = jel[0].y

print("2. feladat")
qestion = int(input("Adja meg a jel sorszámát!"))
print(f"x={jel[qestion-1].x} y={jel[qestion-1].y}")

print("4. feladat")
ido = eltelt(jel[0].h, jel[0].min, jel[0].sec, jel[-1].h, jel[-1].min, jel[-1].sec)
ora =int(ido / (60*60))
perc = int((ido - ora*60*60) / 60)
ms = int(ido - perc*60 - ora*60*60)
print("Időtartam", ora, ":",perc, ":" ,ms)

for i in jel:
    if i.x > xmax:
        xmax = i.x
    if i.x < xmin:
        xmin = i.x
    if i.y > ymax:
        ymax = i.y
    if i.y < ymin:
        ymin = i.y

print("5.feladat")
print(f"Bal also: {xmin} {ymin} Jobb felso: {xmax} {ymax}")