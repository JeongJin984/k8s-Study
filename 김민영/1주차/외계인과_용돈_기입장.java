package 비타알고;

import java.util.Scanner;

public class 외계인과_용돈_기입장 {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        int column = sc.nextInt();
        int[] num_arr = new int[num+1];
        for(int i=1; i<=num; i++){
            num_arr[i] = sc.nextInt();
        }
        for(int i=0; i<column; i++){
            int start = sc.nextInt();
            int last = sc.nextInt();
            System.out.println(Solution(num_arr,start,last));
        }

    }

    private static int Solution(int[] num_arr, int start, int last) {
        int answer=0;
        for(int i=start; i<=last; i++){
            answer += num_arr[i];
        }

        return answer;

    }