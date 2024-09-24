import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer str = new StringTokenizer(br.readLine());
        int hour = Integer.parseInt(str.nextToken());
        int min = Integer.parseInt(str.nextToken());

        if ((min - 45) < 0) {
            min += 15;
            hour -= 1;
        }
        else {
            min -= 45;
        }

        if (hour < 0) {
            hour = 23;
        }

        System.out.println(hour + " " + min);

    }
}
