package 비타알고;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class 앵무새꼬꼬 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();
        String str = new String();
        char[] aa = {'a','A','e','E','o','O','u','U'};
        int count=0;
        for(int i=0; i<input.length(); i++){
            for(int j=0; j<aa.length; j++){
                if(input.charAt(i) == aa[j]){
                    str+=input.charAt(i);
                    count++;
                }
            }
        }
        if(count ==0){
            System.out.println("???");
        }
        else{
            System.out.println(str);
        }


    }
}