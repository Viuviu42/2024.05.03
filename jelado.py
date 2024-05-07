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

for i in range(len(jel)-1):
    onex = jel[i].x-jel[i+1].x
    oney = jel[i].y-jel[i+1].y
    one = onex**2 + oney**2
    count += one**0.5
print("6. feladat")
print(f"Elmozdulás: {round(count, 3)} egység")

hetfeladat = open("kimaradt.txt", "wt")
for i in range(1, len(jel)):
    ido = eltelt(jel[i-1].h, jel[i-1].min, jel[i-1].sec, jel[i].h, jel[i].min, jel[i].sec)
    print(ido)