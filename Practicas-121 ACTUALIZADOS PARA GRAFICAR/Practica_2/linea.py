import matplotlib.pyplot as plt

class Figura:
    def graficar(self, ax):
        ax.axhline(0, color='black', linewidth=0.5)
        ax.axvline(0, color='black', linewidth=0.5)
        plt.grid()

class Linea(Figura):
    def __init__(self, x1, y1, x2, y2): self.p1, self.p2 = (x1, y1), (x2, y2)
    def graficar(self):
        fig, ax = plt.subplots()
        super().graficar(ax)
        ax.plot(*zip(self.p1, self.p2), 'r-')
        plt.show()

for f in [Linea(1, 2, 3, 4)]: f.graficar()
