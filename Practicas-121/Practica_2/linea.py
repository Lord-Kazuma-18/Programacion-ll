class Punto:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return f"({self.x}, {self.y})"

class Linea:
    def __init__(self, x1, y1, x2, y2):
        self.p1, self.p2 = Punto(x1, y1), Punto(x2, y2)

    def __str__(self):
        return f"Línea de {self.p1} a {self.p2}"

    def dibujar(self):
        print(f"Dibujando {self}")

if __name__ == "__main__":
    linea = Linea(0, 0, 5, 5)
    print(linea)
    linea.dibujar()
