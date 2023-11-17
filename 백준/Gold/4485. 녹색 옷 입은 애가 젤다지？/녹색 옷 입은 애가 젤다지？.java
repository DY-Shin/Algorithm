import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    static class Point implements Comparable<Point>{
        int x, y, cost;

        public Point(int x, int y, int cost) {
            this.x = x;
            this.y = y;
            this.cost = cost;
        }

        @Override
        public int compareTo(Point o) {
            return this.cost - o.cost;
        }
    }
    static int[][] arr;
    static int[][] dijk;
    static int N;
    static int[] dx = {0, 0, -1, 1};
    static int[] dy = {-1, 1, 0, 0};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int count = 0;
        while (true) {
            count++;
            N = Integer.parseInt(br.readLine());
            if (N == 0) break;
            arr = new int[N][N];
            dijk = new int[N][N];
            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < N; j++) {
                    arr[i][j] = Integer.parseInt(st.nextToken());
                    dijk[i][j] = Integer.MAX_VALUE;
                }
            }
            System.out.println("Problem " + count + ": " + dijkstra());
        }
        br.close();
    }

    public static int dijkstra() {
        PriorityQueue<Point> pq = new PriorityQueue<>();
        pq.add(new Point(0, 0, arr[0][0]));
        dijk[0][0] = arr[0][0];
        while (!pq.isEmpty()) {
            Point p = pq.poll();
            int sx = p.x;
            int sy = p.y;

            for (int k = 0; k < 4; k++) {
                int nx = sx + dx[k];
                int ny = sy + dy[k];
                if (nx >= 0 && ny >= 0 && nx < N && ny < N) {
                    if (dijk[nx][ny] > dijk[sx][sy] + arr[nx][ny]) {
                        dijk[nx][ny] = dijk[sx][sy] + arr[nx][ny];
                        pq.add(new Point(nx, ny, dijk[nx][ny]));
                    }
                }
            }
        }
        return dijk[N -1][N - 1];
    }
}