import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        HashSet<String> set = new HashSet<>();
        for (int i = 0; i < N; i++) {
            set.add(br.readLine());
        }
        int result = 0;
        List<String> re = new ArrayList<>();
        for (int i = 0; i < M; i++) {
            String see = br.readLine();
            if (set.contains(see)) {
                re.add(see);
                result++;
            }
        }
        re.sort(Comparator.naturalOrder());
        System.out.println(result);
        for (String person : re) {
            System.out.println(person);
        }
    }
}
