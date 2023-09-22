class Juego:
    def __init__(self):
        '''
        Constructor de la clase Juego. Inizializa las variables de la instancia
        '''
        self.nombre = ""
        self.capitulo = 1

    def mostrar_mensaje(self, mensaje):
        '''
        Muestra un mensaje en la consola.
        Args:
            mensaje (str): El mensaje a mostrar.
        '''
        print(mensaje)

    def obtener_decision(self, opciones):
        '''
        Permite al jugador elegir una opción de la lista de opciones.
        Args:
            opciones (list): Una lista de cadenas que representa las opciones disponibles.
        Returns:
            str: la opción elegida por el jugador    
        '''
        while True:
            eleccion = input("Elige una opción: " + " / ".join(opciones) + ": ").lower()
            if eleccion in opciones:
                return eleccion
            else:
                self.mostrar_mensaje("Opción no válida. Inténtalo de nuevo.")

    def capitulo1(self):
        '''
        Capítulo 1 del juego. El jugador debe tomar una decisión al comienzo del juego.
        '''
        self.mostrar_mensaje(f"Es momento de elegir tu rumbo, {self.nombre}: ¿Hacia la derecha o izquierda?")
        eleccion = self.obtener_decision(["derecha", "izquierda"])

        if eleccion == "izquierda":
            self.mostrar_mensaje(f"¡Felicidades, {self.nombre}! Continúas por una corriente de agua tranquila.\n")
            self.capitulo += 1
            self.capitulo2()
        else:
            self.mostrar_mensaje(f"Oh no, {self.nombre}, caíste en una cascada muy alta.")
            self.finalizar_juego()

    def capitulo2(self):
            '''
            Capítulo 2 del juego: El jugador se encuentra con monos salvajes y debe tomar una decisión.
            '''
            self.mostrar_mensaje("En el recorrido encuentras un grupo de monos salvajes en las ramas de un árbol sobre el río. Debes tomar una decisión.")    

            eleccion = self.obtener_decision(["pelear", "interactuar", "pasar sigilosamente"])
            if eleccion == "pasar sigilosamente":
                self.mostrar_mensaje(f"{self.nombre}, lo lograste. No te han visto y continúas.\n")
                self.capitulo += 1
                self.capitulo3()

            else:
                self.mostrar_mensaje(f"Has elegido {eleccion}. Los monos reaccionan y te atacan. ¡Te han derrotado!")
                self.finalizar_juego()

    def capitulo3(self):
        '''
        Capítulo 3 del juego. El jugador debe elegir entre dos caminos en el río.
        '''
        self.mostrar_mensaje("El río se divide en dos caminos uno parece más corto pero peligroso, mientras que el otro es más largo pero parece más seguro.")

        eleccion = self.obtener_decision(["corto", "largo"])
        if eleccion == "corto":
            self.mostrar_mensaje("Has elegido el camino corto. Estás muy cerca de encontrar el tesoro.\n")
            self.capitulo += 1
            self.capitulo4()
        else:
            self.mostrar_mensaje(f"Has elegido el camino largo, {self.nombre}. De repente, una acaconda feroz te atrapa y termina tu aventura.")
            self.finalizar_juego()    

    def capitulo4(self):
        '''
        Capítulo 4 del juego. El jugador debe encontrar un antídoto entre tres plantas.
        '''
        self.mostrar_mensaje(f"Estás muy cerca de encontrar el tesoro, {self.nombre}.")
        self.mostrar_mensaje("En la parada en la orilla, eres picado por unos abejones venenosos. Para buscar el antídoto, debes elegir entre tres plantas.")

        eleccion = self.obtener_decision(["roja", "azul", "verde"])
        if eleccion == "verde":
            self.mostrar_mensaje("Has elegido la planta color verde. ¡Enhorabuena! Elegiste la planta correcta.\n")
            self.capitulo += 1
            self.capitulo5()
        else:
            self.mostrar_mensaje("La planta que elegiste no funcionó y no te salvaste. Tu aventura termina aquí.")    
            self.finalizar_juego()

    def capitulo5(self):
        '''
        Capítulo 5 del juego. El jugador debe decidir si excavar en busca del tesoro o seguir rastreando.
        '''
        self.mostrar_mensaje(f"Finalmente, {self.nombre}, llegaste a la ubicación del tesoro. Debes decidir si excavar o seguir rastreando.")

        eleccion = self.obtener_decision(["excavar", "rastrear"])
        if eleccion == "excavar":
            self.mostrar_mensaje("Has elegido excavar. ¡FELICITACIONES! Encontraste el tesoro perdido. Fin del juego.")
            self.finalizar_juego()
        else:
            self.mostrar_mensaje("Has elegido rastrear, {self.nombre}. En el recorrido encontraste un agujero y lamentablemente, has muerto.")
            self.finalizar_juego()    

    def finalizar_juego(self):
        '''
        Finaliza el juego y muestra un mensaje de despedida.
        '''
        self.mostrar_mensaje("Fin del juego. ¡Gracias por jugar!")

    def iniciar_juego(self):
        '''
        Da inicio al juego solicitando el nombre del jugador y comienza el primer capítulo.
        '''
        self.nombre = input("Para comenzar el juego, escribe tu nombre: ")
        self.mostrar_mensaje(f"Bienvenido(a), {self.nombre}, al emocionante viaje por un río en medio de una exuberante jungla.")
        self.capitulo1()

if __name__ == "__main__":
    juego = Juego()
    juego.iniciar_juego()        