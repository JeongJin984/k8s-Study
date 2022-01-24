package 비타알고;

import java.util.Scanner;

public class 동전줍기대회 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] arr = new int[N+1];

        for(int i=1; i<=N; i++){
            arr[i] = sc.nextInt();
        }



        int[] dp = new int[N+1];
        dp[0] = 0;
        int max = -987654321;
        for(int i=1; i<=N; i++){
            dp[i] = Math.max(0, dp[i-1]) + arr[i];
            max = Math.max(max, dp[i]);
        }

        System.out.println(max);


    }
}