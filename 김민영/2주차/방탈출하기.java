package 비타알고;

import java.util.Arrays;
import java.util.Scanner;

public class 방탈출하기 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] n_arr = new int[n];
        for(int i=0; i<n; i++){
            n_arr[i] = sc.nextInt();
        }
        int m= sc.nextInt();
        int[] m_arr = new int[m];
        for(int i=0; i<m; i++){
            m_arr[i] = sc.nextInt();
        }

        Arrays.sort(n_arr);
        for(int i=0; i<m_arr.length; i++){
            System.out.println(BinarySearch(n_arr,m_arr[i]));
        }

    }

    private static int BinarySearch(int[] n_arr, int m_arr) {
        int answer =0;
        int first =0;
        int last = n_arr.length-1;
        while (first<=last){
            int mid = (first+last)/2;
            if (n_arr[mid] == m_arr) {
                answer = 1;
                break;
            }
            else {
                if (n_arr[mid] > m_arr) {
                    last = mid - 1;
                } else
                    first = mid + 1;
            }
        }

        return answer;
    }
}
