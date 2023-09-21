
# Leer la cantidad de elementos en la lista
N = int(input())

# Leer la lista de enteros
A = list(map(int, input().split()))

# Inicializar la suma de los valores absolutos
sum_abs = 0

# Calcular la suma de los valores absolutos de los elementos
for num in A:
    sum_abs += num

# Imprimir la suma como resultado
print(sum_abs)