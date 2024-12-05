import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());
        int cuteO = 0, cuteX = 0;

        for (int i = 0; i < N; i++) {
            int num = Integer.parseInt(br.readLine());
            if (num == 0)
                cuteX++;
            else
                cuteO++;
        }

        if (cuteO > cuteX)
            sb.append("Junhee is cute!");
        else
            sb.append("Junhee is not cute!");

        System.out.println(sb);

    }
}
