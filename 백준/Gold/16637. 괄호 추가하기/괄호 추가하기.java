import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Main {
    static int N;
    static int result = Integer.MIN_VALUE;
    static List<String> formula;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        formula = Arrays.stream(br.readLine().split("")).collect(Collectors.toList());
        eval(0, Integer.parseInt(formula.get(0)));
        System.out.println(result);
    }

    public static void eval(int s, int sum) {
        if (s >= N - 1) {
            result = Math.max(result, sum);
            return;
        }

        int calc1 = calc(sum, formula.get(s + 1), Integer.parseInt(formula.get(s + 2)));
        eval(s + 2, calc1);

        if (s + 4 < N) {
            int calc2 = calc(sum, formula.get(s + 1), calc(Integer.parseInt(formula.get(s + 2)), formula.get(s + 3), Integer.parseInt(formula.get(s + 4))));
            eval(s + 4, calc2);
        }
    }

    public static int calc(Integer a, String b, Integer c) {
        if (b.equals("+")) {
            return a + c;
        } else if(b.equals("-")) {
            return a - c;
        } else {
            return a * c;
        }
    }
}
