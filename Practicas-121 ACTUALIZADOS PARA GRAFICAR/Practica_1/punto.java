import javax.swing.*;
import java.awt.*;

class Punto {
    float x, y;

    Punto(float a, float b) {
        this.x = a; this.y = b;
    }

    float[] obtenerCartesiano() { return new float[]{x, y}; }
    double[] obtenerPolar() { return new double[]{Math.hypot(x, y), Math.atan2(y, x)}; }
    public String toString() { return "Coordenadas: " + x + " , " + y; }

    void graficar() {
        JFrame frame = new JFrame("Gráfico");
        frame.setSize(400, 400);
        frame.add(new JPanel() {
            protected void paintComponent(Graphics g) {
                int cX = getWidth() / 2, cY = getHeight() / 2, esc = 50;
                g.drawLine(cX, 0, cX, getHeight());
                g.drawLine(0, cY, getWidth(), cY);
                g.setColor(Color.RED);
                g.fillOval(cX + (int) (x * esc) - 5, cY - (int) (y * esc) - 5, 10, 10);
            }
        });
        frame.setVisible(true);
    }

    public static void main(String[] args) {
        Punto p = new Punto(3, 4);
        System.out.println("Cartesiano: " + p.obtenerCartesiano()[0] + " , " + p.obtenerCartesiano()[1]);
        System.out.println("Polar: r= " + p.obtenerPolar()[0] + " , θ= " + p.obtenerPolar()[1]);
        System.out.println(p);
        p.graficar();
    }
}