import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        LinkedList<Integer> que = new LinkedList<>();
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String cmd = st.nextToken();
            if (cmd.equals("push")) {
                que.add(Integer.parseInt(st.nextToken()));
            } else if (cmd.equals("pop")) {
                if (!que.isEmpty()) {
                    System.out.println(que.remove());
                } else {
                    System.out.println(-1);
                }
            } else if (cmd.equals("size")) {
                System.out.println(que.size());
            } else if (cmd.equals("empty")){
                if (que.isEmpty()) {
                    System.out.println(1);
                } else {
                    System.out.println(0);
                }
            } else if (cmd.equals("front")) {
                if (que.isEmpty()) {
                    System.out.println(-1);
                } else {
                    System.out.println(que.peek());
                }
            } else {
                if (que.isEmpty()) {
                    System.out.println(-1);
                } else {
                    System.out.println(que.peekLast());
                }
            }
        }
    }
}
