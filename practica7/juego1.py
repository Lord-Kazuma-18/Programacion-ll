import random

class Juego:
    def __init__(self):
        self.numeroDeVidas = 0
        self.record = 0

    def reiniciaPartida(self):
        self.numeroDeVidas = self.vidasIniciales

    def actualizaRecord(self):
        if self.numeroDeVidas > self.record:
            self.record = self.numeroDeVidas

    def quitaVida(self):
        self.numeroDeVidas -= 1
        return self.numeroDeVidas > 0


class JuegoAdivinaNumero(Juego):
    def __init__(self, numeroDeVidas):
        super().__init__()
        self.vidasIniciales = numeroDeVidas
        self.numeroAAdivinar = 0

    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)

        while True:
            intento = int(input("Adivina un número entre 0 y 10: "))
            if intento == self.numeroAAdivinar:
                print("¡Acertaste!")
                self.actualizaRecord()
                break
            else:
                if self.quitaVida():
                    mensaje = "mayor" if intento < self.numeroAAdivinar else "menor"
                    print(f"Incorrecto. El número es {mensaje}. Te quedan {self.numeroDeVidas} vidas.")
                else:
                    print("No te quedan más vidas. Fin del juego.")
                    break


class Aplicacion:
    @staticmethod
    def main():
        juego = JuegoAdivinaNumero(numeroDeVidas=3)
        juego.juega()


# Solo se ejecuta si se llama este archivo directamente
if __name__ == "__main__":
    Aplicacion.main()
