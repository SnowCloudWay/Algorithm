import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer str = new StringTokenizer(br.readLine());

        int hour = Integer.parseInt(str.nextToken());
        int min = Integer.parseInt(str.nextToken());
        int sec = Integer.parseInt(str.nextToken());

        int cookTime = Integer.parseInt(br.readLine());

        sec += cookTime;

        min += sec / 60;
        sec = sec % 60;

        hour += min / 60;
        min = min % 60;

        hour %= 24;

        System.out.printf("%d %d %d", hour, min, sec);

    }
}
