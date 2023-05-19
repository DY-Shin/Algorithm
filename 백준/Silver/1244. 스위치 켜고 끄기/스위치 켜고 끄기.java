import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] arr = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
        int M = Integer.parseInt(br.readLine());
        for (int i = 0; i < M; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int gender = Integer.parseInt(st.nextToken());
            int num = Integer.parseInt(st.nextToken());
            if (gender == 1) {
                for (int j = 1; j <= N / num; j++) {
                    if (arr[j * num - 1] == 1) {
                        arr[j * num - 1] = 0;
                    } else {
                        arr[j * num - 1] = 1;
                    }
                }
            } else {
                for (int j = 0; j < num && j < N - num + 1; j++) {
                    if (arr[num - j - 1] == arr[num + j - 1]) {
                        if (arr[num - j - 1] == 0) {
                            arr[num - j - 1] = 1;
                            arr[num + j - 1] = 1;
                        } else {
                            arr[num - j - 1] = 0;
                            arr[num + j - 1] = 0;
                        }
                    } else {
                        break;
                    }
                }
            }
        }
        for (int i = 0; i < N; i++) {
            System.out.print(arr[i] + " ");
            if ((i + 1) % 20 == 0) {
                System.out.println();
            }
        }
    }
}
