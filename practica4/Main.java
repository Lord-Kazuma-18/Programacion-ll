public class Main {
    public static void main(String[] args) {
        FiguraGeometrica figura = new FiguraGeometrica();

        System.out.println("Área del círculo: " + figura.area(5));
        System.out.println("Área del rectángulo: " + figura.area(4, 6));
        System.out.println("Área del triángulo: " + figura.area(3, 8, true));
        System.out.println("Área del trapecio: " + figura.area(3, 6, 4, 0));
        System.out.println("Área del pentágono: " + figura.area(5, 3, 5, true));
        System.out.println("Longitud de la recta: " + figura.area(1, 1, 4, 5, true));
    }
}
