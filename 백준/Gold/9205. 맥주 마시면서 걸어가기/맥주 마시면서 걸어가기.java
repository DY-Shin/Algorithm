import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
    static int n;
    static int[][] arr;
    static Queue<int[]> que = new LinkedList<>();
    static boolean[] visited;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        for (int i = 0; i < t; i++) {
            n = Integer.parseInt(br.readLine());
            arr = new int[n + 2][2];
            visited = new boolean[n + 2];
            for (int j = 0; j < n + 2; j++) {
                arr[j] = Arrays.stream(br.readLine().split(" "))
                        .mapToInt(Integer::parseInt)
                        .toArray();
            }
            System.out.println(bfs(arr[0]));
        }
    }

    public static String bfs(int[] house){
        que.add(house);
        visited[0] = true;
        while (!que.isEmpty()){
            int[] tmp = que.remove();
            if (tmp == arr[n + 1]) {
                return "happy";
            }
            int x = tmp[0];
            int y = tmp[1];
            for (int i = 0; i < arr.length; i++) {
                int nx = arr[i][0];
                int ny = arr[i][1];
                if (Math.abs(nx - x) + Math.abs(ny - y) <= 1000 && !visited[i]){
                    visited[i] = true;
                    que.add(arr[i]);
                }
            }
        }
        return "sad";
    }
}
