import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        List<Integer> sixBundle = new ArrayList<>();
        List<Integer> single = new ArrayList<>();
        for (int i = 0; i < M; i++) {
            StringTokenizer str = new StringTokenizer(br.readLine());
            int sx = Integer.parseInt(str.nextToken());
            int sg = Integer.parseInt(str.nextToken());
            sixBundle.add(sx);
            single.add(sg);
        }
        int value1 = N / 6;
        int value2 = N - value1 * 6;

        int sxMin = Collections.min(sixBundle);
        int sgMin = Collections.min(single);

        int result = 0;
        if (sxMin > sgMin * 6) {
            result = sgMin * N;
        }
        else if (value2 * sgMin > sxMin) {
            result = sxMin * (value1 + 1);
        }
        else {
            result = sxMin * value1 + sgMin * value2;
        }
        System.out.println(result);
    }
}
