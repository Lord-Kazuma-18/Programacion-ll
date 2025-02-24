import javax.swing.*;
import java.awt.*;

public class Linea extends JPanel {
    float x1, y1, x2, y2;

    Linea(float x1, float y1, float x2, float y2) {
        this.x1 = x1 * 50; // Escalamos para que se vea bien
        this.y1 = y1 * 50;
        this.x2 = x2 * 50;
        this.y2 = y2 * 50;
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.drawLine((int)x1, (int)y1, (int)x2, (int)y2);
    }

    public static void main(String[] args) {
        JFrame ventana = new JFrame("Línea");
        ventana.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        ventana.setSize(300, 300);
        ventana.add(new Linea(1, 2, 3, 4)); // Definir la línea
        ventana.setVisible(true);
    }
}
