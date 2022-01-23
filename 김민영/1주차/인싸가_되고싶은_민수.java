package 비타알고;


import java.util.Scanner;

public class 인싸가되고싶은민수 {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        if(a!=b){
            System.out.println(2);
        }
        else{
            for(int i=2; i<=a; i++){
                if(a%i==0){
                    System.out.println(i);
                    break;
                }
            }
        }
    }
}
