import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class tomato {
    int x, y, z;

    tomato(int x, int y, int z){
        this.x = x;
        this.y = y;
        this.z = z;
    }
}

public class Main {
    static int M, N, H;
    static int[][][] arr;
    static int[] dx = {0, 0, -1, 1, 0, 0};
    static int[] dy = {-1, 1, 0, 0, 0, 0};
    static int[] dz = {0, 0, 0, 0, -1, 1};
    static Queue<tomato> q;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        H = Integer.parseInt(st.nextToken());
        arr = new int[H][N][M];
        q = new LinkedList<>();
        for (int i = 0; i < H; i++) {
            for (int j = 0; j < N; j++) {
                StringTokenizer str = new StringTokenizer(br.readLine());
                for (int k = 0; k < M; k++) {
                    arr[i][j][k] = Integer.parseInt(str.nextToken());
                    if (arr[i][j][k] == 1) {
                        q.add(new tomato(k, j, i));
                    }
                }
            }
        }
        System.out.println(bfs());
    }

    public static int bfs() {
        while(!q.isEmpty()) {
            tomato t = q.remove();
            int x = t.x;
            int y = t.y;
            int z = t.z;

            for (int i = 0; i < 6; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                int nz = z + dz[i];

                if (nx >= 0 && ny >= 0 && nz >= 0 && nx < M && ny < N && nz < H) {
                    if (arr[nz][ny][nx] == 0) {
                        q.add(new tomato(nx, ny, nz));
                        arr[nz][ny][nx] = arr[z][y][x] + 1;
                    }
                }
            }
        }
        int result = Integer.MIN_VALUE;

        for (int i = 0; i < H; i++) {
            for (int j = 0; j < N; j++) {
                for (int k = 0; k < M; k++) {
                    if (arr[i][j][k] == 0) {
                        return -1;
                    }
                    result = Math.max(result, arr[i][j][k]);
                }
            }
        }
        return result - 1;
    }
}
