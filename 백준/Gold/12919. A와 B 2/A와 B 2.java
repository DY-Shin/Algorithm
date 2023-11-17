import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int result;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String S = br.readLine();
        String T = br.readLine();
        result = 0;
        solve(S, T);
        System.out.println(result);
    }

    public static void solve(String s, String t) {
        if (s.length() == t.length()) {
            if (s.equals(t)) {
                result = 1;
            }
            return;
        }

        if (t.charAt(0) == 'B') {
            StringBuilder st = new StringBuilder(t);
            String sub = st.reverse().substring(0, t.length() - 1);
            solve(s, sub);
        }
        if (t.charAt(t.length() - 1) == 'A') {
            t = t.substring(0, t.length() - 1);
            solve(s, t);
        }
}
}
