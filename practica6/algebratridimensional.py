import numpy as np

class AlgebraVectorial:
    def __init__(self, vector):
        self.vector = np.array(vector, dtype=float)
    
    def __add__(self, other):
        return AlgebraVectorial(self.vector + other.vector)
    
    def __sub__(self, other):
        return AlgebraVectorial(self.vector - other.vector)
    
    def modulo(self):
        return np.linalg.norm(self.vector)
    
    def normalizar(self):
        return self.vector / self.modulo() if self.modulo() != 0 else self.vector
    
    def producto_escalar(self, other):
        return np.dot(self.vector, other.vector)
    
    def producto_vectorial(self, other):
        return np.cross(self.vector, other.vector)
    
    def __repr__(self):
        
        return f"Vector: {self.vector}"


def ingresar_vector(nombre):
    print(f"Ingrese las componentes del vector {nombre} (separadas por espacios):")
    componentes = list(map(float, input().split()))
    return AlgebraVectorial(componentes)

a = ingresar_vector("a")
b = ingresar_vector("b")

print(f"Suma: {a + b}.")
print(f"Resta: {a - b}.")
print(f"Modulo de a: {a.modulo()}.")
print(f"Vector normalizado de a: {a.normalizar()}.")
print(f"Producto escalar: {a.producto_escalar(b)}.")
print(f"Producto vectorial: {a.producto_vectorial(b)}.")


