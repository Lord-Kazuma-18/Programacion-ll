public class Punto {
    float x;
    float y;

    Punto(float a, float b) {
        this.x = a;
        this.y = b;
    }

    float[] obtenerCartesiano() {
        float[] c = new float[2];
        c[0] = x;
        c[1] = y;
        return c;
    }

    double[] obtenerPolar() {
        double[] p = new double[2];
        p[0] = Math.sqrt(x * x + y * y);
        p[1] = Math.atan2(y, x);
        return p;
    }

    public String toString() {
        return "Coordenadas: " + x + " , " + y;
    }

    public static void main(String[] args) {
        Punto p;
        p = new Punto(3, 4);

        float[] cart = p.obtenerCartesiano();
        System.out.println("Cartesiano: " + cart[0] + " , " + cart[1]);

        double[] polar = p.obtenerPolar();
        System.out.println("Polar: r= " + polar[0] + " , θ= " + polar[1]);

        System.out.println(p.toString());
    }
}
