import time

def calcul(N):
    start = time.time()
    sum = 0
    for i in range(1, N+1):
        sum += i
    end = time.time()
    return end-start


print(calcul(8388608))


def algoA(objet,poidsMax):
    prendre=[]
    sacTemp=[]
    poids=0
    terminé=False
    i = 0
    while terminé!=True:
        j=i+1
        for i in range(len(objet)):
            for j in range(len(objet)):
                if poids+objet[]>poidsMax