package 비타알고;

import java.util.ArrayList;
import java.util.Scanner;
import java.util.Stack;

public class 숫자블럭쌓기 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Stack<Integer> stack = new Stack<>();

        int count =0;
        int index=1;
        for(int i=0; i<2*n; i++){
            String str =sc.nextLine();
            String case_div = str.split(" ")[0];

            switch (case_div){
                case "add" :
                    int num = Integer.parseInt(str.split(" ")[1]);
                    stack.push(num);
                    break;

                case "remove":
                    if(!stack.isEmpty() && stack.peek() == index){
                        stack.pop();
                    }
                    else if(!stack.isEmpty()){
                        count++;
                        stack.clear();
                    }
                    index++;
                    break;
            }

        }
        System.out.println(count);
    }
}
