import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int L = Integer.parseInt(br.readLine());
        double[] powValue = new double[50];
        int result = 0;
        String line = br.readLine();
        HashMap<String, Integer> map = new HashMap<>();
        for (int i = 1; i < 27; i++) {
            map.put(String.valueOf((char)(96 + i)), i);
        }
        for (int i = 0; i < L; i++) {
            powValue[i] = Math.pow(31, i);
        }
        for (int i = 0; i < L; i++) {
            int tmp = map.get(String.valueOf(line.charAt(i)));
            result += tmp * powValue[i];
        }
        System.out.println(result);
    }
}
