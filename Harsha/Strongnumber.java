package Harsha;

import java.util.Scanner;;

public class Strongnumber {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int n = sc.nextInt();
        int number = n;
        int sum = 0;

        while (n != 0) {
            int remainder = n % 10;
            int fact = 1;

            for (int i = 1; i <= remainder; i++) {
                fact = fact * i;
            }
            sum += fact;
            n = n / 10;
        }
        if (sum == number) {
            System.out.println("The number is strong number");
        } else {
            System.out.println("the number is not a strong number");
        }

        sc.close();
    }
}
