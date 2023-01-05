import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		int[] fee = new int[N];
		for (int i = 0; i < N; i++) {
			fee[i] = Integer.parseInt(st.nextToken());
		}
//		System.out.println(Arrays.toString(fee));
		int Y = 0, M = 0;
		for (int i : fee) {
			Y += ((i / 30) + 1) * 10;
			M += ((i / 60) + 1) * 15;
		}
		if (Y > M) {
			System.out.println("M " + M);
		}
		else if(M > Y) {
			System.out.println("Y " + Y);
		}
		else {
			System.out.println("Y " + "M " + Y);
		}
	}
}