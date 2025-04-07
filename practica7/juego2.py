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

    def validaNumero(self, numero):
        return 0 <= numero <= 10

    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)
        while True:
            intento = int(input("Adivina un número entre 0 y 10: "))
            if not self.validaNumero(intento):
                print("Número inválido. Debe estar entre 0 y 10.")
                continue
            if intento == self.numeroAAdivinar:
                print("¡Acertaste!")
                self.actualizaRecord()
                break
            elif self.quitaVida():
                pista = "mayor" if intento < self.numeroAAdivinar else "menor"
                print(f"Incorrecto. El número es {pista}. Te quedan {self.numeroDeVidas} vidas.")
            else:
                print("No te quedan más vidas. Fin del juego.")
                break


class JuegoAdivinaPar(JuegoAdivinaNumero):
    def validaNumero(self, numero):
        if 0 <= numero <= 10 and numero % 2 == 0:
            return True
        print("Número inválido. Debe ser PAR y estar entre 0 y 10.")
        return False


class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def validaNumero(self, numero):
        if 0 <= numero <= 10 and numero % 2 == 1:
            return True
        print("Número inválido. Debe ser IMPAR y estar entre 0 y 10.")
        return False


class Aplicacion:
    @staticmethod
    def main():
        juegos = [JuegoAdivinaNumero(3), JuegoAdivinaPar(3), JuegoAdivinaImpar(3)]
        for juego in juegos:
            juego.juega()


if __name__ == "__main__":
    Aplicacion.main()
