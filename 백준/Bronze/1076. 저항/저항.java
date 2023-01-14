import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        List<List<String>> mylist = Arrays.asList(
                Arrays.asList("black", "0", "1"),
                Arrays.asList("brown", "1", "10"),
                Arrays.asList("red", "2", "100"),
                Arrays.asList("orange", "3", "1000"),
                Arrays.asList("yellow", "4", "10000"),
                Arrays.asList("green", "5", "100000"),
                Arrays.asList("blue", "6", "1000000"),
                Arrays.asList("violet", "7", "10000000"),
                Arrays.asList("grey", "8", "100000000"),
                Arrays.asList("white", "9", "1000000000")
        );
        String s = new String();
        Long num = 0L;
        for (int i = 0; i < 3; i++) {
            String color = br.readLine();
            if (i < 2) {
                for (int j = 0; j < 10; j++) {
                    if (color.equals(mylist.get(j).get(0))) {
                        s += mylist.get(j).get(1);
                    }
                }
            } else {
                for (int j = 0; j < 10; j++) {
                    if (color.equals(mylist.get(j).get(0))) {
                        num = Long.parseLong(mylist.get(j).get(2));
                    }
                }
            }
        }
        long result = Integer.parseInt(s) * num;
        System.out.println(result);
    }
}