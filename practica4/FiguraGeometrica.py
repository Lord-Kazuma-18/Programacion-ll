import math

class FiguraGeometrica:

    def area(self, *args):
        if len(args) == 1 and isinstance(args[0], (int, float)):
            
            radio = args[0]
            return math.pi * radio ** 2
        elif len(args) == 2 and all(isinstance(arg, (int, float)) for arg in args):
        
            ancho, alto = args
            return ancho * alto
        elif len(args) == 3 and isinstance(args[2], str) and args[2] == 'triangulo':
            
            base, altura, _ = args
            return (base * altura) / 2
        elif len(args) == 3:
            
            base_menor, base_mayor, altura = args
            return ((base_menor + base_mayor) * altura) / 2
        elif len(args) == 4 and isinstance(args[2], str) and args[2] == 'pentagono':
            
            lado, apotema, _, _ = args
            perimetro = lado * 5
            return (perimetro * apotema) / 2
        elif len(args) == 2 and all(isinstance(arg, tuple) and len(arg) == 2 for arg in args):
            
            (x1, y1), (x2, y2) = args
            return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        else:
            raise NotImplementedError("Parámetros insuficientes o incorrectos")

figura = FiguraGeometrica()

print("Área del círculo: ", figura.area(5.0))
print("Área del rectángulo: ", figura.area(4, 6))
print("Área del triángulo: ", figura.area(3, 8, 'triangulo'))
print("Área del trapecio: ", figura.area(3, 6, 4))
print("Área del pentágono: ", figura.area(5, 3, 'pentagono', 'extra'))
print("Longitud de la recta: ", figura.area((1, 1), (4, 5)))
