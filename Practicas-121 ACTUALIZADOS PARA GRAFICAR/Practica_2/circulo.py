import matplotlib.pyplot as plt

class Circulo:
    def __init__(self, x, y, r):
        self.x, self.y, self.r = x, y, r

    def __str__(self):
        return f"Círculo en ({self.x}, {self.y}) con radio {self.r}"

    def graficar(self):
        fig, ax = plt.subplots()
        ax.set_aspect('equal')
        ax.set_xlim(self.x - self.r - 1, self.x + self.r + 1)
        ax.set_ylim(self.y - self.r - 1, self.y + self.r + 1)
        ax.axhline(0, color='black', linewidth=0.5)
        ax.axvline(0, color='black', linewidth=0.5)
        ax.add_patch(plt.Circle((self.x, self.y), self.r, color='blue', fill=False))
        plt.grid()
        plt.show()

c = Circulo(5, 10, 3.5)
print(c)
c.graficar()