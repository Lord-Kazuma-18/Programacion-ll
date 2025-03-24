import math

class Estadisticas:
    def __init__(self, numeros):
        self.numeros = numeros

    def promedio(self):
        return round(sum(self.numeros) / len(self.numeros), 2)

    def desviacion(self):
        promedio_valor = self.promedio()
        suma_cuadrados = sum((valor - promedio_valor) ** 2 for valor in self.numeros)
        return round(math.sqrt(suma_cuadrados / (len(self.numeros) - 1)), 5)

numeros = list(map(float, input("Introduce exactamente 10 números separados por espacio: ").split()))

if len(numeros) != 10:
    print("Error: Se requieren exactamente 10 números.")
else:
    stats = Estadisticas(numeros)
    print(f"Promedio: {stats.promedio()}")
    print(f"Desviación estándar: {stats.desviacion()}")
