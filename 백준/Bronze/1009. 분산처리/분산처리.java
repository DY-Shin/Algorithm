import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int tmp = a % 10;
            if (tmp == 0){
                tmp = 10;
                System.out.println(tmp);
                continue;
            }
            for (int j = 1; j < b; j++) {
                tmp = (tmp * a) % 10;
            }
            System.out.println(tmp);
        }
    }
}
