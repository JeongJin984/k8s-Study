package 비타알고;

import java.util.Scanner;

public class A4용지를_만들자 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();

        int answer;

        int width = (n/20) * (m/40);

        int hight = (n/40) * (m/20);

        int intersection = 2*((n/40) *(m/40));

        answer = width+hight-intersection;
        System.out.println(answer);


    }
}