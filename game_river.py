nombre = input("Para comenzar el juego escribe tu nombre: ")
print("\n")
print(".....................:Hola", nombre, "Bienvenido(a) a Rio:........................")
print("el juego de un emocionante viaje por un río en medio de una exuberante jungla.\nEl jugador asume el papel de un aventurero que navega en una canoa por el río\ny se enfrentan a una serie de desafíos en búsqueda de un antiguo tesoro\nescondido en lo profundo de la selva.")
print("")
print(".................................:Capítulo 1:..................................")
print(nombre, "es momento de elegir tu rumbo: ¿Hacia la derecha o izquierda?")

ruta1 = 0; 
# ruta2 = 0; ruta3 = 0; ruta4 = 0; ruta5 = 0

while ruta1 == 0:
    rumbo = input("Digita tu decisión (derecha o izquierda): ")
    if rumbo == "izquierda":
        print("Has elegido la puerta izquierda.")            
        print("¡Felicidades!", nombre, "Continúas por una corriente de agua tranquila.")
        ruta1 +=1

        print("")
        print(".................................:Capítulo 2:..................................")
        print("en el recorrido encuentras un grupo de monos salvajes en las ramas de un arbol\nsobre el rio debes tomar una decisión\n")

        ruta2 = 0
        while ruta2 == 0:
            elegir = input("1. pelear\n2. interactúa con los monos\n3. pasar sigilosamente\n¿Qué opción eliges?: ")           
            if elegir == "3":
                print("Haz elegido pasar sigilosamente")
                print(nombre, "Lo lograste no te han visto y continúas ")
                ruta2 +=1

                print("")
                print(".................................:Capítulo 3:..................................")
                print("El río se divide en dos caminos, uno parece más corto pero más peligroso,\nmientras que el otro es más largo pero parece más peligroso")

                ruta3 = 0
                while ruta3 == 0:
                    rio = input("¿Cuál río deseas elegir? (largo ó corto): ")
                    if rio == "corto":
                        print("Haz elegido la opción corto")
                        print(nombre, "Muy bién estás muy cerca de lograr encontrar el tesoro")
                        ruta3 +=1

                        print("")
                        print(".................................:Capítulo 3:..................................")
                        print("estás muy cerca de encontrar el tesoro\nEn la parada en la orilla eres picado por unos abejones benenosos, para buscar\nel antídoto debes elegir entre tres plantas")

                        ruta4 = 0
                        while ruta4 == 0:
                            color = input("Elige el color de la planta para preparar el antídoto.\n(roja, azul ó verde): ")
                            if color == "verde":
                                print("Haz elegido la planta color verde")
                                print("!Enhorabuena¡", nombre, ", elegiste la planta correcta")
                                ruta4 +=1

                                print("")
                                print(".................................:Capítulo 4:..................................")
                                print("Finalmente", nombre, "Llegaste a la unicación del tesoro, debes decidir si excavar o seguir rastreando")

                                ruta5 = 0
                                while ruta5 == 0:
                                    decide = input("¿Qué deseas hacer rastrear ó excavar?: ")
                                    print("")
                                    if decide == "excavar":
                                        print("Haz elegido excavar")
                                        print("!FELICITACIONES¡", nombre,"\nEncontraste el tesoro perdido\nFin del juego")
                                        ruta5 +=1
                                    elif decide == "rastrear":
                                        print("Has elegido rastrear.")
                                        print(nombre, "en el recorrido encontraste un agujero y haz muerto") 
                                        break
                                    else:
                                        print("Esa no es una opción válida. Debes elegir 'excavar ó rastrear'.")     

                            elif color == "roja":
                                print("Has elegido la planta color roja.")
                                print("la planta no ha funcionado y no te salvaste", nombre)
                                break
                            elif color == "azul":
                                print("Has elegido la planta color azul.")
                                print(nombre, "Es una planta tóxica y haz muerto")    
                                break
                            else:
                                print("Esa no es una opción válida. Debes elegir 'verde, azul ó roja'.")  

                    elif rio == "largo":
                        print("Has elegido la opción largo.")
                        print(nombre, "Fuiste devorado por una feroz anaconda") 
                    else:
                        print("Esa no es una opción válida. Debes elegir 'largo ó corto'.")        

            elif elegir == "1":
                print("Has elegido pelear con los monos.")
                print(nombre, "Son muchos y te han acabado")
                break
            elif elegir == "2":
                print("Has elegido interactuar.")
                print(nombre, "Los monos son poco amigables y te han atacado ")
                break   
            else:
                 print("Esa no es una opción válida. Debes elegir '1, 2 ó 3'.") 

    elif rumbo == "derecha":
        print("Has elegido la puerta derecha.")
        print(nombre, "Oh no, caíste en una cascada muy alta.")
        break 
    else:
        print("Esa no es una opción válida. Debes elegir 'izquierda' o 'derecha'.") 
         










































































































