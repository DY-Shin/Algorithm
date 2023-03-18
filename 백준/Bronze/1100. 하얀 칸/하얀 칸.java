import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        List<String> list = new ArrayList<>();
        int chess = 0;
        for (int i = 0; i < 8; i++) {
            String line = br.readLine();
            list.add(line);
        }
        String[] array = list.toArray(new String[list.size()]);
        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {
                if (array[i].charAt(j) == 'F' && (i + j) % 2 == 0) {
                    chess++;
                }
            }
        }
        System.out.println(chess);
    }
}
