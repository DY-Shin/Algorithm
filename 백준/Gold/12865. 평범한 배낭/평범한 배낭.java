import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        int[] W = new int[K + 1];
        int[] V = new int[K + 1];
        int[] dp = new int[K + 1];
        for (int i = 1; i <= N; i++) {
            StringTokenizer str = new StringTokenizer(br.readLine());
            W[i] = Integer.parseInt(str.nextToken());
            V[i] = Integer.parseInt(str.nextToken());
        }
        
        for (int i = 1; i <= N; i++) {
            for (int j = K; j - W[i] >= 0; j--) {
                dp[j] = Math.max(dp[j], dp[j - W[i]] + V[i]);
            }
        }
        System.out.println(dp[K]);
    }
}
