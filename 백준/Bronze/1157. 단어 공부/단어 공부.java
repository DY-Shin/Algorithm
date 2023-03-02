import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        int[] arr = new int[26];

        for (int i = 0; i < s.length(); i++) {
            if ('a' <= s.charAt(i) && s.charAt(i) <= 'z') {
                arr[s.charAt(i) - 'a']++;
            }
            else {
                arr[s.charAt(i) - 'A']++;
            }
        }
        int max = -1;
        char cr = '?';
        for (int i = 0; i < 26; i++) {
            if (arr[i] > max) {
                max = arr[i];
                cr = (char) (i + 'A');
            }
            else if (arr[i] == max) {
                cr = '?';
            }
        }
        System.out.println(cr);
    }
}
