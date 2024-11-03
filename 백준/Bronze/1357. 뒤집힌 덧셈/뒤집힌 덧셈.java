import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder a = new StringBuilder(st.nextToken());
        StringBuilder b = new StringBuilder(st.nextToken());
        StringBuilder sb = new StringBuilder();
        sb.append(Integer.parseInt(a.reverse().toString()) + Integer.parseInt(b.reverse().toString()));

        bw.write(Integer.toString(Integer.parseInt(sb.reverse().toString())));
        bw.flush();

    }

}
