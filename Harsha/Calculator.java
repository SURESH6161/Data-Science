package Harsha;
import java.util.*;

import java.util.Scanner;
public class Calculator {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int choice;
        do {
            System.out.println("1 to addition");
            System.out.println("2 to subtraction");
            System.out.println("3 to mulitplication");
            System.out.println("4 to divison");
            System.out.println("5 to exit");
            System.out.println("Enter a choice : ");
            choice = sc.nextInt();
            if (choice >= 1 && choice <= 4) {
                System.out.println("Enter first num1");
                Double num1 = sc.nextDouble();
                System.out.println("Enter first num2");
                Double num2 = sc.nextDouble();
                switch (choice) {
                    case 1:
                        System.out.println("Result" + (num1 + num2));
                        break;
                    case 2:
                        System.out.println("Result" + (num1 - num2));
                        break;
                    case 3:
                        System.out.println("Result" + (num1 * num2));
                        break;
                    case 4:
                        if (num2 != 0) {
                            System.out.println("Result" + (num1 / num2));
                        } else {
                            System.out.println("error in because of zero");
                        }
                        break;
                }
            } else if (choice != 5) {
                System.out.println("Invalid choice");
            }
        } while (choice != 5);
        sc.close();
    }
}