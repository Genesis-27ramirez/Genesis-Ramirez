# Programa para ingresar números de la Lotería 
numeros = []

print("Introduce los 2 números ganadores de la Lotería:")

for i in range(2):
    num = int(input(f"Número {i+1}: "))
    numeros.append(num)

# Ordenar la lista
numeros.sort()

# Obtener el número ganador (el mayor)
ganador = numeros[-1]


# Mostrar resultados
print("Números ordenados de menor a mayor:")
print(numeros)

print("El número ganador es:")
print(ganador)