
N = int(input())

A = list(map(int, input().split()))

numero_cercano = A[0] 
distancia_cercana = abs(A[0])

for numero in A:
    distancia_actual = abs(numero)
    if distancia_actual < distancia_cercana:
        distancia_cercana = distancia_actual
        numero_cercano = numero

print(numero_cercano)

