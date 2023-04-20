import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] arr = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
        int[] sorted_arr = arr.clone();
        Arrays.sort(sorted_arr);
        int[] P = new int[N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (sorted_arr[i] == arr[j]) {
                    P[j] = i;
                    arr[j] = -1;
                    break;
                }
            }
        }
        Arrays.stream(P).forEach(x -> System.out.print(x + " "));
    }
}
