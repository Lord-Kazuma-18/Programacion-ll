import javax.swing.*;
import java.awt.*;

class Circulo {
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

    void graficar() {
        JFrame frame = new JFrame("Gráfico");
        frame.setSize(400, 400);
        frame.add(new JPanel() {
            protected void paintComponent(Graphics g) {
                int cX = getWidth() / 2, cY = getHeight() / 2, esc = 50;
                g.drawLine(cX, 0, cX, getHeight());
                g.drawLine(0, cY, getWidth(), cY);
                g.setColor(Color.BLUE);
                g.drawOval(cX + centro.x * esc - (int)(radio * esc), cY - centro.y * esc - (int)(radio * esc), (int)(radio * 2 * esc), (int)(radio * 2 * esc));
            }
        });
        frame.setVisible(true);
    }

    public static void main(String[] args) {
        Circulo c = new Circulo(5, 10, 3.5f);
        System.out.println(c);
        c.graficar();
    }
}
