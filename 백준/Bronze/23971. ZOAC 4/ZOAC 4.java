import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int H = Integer.parseInt(st.nextToken());
        int W = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int r = H / (1 + N);
        if (H % (1 + N) != 0) {
            r++;
        }
        int c = W / (1 + M);
        if (W % (1 + M) != 0) {
            c++;
        }
        System.out.println(r * c);
    }
}
