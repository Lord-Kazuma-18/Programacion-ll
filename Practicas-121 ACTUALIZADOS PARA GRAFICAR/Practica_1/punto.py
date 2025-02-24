import math
import matplotlib.pyplot as plt

class Punto:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def coord_cartesianas(self):
        return (self.x, self.y)

    def coord_polares(self):
        r = math.sqrt(self.x ** 2 + self.y ** 2)
        theta = math.atan2(self.y, self.x)
        return (r, theta)

    def graficar(self):
        fig, ax = plt.subplots()
        ax.scatter(self.x, self.y, color='red', label=f'P({self.x}, {self.y})')
        ax.axhline(0, color='black', linewidth=0.5)
        ax.axvline(0, color='black', linewidth=0.5)
        ax.grid(True, linestyle='--', linewidth=0.5)
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.legend()
        plt.show()

    def __str__(self):
        return f"Punto({self.x}, {self.y})"

p = Punto(3, 4)
print("Coordenadas Cartesianas:", p.coord_cartesianas())
print("Coordenadas Polares:", p.coord_polares())
print("Representación del Punto:", p)
p.graficar()
