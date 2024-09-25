import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            int score = 0;
            int total_score = 0;
            String ox = br.readLine();
            for (String s : ox.split("")) {
                if (s.equals("X")) {
                    score = 0;
                }
                else if (s.equals("O")) {
                    score += 1;
                    total_score += score;
                }
            }
            System.out.println(total_score);
        }

    }
}