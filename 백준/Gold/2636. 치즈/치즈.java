import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Cheese {
    int x;
    int y;

    public Cheese(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

public class Main {
    static int[][] arr;
    static int[] dx = {0, 0, -1, 1};
    static int[] dy = {-1, 1, 0, 0};
    static boolean[][] visited;
    static Queue<Cheese> que = new LinkedList<>();
    static int r;
    static int c;
    static int cheese = 0;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        arr = new int[r][c];
        for (int i = 0; i < r; i++) {
            arr[i] = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();
        }
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (arr[i][j] == 1) {
                    cheese++;
                }
            }
        }
        int time = 0;
        int resultCheese = 0;
        while (cheese > 0) {
            visited = new boolean[r][c];
            time++;
            resultCheese = bfs();
            cheese -= resultCheese;
        }
        System.out.println(time);
        System.out.println(resultCheese);
    }

    public static int bfs() {
        que.offer(new Cheese(0, 0));
        visited[0][0] = true;
        int ch = 0;
        while (!que.isEmpty()) {
            Cheese tmp = que.remove();
            int x1 = tmp.x;
            int y1 = tmp.y;
            for (int i = 0; i < 4; i++) {
                int nx = x1 + dx[i];
                int ny = y1 + dy[i];
                if (nx >= 0 && ny >= 0 && nx < r && ny < c && !visited[nx][ny]) {
                    if (arr[nx][ny] == 0) {
                        que.offer(new Cheese(nx, ny));
                        visited[nx][ny] = true;
                    } else {
                        visited[nx][ny] = true;
                        arr[nx][ny] = 0;
                        ch++;
                    }
                }
            }
        }
        return ch;
    }
}
