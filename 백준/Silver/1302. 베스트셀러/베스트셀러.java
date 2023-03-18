import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        HashMap<String, Integer> map = new HashMap<>();
        for (int i = 0; i < N; i++) {
            String book = br.readLine();
            if (map.containsKey(book)) {
                int oldValue = map.get(book);
                map.replace(book, oldValue + 1);
            } else {
                map.put(book, 1);
            }
        }
        int max = 0;
        for (String a : map.keySet()) {
            max = Math.max(max, map.get(a));
        }

        List<String> keyList = new ArrayList<>(map.keySet());
        Collections.sort(keyList);
        for(String key : keyList){
            if (map.get(key) == max) {
                System.out.println(key);
                break;
            }
        }
    }
}
