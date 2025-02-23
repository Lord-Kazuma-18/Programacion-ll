class Punto:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return f"({self.x}, {self.y})"

class Circulo:
    def __init__(self, x, y, r):
        self.centro = Punto(x, y)
        self.radio = r

    def __str__(self):
        return f"Círculo en {self.centro} con radio {self.radio}"

    def dibujar(self):
        print(f"Dibujando {self}")

circulo = Circulo(5, 10, 3.5)
print(circulo)
circulo.dibujar()
