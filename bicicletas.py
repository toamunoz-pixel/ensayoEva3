print("Bienvenido al sistema de gestion de bicicletas")
capacidad_maxima = 25
bicis_disponibles = 25
viajes_activos = 0
ejecutando = True
#ciclo Principal
while ejecutando:
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Bicicletas disponibles")
    print("2. Arrendar bicicletas (Salida)")
    print("3. Devolver bicicletas (Entrada)")
    print("4. Historial de viajes activos")
    print("5. Salir")
    try:
        opcion = int(input("Seleccione una opcion (1-5): "))
    except ValueError:
        print("Opcion no valida, por favor, ingrese un numero entre 1 y 5")
        continue
    #opcion 1
    if opcion == 1:
        print(f"\n[INFO] Cantidad actual de bicicletas disponibles: {bicis_disponibles}")
    #opcion 2 Arrendar bicicletas
    elif opcion == 2:
        print(f"\n--- Arrendar bicicletas (Dsiponibles: {bicis_disponibles})---")
        if bicis_disponibles == 0:
            print("Lo sentimos, no quedan bucicletas disponibles")
        else:
            try:
                cantidad_a_arrendar = int(input("¿Cuantas bicicletas desea arrendar?: "))
                if cantidad_a_arrendar <= 0:
                    print("Error:  la cantidad a arrendar debe ser mayor a 0")
                elif cantidad_a_arrendar > bicis_disponibles:
                    print(f"no hay suficientes bicicletas, puede arrendar hasta: {bicis_disponibles}")
                else:
                    bicis_disponibles -= cantidad_a_arrendar
                    viajes_activos += cantidad_a_arrendar
                    print(f"Arriendo exitoso, ha retirado {cantidad_a_arrendar} bicis")
            except ValueError:
                print("Error, debe ingresar un numero entero")
    #opcion 3 _devolver biciletas
    elif opcion == 3:
        diferencia = capacidad_maxima-bicis_disponibles
        print(f"\n--- DEVOLVER BICILETA (espacio libre en estacion: {diferencia})")
        try:
            cantidad_a_devolver = int(input("¿Cuantas bicicletas desea devolver?: "))
            if cantidad_a_devolver <= 0:
                print("Error: la cantidad a devolver debe ser mayor a 0")
            elif bicis_disponibles + cantidad_a_devolver > capacidad_maxima:
                prin(f"Error: no se pueden devolver tantas bicicletas, supera cantidad máxima de 25 bicis")
            else:
                bicis_disponibles += cantidad_a_devolver
                viajes_activos -= cantidad_a_devolver
                print(f"Devolucion exitosa ha regresado {cantidad_a_devolver} biciletas")
        except ValueError:
            print("Error debe ingresar un numero entero valido")
    #opcion 4: Viajes activos
    elif opcion == 4:
        print(f"\n[HISTORIAL] actualmente hay {viajes_activos} bicicletas en uso por usuarios")
        