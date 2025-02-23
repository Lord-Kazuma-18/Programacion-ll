public class Linea {
    static class Punto {
        float x, y;
        Punto(float x, float y) { this.x = x; this.y = y; }
        public String toString() { return "(" + x + ", " + y + ")"; }
    }

    Punto inicio, fin;

    Linea(float x1, float y1, float x2, float y2) {
        inicio = new Punto(x1, y1);
        fin = new Punto(x2, y2);
    }

    public String toString() { return "Línea de " + inicio + " a " + fin; }

    void dibujar() { System.out.println("Dibujando " + this); }

    public static void main(String[] args) {
        Linea linea = new Linea(1, 2, 3, 4);
        System.out.println(linea);
        linea.dibujar();
    }
}
