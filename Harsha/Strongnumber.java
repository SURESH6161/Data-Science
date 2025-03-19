package Harsha;

import java.util.Scanner;;

public class Strongnumber {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int number = n;
        int sum = 0;

        while (n != 0) {
            int remainder = n % 10;
            int fact = 1;

            for (int i = 0; i <= remainder; i++) {
                fact = fact * i;
            }
            sum += fact;
            n = n / 10;
      }
if(sum==number){
    System.out.println("the number is strong number");
}
else{
    System.out.println("the number is not a strong number");
}
    }
}
