import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int chicken = Integer.parseInt(st.nextToken());
        int beef = Integer.parseInt(st.nextToken());
        int pasta = Integer.parseInt(st.nextToken());

        StringTokenizer str = new StringTokenizer(br.readLine());
        int c = Integer.parseInt(str.nextToken());
        int b = Integer.parseInt(str.nextToken());
        int p = Integer.parseInt(str.nextToken());

        int result = 0;

        if (c > chicken) {
            result += (c - chicken);
        }
        if (b > beef) {
            result += (b - beef);
        }
        if (p > pasta) {
            result += (p - pasta);
        }

        System.out.println(result);
    }
}
