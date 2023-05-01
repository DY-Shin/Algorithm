import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main{
    static int N, M, cheese;
    static int[][] visited;
    static int[][] arr;
    static int[] dx = {0, 0, -1, 1};
    static int[] dy = {-1, 1, 0, 0};
    static Queue<int[]> que = new LinkedList<>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        arr = new int[N][M];
        for (int i = 0; i < N; i++) {
            StringTokenizer str = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                arr[i][j] = Integer.parseInt(str.nextToken());
                if (arr[i][j] == 1) {
                    cheese++;
                }
            }
        }
        int count = 0;
        while (cheese > 0) {
            visited = new int[N][M];
            int result = bfs();
            count++;
            cheese -= result;
        }
        System.out.println(count);
    }

    public static int bfs() {
        int result = 0;
        que.add(new int[]{0, 0});
        while (!que.isEmpty()) {
            int[] site = que.remove();
            for (int i = 0; i < 4; i++) {
                int nx = site[0] + dx[i];
                int ny = site[1] + dy[i];
                if (nx >= 0 && ny >= 0 && nx < N && ny < M) {
                    if (visited[nx][ny] == 0 && arr[nx][ny] == 0) {
                        visited[nx][ny] += 1;
                        que.add(new int[]{nx, ny});
                    } else if (visited[nx][ny] >= 0 && arr[nx][ny] == 1) {
                        visited[nx][ny] += 1;
                    }
                }
            }
        }
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (visited[i][j] >= 2) {
                    arr[i][j] = 0;
                    result++;
                }
            }
        }
        return result;
    }
}
