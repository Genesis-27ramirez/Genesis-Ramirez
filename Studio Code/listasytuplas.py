# Tuplas - Inventario

inventario = [
    (101, "laptops", 800.00),
    (102, "mouse", 25.50),
    (103, "teclado", 45.00),
    (104, "auriculares", 80.00),
    (105, "tablet", 40.00)
]

def mostrar_inventario(lista_de_productos):
    print("Inventario de productos:")
    for producto in lista_de_productos:
        print(f"ID: {producto[0]}, Nombre: {producto[1]}, Precio: ${producto[2]:.2f}")

def calcular_valor_total_inventario(lista_de_productos):
    valor_total = 0
    for producto in lista_de_productos:
        valor_total += producto[2]  # sumar el precio de cada producto
    return valor_total

# Llamadas a las funciones
mostrar_inventario(inventario)

valor_total_inventario = calcular_valor_total_inventario(inventario)
print(f"\nValor total del inventario: ${valor_total_inventario:.2f}")