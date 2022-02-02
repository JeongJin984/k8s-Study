package 비타알고;
import java.util.Scanner;

public class 여름의_대삼각형 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x1 = sc.nextInt();
        int y1 = sc.nextInt();
        int x2 = sc.nextInt();
        int y2 = sc.nextInt();
        int x3 = sc.nextInt();
        int y3 = sc.nextInt();

        double S;
         double answer;
        S= Math.abs(((x1 * y2) + (x2 * y3) + (x3 * y1)) - ((x2 * y1) + (x3 * y2) + (x1 * y3)));
         answer = S/2;
        System.out.printf("%.2f" , answer);


    }
}