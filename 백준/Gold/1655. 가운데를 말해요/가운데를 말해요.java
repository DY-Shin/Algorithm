import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Queue;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        Queue<Integer> maxQue = new PriorityQueue<>(Comparator.reverseOrder());
        Queue<Integer> minQue = new PriorityQueue<>();
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
            int num = Integer.parseInt(br.readLine());
            if (maxQue.size() > minQue.size()) {
                minQue.add(num);
                if (maxQue.peek() > minQue.peek()) {
                    minQue.add(maxQue.poll());
                    maxQue.add(minQue.poll());
                }
            } else {
                maxQue.add(num);
                if (!minQue.isEmpty() && maxQue.peek() > minQue.peek()) {
                    minQue.add(maxQue.poll());
                    maxQue.add(minQue.poll());
                }
            }
            sb.append(maxQue.peek() + "\n");
        }
        System.out.println(sb);
    }
}
