import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int L = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        ArrayList<Integer> arr = new ArrayList<>();
        for (int i = 0; i < L; i++) {
            int num = Integer.parseInt(st.nextToken());
            arr.add(num);
        }
        int n = Integer.parseInt(br.readLine());
        Collections.sort(arr);
        int result = 0;
        int s = 0;
        int e = 1001;
        for (int i = 0; i < L; i++) {
            if (arr.get(i) == n) {
                System.out.println(0);
                return;
            }
            if (arr.get(i) > n) {
                if (i == 0) {
                    e = arr.get(i);
                    break;
                }
                s = arr.get(i - 1);
                e = arr.get(i);
                break;
            }
        }
        for (int i = s + 1; i <= n; i++) {
            for (int j = n; j <= e - 1; j++) {
                if (i != j) {
                    result++;
                }
            }
        }
        System.out.println(result);
    }
}
