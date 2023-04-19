import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
    static int k;
    static String[] arr;
    static List<String> answer;
    static boolean[] visited;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        k = Integer.parseInt(br.readLine()) + 1;
        arr = br.readLine().split(" ");
        answer = new ArrayList<>();
        visited = new boolean[10];
        for (int i = 0; i < 10; i++) {
            visited[i] = false;
        }
        dfs(0, "");
        System.out.println(answer.get(answer.size() - 1));
        System.out.println(answer.get(0));
    }

    public static void dfs(int cnt, String word) {
        if (word.length() == k) {
            answer.add(word);
            return;
        }

        if (cnt >= k) {
            return;
        }

        for (int i = 0; i < 10; i++) {
            if (!visited[i]) {
                if (word.length() < 1) {
                    visited[i] = true;
                    dfs(cnt + 1, word + i);
                    visited[i] = false;
                } else {
                    if (arr[cnt - 1].equals(">")) {
                        if (word.charAt(word.length() - 1) - '0' > i) {
                            visited[i] = true;
                            dfs(cnt + 1, word + i);
                            visited[i] = false;
                        }
                    } else {
                        if (word.charAt(word.length() - 1) - '0' < i) {
                            visited[i] = true;
                            dfs(cnt + 1, word + i);
                            visited[i] = false;
                        }
                    }
                }
            }
        }
    }
}
