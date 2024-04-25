# Proyecto Final
# Laura Cintora Cendejas
# A01712379
# Memorama (Español, Quimica y Matematicas)
# Pensamiento Computacional Para Ingeneria
# Gpo 852

import random

def ver_carta(cartas):  #Funcion: Mostrar cartas 
    for ficha in cartas: 
        if ficha == "*":
            print (ficha, end=" ")
        else:
            print(ficha[0], end=" ")
    print()

def verificacion(maximo): #Funcion: Para verificar si el numero es valido mayor a 0 y menor a la longitud del memorarama 7
    while True:
        try:
            numero = int(input(f"Elige un número del 0 al {maximo - 1}: "))
            if 0 <= numero < maximo:
                return numero
            else:
                print(f"Incorrecto .Elige un número entre 0 y {maximo - 1}.")
        except ValueError: # Use la funcion except para evitar que se cortara el programa al presionar cuqluier tecla no numerica.
            print("Error. Introduce un número.")

def juego_memorama(carta_seleccionada): #Ejecuta un juego de memorama con las cartas especificadas
    cartas = ['*'] * len(carta_seleccionada)
    par_encontrado = 0
    resultado_par = len(carta_seleccionada) // 2
    while par_encontrado < resultado_par:   #Ciclo: El par debe ser menor que el resultado
        print("\nMEMORAMA")
        ver_carta(cartas)
        uno = verificacion(len(cartas))    #Funcion para coincidir carta uno
        while cartas[uno] != '*':
            print("Intenta otra vez")
            uno = verificacion(len(cartas))
        cartas[uno] = carta_seleccionada[uno]
        ver_carta(cartas)
        dos = verificacion(len(cartas))   #Funcion para coincidir carta dos 
        while dos == uno or cartas[dos] != '*':
            if dos == uno:
                print("Elige otra, ya esta seleccionada")
            else:
                print("Intenta, otra vez")
            dos = verificacion(len(cartas))
        cartas[dos] = carta_seleccionada[dos]
        ver_carta(cartas)
        if carta_seleccionada[uno][1] == carta_seleccionada[dos][0]: #Validar que carta uno y dos sean iguales 
            print("\nPAR ENCONTRADO")
            par_encontrado += 1
        else:
            print("No coinciden las cartas")
            cartas[uno] = cartas[dos] = "*"
    print("¡FELICIDADES!") 

#Cartas del memorama de ESPAÑOL

español = [("Presente", "subo"), ("Preterito", "amé"), ("Futuro", "comeré"), ("Copretérito", "miraba")]
memorama_español = []      #Funcion: Append para agregar las tuplas de las cartas.
for palabra in español:
    nombre, verbo = palabra
    memorama_español.append((nombre, verbo))
    memorama_español.append((verbo, nombre))

def main():
    random.shuffle(memorama_español) #Shuffle se uso para mezlar las cartas

#Cartas del memorama de QUIMICA
quimica = [("H", "Hidrogeno"), ("N", "Nitrogeno"), ("C", "Carbono"), ("O", "Oxígeno")]
quimica_1 = []
for elemento in quimica:
    formula, nombre = elemento
    quimica_1.append((formula, nombre))
    quimica_1.append((nombre, formula))
random.shuffle(quimica_1)

#Cartas del memorama de MATEMATICAS
matematicas = [("11", "23+6-18"), ("10x", "2x+8x"), ("67.5", "45/2*3"), ("1/6", "1/2-1/3")]
operacion = []
for resultado in matematicas:
    total, calculo = resultado
    operacion.append((total, calculo))
    operacion.append((calculo, total))
random.shuffle(operacion)

while True:             # Menú para seleccionar el juego que eliga el usuario
    print("\nMemorama")
    print("1. Juego de memorama de ESPAÑOL")
    print("2. Juego de memorama de QUIMICA")
    print("3. Juego de memorama de MATEMATICAS")
    print("4. Salir")
    opcion = int(input("Elige una opción: "))   #Uso de if y elif para que se ejecuten las funciones dependiendo de la seleccion del menu
    if opcion == 1:
        print("\nHas seleccionado el memorama de español.")
        main()
        juego_memorama(memorama_español)
    elif opcion == 2:
        print("\nHas seleccionado el memorama de química.")
        main()
        juego_memorama(quimica_1)
    elif opcion == 3:
        print("\nHas seleccionado el memorama de química.")
        main()
        juego_memorama(operacion)
    elif opcion == 4:
        print("Salir")
        break
    else:
        print("Opción Incorrecta")
        print("Intenta otra vez")