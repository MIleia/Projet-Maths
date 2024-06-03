import time

def calcul(N):
    start = time.time()
    sum = 0
    for i in range(1, N+1):
        sum += i
    end = time.time()
    return end-start


print(calcul(8388608))


