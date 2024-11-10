import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        String str = br.readLine();

        long cntA = str.chars().filter(c -> c == 'A').count();
        long cntB = str.chars().filter(c -> c == 'B').count();

        if (cntA > cntB) System.out.println("A");
        else if (cntA < cntB) System.out.println("B");
        else System.out.println("Tie");

    }

}
