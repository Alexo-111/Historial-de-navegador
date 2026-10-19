class Pila:
    def __init__(self):
        self.items = []

    def push(self, elemento):
        self.items.append(elemento)

    def pop(self):
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        return self.items.pop()

    def peek(self):
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        return self.items[-1]

    def esta_vacia(self):
        return len(self.items) == 0

    def vaciar(self):
        self.items = []


class Navegador:
    def __init__(self):
        self.actual = None
        self.pila_atras = Pila()
        self.pila_adelante = Pila()

    def visitar(self, sitio):
        if self.actual is not None:
            self.pila_atras.push(self.actual)
        self.actual = sitio
        self.pila_adelante.vaciar()  
        print(f"Visitando: {self.actual}")

    def atras(self):
        if self.pila_atras.esta_vacia():
            print("No hay páginas anteriores.")
            return
        self.pila_adelante.push(self.actual)
        self.actual = self.pila_atras.pop()
        print(f"Regresaste a: {self.actual}")

    def adelante(self):
        if self.pila_adelante.esta_vacia():
            print("No hay páginas siguientes.")
            return
        self.pila_atras.push(self.actual)
        self.actual = self.pila_adelante.pop()
        print(f"Avanzaste a: {self.actual}")

    def mostrar_historial(self):
        print("\n--- Historial ---")
        print("Atrás (más reciente primero):", list(reversed(self.pila_atras.items)))
        print("Página actual:", self.actual)
        print("Adelante (siguiente primero):", list(reversed(self.pila_adelante.items)))


def main():
    navegador = Navegador()
    while True:
        print("\n=== Navegador web ===")
        print("1. Visitar sitio")
        print("2. Atrás")
        print("3. Adelante")
        print("4. Ver historial")
        print("5. Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            sitio = input("Escribe la URL: ").strip()
            if sitio:
                navegador.visitar(sitio)
            else:
                print("La URL no puede estar vacía.")
        elif opcion == "2":
            navegador.atras()
        elif opcion == "3":
            navegador.adelante()
        elif opcion == "4":
            navegador.mostrar_historial()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()