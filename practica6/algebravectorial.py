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
    
    def es_perpendicular_a(self, other):
        return np.dot(self.vector, other.vector) == 0
    
    def es_mutuamente_ortogonal(self, other):
        return np.linalg.norm(self.vector + other.vector) == np.linalg.norm(self.vector - other.vector)
    
    def ortogonalidad_por_producto(self, other):
        return np.dot(self.vector, other.vector) == 0
    
    def ortogonalidad_por_norma(self, other):
        return np.linalg.norm(self.vector + other.vector) ** 2 == self.modulo() ** 2 + other.modulo() ** 2
    
    def es_paralelo_a(self, other):
        return np.cross(self.vector, other.vector).sum() == 0
    
    def proyeccion_sobre(self, other):
        return (np.dot(self.vector, other.vector) / np.dot(other.vector, other.vector)) * other.vector
    
    def componente_en(self, other):
        return (np.dot(self.vector, other.vector) / np.linalg.norm(other.vector)) * (other.vector / np.linalg.norm(other.vector))
    
vector_a = list(map(float, input("Ingrese valores para vector a").split()))
vector_b = list(map(float, input("Ingrese valores para vector b").split()))

a = AlgebraVectorial(vector_a)
b = AlgebraVectorial(vector_b)

print("¿a es perpendicular a b?", a.es_perpendicular_a(b))
print("¿a es mutuamente ortogonal a b?", a.es_mutuamente_ortogonal(b))
print("¿a es ortogonal a b por producto?", a.ortogonalidad_por_producto(b))
print("¿a es ortogonal a b por norma?", a.ortogonalidad_por_norma(b))
print("¿a es paralelo a b?", a.es_paralelo_a(b))
print("Proyección de a sobre b:", a.proyeccion_sobre(b))
print("Componente de a en b:", a.componente_en(b))
