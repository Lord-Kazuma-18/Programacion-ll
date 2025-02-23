package Practica_2;

public class Circulo {
    static class Punto {
        int x, y;
        Punto(int x, int y) { this.x = x; this.y = y; }
        public String toString() { return "(" + x + "," + y + ")"; }
    }

    Punto centro;
    float radio;

    Circulo(int x, int y, float r) {
        centro = new Punto(x, y);
        radio = r;
    }

    public String toString() { return "Círculo en " + centro + " con r=" + radio; }

    void dibujar() { System.out.println("Dibujando " + this); }

    public static void main(String[] args) {
        Circulo c = new Circulo(5, 10, 3.5f);
        System.out.println(c);
        c.dibujar();
    }
}
