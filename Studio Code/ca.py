# Programa de cajero automático
 
saldo = 500
limite_retiro = 200
 
for intento in range(10):   # máximo 10 operaciones
    while saldo > 0:
        retiro = int(input("¿Cuánto dinero deseas retirar? (0 para salir): "))
 
        if retiro == 0:
            print("Gracias por usar el cajero.")
            saldo = 0
            break
 
        elif retiro > limite_retiro:
            print("No puedes retirar más del límite permitido:", limite_retiro)
 
        elif retiro > saldo:
            print("No tienes suficiente saldo.")
 
        else:
            saldo -= retiro
            print("Retiro exitoso.")
            print("Saldo restante:", saldo)
 
        if saldo == 0:
            print("Tu cuenta se quedó sin saldo.")
            break
 
    break