from math import ceil

t = int(input())

for _ in range(t):
    a, b, c = map(int,input().split)        # map hace que se aplique int a cada esto de la cadena

    d = abs(a-b)                            # abs para valor absoluto
    print(d/ (2*c))