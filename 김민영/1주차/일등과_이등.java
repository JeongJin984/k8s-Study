package 비타알고;

import java.util.Scanner;

public class 일등과_2등 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        // 배열로 변환
        int[] num_arr= new int[str.length()];
        for (int i=0; i<num_arr.length; i++){
            num_arr[i] = str.charAt(i)-'0';
        }

        String[] flag = {"12","21"};
        for(int i=0; i< num_arr.length; i++){
            if (num_arr[i] == 1) {
                if(flag[0] != "yes") {
                    if(num_arr[i+1]==2){
                        flag[0] = "yes";
                        num_arr[i] =0;
                        num_arr[i+1] =0;
                        continue;
                    }
                }
            }
            else if(num_arr[i] == 2){
                if(flag[1] != "yes"){
                    if(num_arr[i+1]==1){
                        flag[1] = "yes";
                        num_arr[i]=0;
                        num_arr[i+1]=0;
                        continue;
                    }
                }
            }
        }

        if(flag[0].equals(flag[1])){
            System.out.println("Yes");
        }
        else {
            System.out.println("No");
        }

    }
}