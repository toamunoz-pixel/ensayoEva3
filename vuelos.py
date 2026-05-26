print("=== Registro de equipaje - vuelos chile ===")
#1.- Validar la cantidad total de equipaje a registrar 
total_equipaje = 0
while total_equipaje <= 0:
    try:
        entrada = input("¿Cuantos equipajes desea registrar?: ")
        total_equipaje = int(entrada)
        if total_equipaje <= 0:
            print("¡Cantidad invalida! Ingresa un entero positivo para continuar. ")
    except ValueError:
     print("¡Cantidad invalida! Ingresa un entero positivo para continuar. ")
#Inicializacion de contadores 
equipajes_cabina = 0
equipajes_bodega = 0
#2 Ciclo de registro del equipaje
for i in range(total_equipaje):
    print(f"\n--- Registro del equipaje N° {i+1} ---")
    #Validacion del codigo del ticket
    codigo_ticket = ""
    while True:
        codigo_ticket = input("Ingrese codigo de ticket (Min 5 caracteres, sin espacios)")
        #Validar largo de codigo de ticket
        if len(codigo_ticket) > 5 :
            print("¡Error! el codigo debe tener al menos 5 caracteres")
            continue
        #Validar  que no tenga espacios
        tiene_espacios = False
        for caracter in codigo_ticket:
            if caracter == " ":
                tiene_espacios = True
        if tiene_espacios:
            print("¡Error! el codigo no deebe incluir espacios")
            continue
        break
    #Validacion del peso
    peso = -1
    while peso <= 0:
        try:
            entrada_peso = input("Ingrese el peso del equipaje en kg (entero positivo)")
            peso = int(entrada_peso)
            if peso <= 0:
                print("¡Error de pesaje! Ingrese un numero positivo para el peso")
        except ValueError:
             print("¡Error de pesaje! Ingrese un numero positivo para el peso")
    # paso 3. Clasificacion del equipaje
    if peso  > 10:
        equipajes_bodega += 1
        print("Clasificado como equipo de bodega")
    else:
        equipajes_cabina +=1
        print("Clasificado  como equipo de cabina")
# paso 4. Salida final
print("\n====================================")
print(f"¡El avion transportara {equipajes_cabina} equipajes en bodega y {equipajes_cabina} equipajes en bodega!¡Manifiesto completo")
print("======================================")