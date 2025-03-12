public class FiguraGeometrica {

    public double area(double radio) {
        
        return Math.PI * Math.pow(radio, 2);
    }

    public double area(double ancho, double alto) {
        
        return ancho * alto;
    }

    public double area(double base, double altura, boolean Triangulo) {
        
        return (base * altura) / 2;
    }

    public double area(double baseMenor, double baseMayor, double altura, int Trapecio) {
        
        return ((baseMenor + baseMayor) * altura) / 2;
    }

    public double area(double lado, double apotema, int lados, boolean Pentagono) {
        
        double perimetro = lado * lados;
        return (perimetro * apotema) / 2;
    }

    public double area(double puntoX1, double puntoY1, double puntoX2, double puntoY2, boolean Recta) {
        
        return Math.sqrt(Math.pow(puntoX2 - puntoX1, 2) + Math.pow(puntoY2 - puntoY1, 2));
    }
}