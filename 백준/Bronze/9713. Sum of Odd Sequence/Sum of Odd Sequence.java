import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            int result = 0;
            int num = Integer.parseInt(br.readLine());
            for (int j = 1; j < num+1; j++) {
                if (j % 2 != 0) result += j;
            }
            bw.write(Integer.toString(result)+'\n');
            bw.flush();
        }

    }

}
