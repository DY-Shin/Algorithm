import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int num;
        String game = st.nextToken();
        List<String> arr = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            arr.add(br.readLine());
        }
        arr = new ArrayList<String>(arr.stream().distinct()
                .collect(Collectors.toList()));

        if (game.equals("Y")) {
            num = arr.size();
        } else if (game.equals("F")) {
            num = arr.size() / 2;
        } else {
            num = arr.size() / 3;
        }

        System.out.println(num);

    }
}
