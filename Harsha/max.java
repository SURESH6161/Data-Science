package Harsha;

public class max {
    public static void main(String[] args) {

        int a = 5;
        int b = 10;

        int max = (a + b + Math.abs(a - b)) / 2;
        int min = (a + b - Math.abs(a - b)) / 2;

        System.out.println("max is " + max);
        System.out.println("min is " + min);

        for (;;) {
            System.out.println("hi");

        }
    }
}
