import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer str1 = new StringTokenizer(br.readLine());
        StringTokenizer str2 = new StringTokenizer(br.readLine());

        int totalScore_S = 0;    // 민국
        int totalScore_T = 0;    // 만세

        for(int i = 0; i < 4; i++) {
           totalScore_S += Integer.parseInt(str1.nextToken());
           totalScore_T += Integer.parseInt(str2.nextToken());
        }

        if(totalScore_S >= totalScore_T)
            System.out.println(totalScore_S);
        else
            System.out.println(totalScore_T);

    }

}
