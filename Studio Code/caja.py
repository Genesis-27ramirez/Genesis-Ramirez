# --- MARKER PLANE ---
 
 
# Datos iniciales
stock = 20
precio_unitario = 50
ganancia_total = 0
presupuesto = 1000
 
while stock >0 :
    print("\n--- TIENDA DE ZAPATILLAS ---")
    print("1. Comprar zapatillas")
    print("2. Vender zapatillas")
    print("3. Ver estado")
    print("4. Salir")
 
    opcion = int(input("Elige una opcion: "))
 
    # COMPRAR
    if opcion == 1:
        cantidad = int(input("Cuantas zapatillas quieres comprar: "))
        costo = cantidad * precio_unitario
 
        if presupuesto >= costo:
            stock -= cantidad
            presupuesto -= costo
            print("Compra realizada")
        else:
            print("No hay suficiente presupuesto")
 
    # VENDER
    elif opcion == 2:
        cantidad = int(input("Cuantas zapatillas quieres vender: "))
 
        if stock >= cantidad:
            venta = cantidad * precio_unitario
            stock -= cantidad
            ganancia_total += venta
            presupuesto += venta
            print("Venta realizada")
        else:
            print("No hay suficiente stock")
 
    # ESTADO
    elif opcion == 3:
        print("\n--- ESTADO ACTUAL ---")
        print(f"Stock: {stock}")
        print(f"Precio unitario: {stock} precio_unitario")
        print(f"Ganancia total: {stock} ganancia_total")
        print(f"Presupuesto: {stock} presupuesto")
 
    # SALIR
    elif opcion == 4:
        print("Programa terminado")
        break
 
    else:
        print("Opcion invalida")

 