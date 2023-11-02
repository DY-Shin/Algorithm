import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int P = Integer.parseInt(br.readLine());
        int arr[][] = new int[P][21];
        for (int i = 0; i < P; i++) {
            arr[i] = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();
        }
        for (int i = 0; i < P; i++) {
            int tmp[] = new int[20];
            tmp[19] = arr[i][1];
            int cnt = 0;
            for (int j = 2; j < 21; j++) {
                int num = 0;
                for (int k = 19; k > -1; k--) {
                    if (tmp[k] > arr[i][j]) {
                        num += 1;
                    } else {
                        tmp[0] = arr[i][j];
                        Arrays.sort(tmp);
                        break;
                    }
                }
                cnt += num;
            }
            System.out.print(arr[i][0] + " ");
            System.out.println(cnt);
        }
    }
}
