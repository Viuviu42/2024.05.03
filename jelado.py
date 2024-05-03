class Jel:
    def __init__(self,h,min,sec,x,y):
        self.h = int(h)
        self.min = int(min)
        self.sec = int(sec)
        self.x = x
        self.y = y

def eltelt(sh, smin, ssec, eh, emin, esec):
    return (eh*60*60+emin*60+esec)-(sh*60*60+smin*60+ssec)

file = open("jel.txt","rt")
jel = []
count = 0

for i in file:
    row = i.strip().split(" ")
    jel.append(Jel(row[0], row[1], row[2],row[3],row[4]))

    
print("2. feladat")
qestion = int(input("Adja meg a jel sorszámát!"))
print(f"x={jel[qestion-1].x} y={jel[qestion-1].y}")

