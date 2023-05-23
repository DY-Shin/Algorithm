import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        PriorityQueue<Integer> que = new PriorityQueue<>(Comparator.reverseOrder());
        for (int i = 0; i < N; i++) {
            int value = Integer.parseInt(br.readLine());
            if (value == 0) {
                if (!que.isEmpty()) {
                    System.out.println(que.remove());
                } else {
                    System.out.println(0);
                }
            } else {
                que.add(value);
            }
        }
    }
}
