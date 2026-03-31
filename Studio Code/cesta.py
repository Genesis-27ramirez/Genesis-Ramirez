cesta = {}

while True:
    producto = input("Introduce un producto: ")
    precio = float(input("Introduce su precio: "))

    cesta[producto] = precio

    continuar = input("¿Quieres añadir otro producto? (s/n): ")
    if continuar.lower() == "n":
        break

total = 0

print("\nLista de la compra:")

for producto, precio in cesta.items():
    print(f"{producto}/{precio}")
    total += precio

print(f"Total: {total:.2f}")