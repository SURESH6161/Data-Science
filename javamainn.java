import java.util.*;

class javamainn {
        public static void main(String[] args) {
                Scanner sc = new Scanner(System.in);

                // Strong Number
                // int n=sc.nextInt();
                // int num1=n;
                // int sum=0;
                // while (n!=0){
                // int num=n%10;
                // int fact=1;
                // for(int i=1;i<=num;i++)
                // {
                // fact=fact*i;
                // }
                // sum+=fact;
                // n = n/10;
                // }
                // if(sum==num1) {
                // System.out.println("Strong Number");
                // }
                // else{
                // System.out.println("Not Strong Number");
                // }

                // reverse the array
                // int []arr={1,2,3,4,5,6,7,8,9};
                // for(int i=arr.length-1;i>=0;i--)
                // {
                // System.out.print(arr[i]);
                // }

                // Ass order
                // int []arr1={2,44,66,84,231,22,45,78,9,21};
                // int arr2[]= new int[arr1.length];
                // int temp=0;
                // for(int i=0;i<arr1.length;i++)
                // {
                // for(int j=i+1;j<arr1.length;j++)
                // {
                // if(arr1[i]>arr1[j])
                // {
                // temp=arr1[i];
                // arr1[i]=arr1[j];
                // arr1[j]=temp;
                // }
                // }
                // }
                // for(int i:arr1)
                // {
                // System.out.print(i+" ");
                // }

                // Odd and even
                // int ar[]={2,3,4,5,6,7,8};
                // for(int i=0;i<ar.length;i++)
                // {
                // if(ar[i]%2==0) System.out.print(ar[i]);
                // }
                // System.out.println();
                // for(int i=0;i<ar.length;i++)
                // {
                // if(ar[i]%2!=0) System.out.print(ar[i]);
                // }

                // Max And min

                int array[] = { 12, 23, 3, 44, 56, 778, 90 };
                int max = array[0];
                int min = array[0];
                int secmin = 9999;
                int secmax = 0;
                for (int i = 1; i < array.length; i++) {
                        if (max < array[i])
                                max = array[i];
                        if (min > array[i])
                                min = array[i];

                }
                System.out.println(min);
                System.out.println(max);

                // second largest and second minimum

                for (int i = 0; i < array.length; i++) {
                        if (array[i] > secmax && array[i] < max)
                                secmax = array[i];
                        if (array[i] < secmin && array[i] > min)
                                secmin = array[i];
                }
                System.out.println(secmax);
                System.out.println(secmin);

                sc.close();
        }
}
