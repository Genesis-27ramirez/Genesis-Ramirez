while True:
    Frase = input("Escriba su frase: ")
    Letra = input("Escriba su letra: ")

    # Contador de cuantas veces aparece la letra
    count = 0 
    for a in Frase:
        if a == Letra:
            count += 1

    # Mostrar resultado
    print("La letra aparece", count, "veces en la frase")

    # Preguntar si quiere continuar
    repetir = input("¿Desea intentar otra vez? (s/n): ")
    if repetir.lower() != 's':
        print("Programa finalizado.")
        break