import random
from abc import ABC, abstractmethod

class Personaje(ABC):
    def __init__(self, nombre, ciudad):
        self.nombre = nombre
        self.ciudad = ciudad
        self._vida = 100 

    @property
    def vida(self):
        return self._vida

    @abstractmethod
    def realizar_accion(self):
        pass


class Civil(Personaje):
    def __init__(self, nombre, ciudad, trabajo):
        super().__init__(nombre, ciudad)
        self.trabajo = trabajo

    def realizar_accion(self):
        return f"El civil {self.nombre} está trabajando de {self.trabajo} en las calles de {self.ciudad}."


class Policia(Personaje):
    def __init__(self, nombre, city, rango):
        super().__init__(nombre, city)
        self.rango = rango

    def realizar_accion(self):
        return f"El {self.rango} {self.nombre} patrulla {self.ciudad} buscando criminales."


class Auto:
    def __init__(self, modelo, color):
        self.modelo = modelo
        self.color = color


class Mision:
    def __init__(self, nombre_mision, pago):
        self.nombre_mision = nombre_mision
        self.pago = pago


class JuegoGTA:
    def __init__(self):
        self.lista_personajes = []
        self.billetera = 500  

    def iniciar(self):
        self.lista_personajes.append(Civil("Niko", "Los Santos", "Taxista"))
        self.lista_personajes.append(Policia("Tenpenny", "Los Santos", "Sargento"))

        while True:
            print("\n==== MENÚ MINI GTA ====")
            print("1. Registrar Personaje")
            print("2. Mostrar Personajes")
            print("3. Hacer una Misión")
            print("4. Salir")
            print("=======================")
            
            opcion = input("Elige una opción (1-4): ")

            if opcion == "1":
                self.registrar()
            elif opcion == "2":
                self.mostrar()
            elif opcion == "3":
                self.jugar_mision()
            elif opcion == "4":
                print("\n¡Cerrando el juego!")
                break
            else:
                print("\nOpción no válida.")

    def registrar(self):
        print("\n--- REGISTRAR PERSONAJE ---")
        tipo = input("Tipo (1: Civil / 2: Policía): ")
        nombre = input("Nombre: ")
        ciudad = input("Ciudad: ")

        if tipo == "1":
            trabajo = input("Trabajo: ")
            self.lista_personajes.append(Civil(nombre, ciudad, trabajo))
            print("¡Civil guardado!")
        elif tipo == "2":
            rango = input("Rango: ")
            self.lista_personajes.append(Policia(nombre, ciudad, rango))
            print("¡Policía guardado!")
        else:
            print("Tipo no válido.")

    def mostrar(self):
        print("\n--- LISTA DE PERSONAJES ---")
        if not self.lista_personajes:
            print("No hay nadie registrado.")
            return

        for p in self.lista_personajes:
            print(f"- Nombre: {p.nombre} | Vida: {p.vida}% | Ubicación: {p.ciudad}")
            print(f"  Acción: {p.realizar_accion()}")

    def jugar_mision(self):
        print("\n--- PANEL DE MISIONES ---")
        print(f"Dinero: ${self.billetera}")
        
        mision_actual = Mision("Robar la Tienda del Barrio", 800)
        print(f"Misión: {mision_actual.nombre_mision} | Paga: ${mision_actual.pago}")
        
        confirmar = input("¿Aceptar misión? (si / no): ").lower()
        if confirmar == "si":
            if random.choice([True, False]):
                self.billetera += mision_actual.pago
                print(f"¡Éxito! Ganaste ${mision_actual.pago}")
            else:
                self.billetera -= 200
                print("¡Fallaste! Perdiste $200.")
            print(f"Saldo actual: ${self.billetera}")
        else:
            print("Misión cancelada.")


if __name__ == "__main__":
    juego = JuegoGTA()
    juego.iniciar()