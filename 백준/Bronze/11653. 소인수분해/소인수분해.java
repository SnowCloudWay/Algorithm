import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		int m = n;
		
		for (int i = 2; i <= m; i++) {
			if(n % i == 0) {
				n = n / i;
				System.out.println(i);
				i-= 1;
			}
			if(n == 1) break;
		}
		
		

	}

}