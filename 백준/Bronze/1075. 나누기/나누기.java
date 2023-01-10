import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String num = br.readLine();
        char[] arr = num.toCharArray();
        for(int i = (arr.length) - 2; i < arr.length; i++){
            arr[i] = '0';
        }
        String new_N = new String(arr);
        int N = Integer.parseInt(new_N);
        int F = Integer.parseInt(br.readLine());
        if (N % F == 0){
            System.out.println("00");
        }
        else if((F - (N % F)) < 10){
            String result = Integer.toString(F - (N % F));
            System.out.println("0" + result);
        }
        else{
            System.out.println(F - (N % F));
        }
    }
}