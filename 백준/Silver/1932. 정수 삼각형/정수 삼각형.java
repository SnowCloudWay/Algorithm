import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		
		int[][] a = new int[n][n];
		int[][] dp = new int[n][n];
		StringTokenizer str;
		
		for(int i = 0; i < n; i++) {
			str = new StringTokenizer(br.readLine(), " ");
			
			for(int j = 0; j < i + 1; j++) {
				a[i][j] = Integer.parseInt(str.nextToken());
			}
		}
		
		dp[0][0] = a[0][0];
		
		for(int i = 1; i < n; i++) {
			for(int j = 0; j <= i; j++) {
				if(j == 0) {
					dp[i][j] = dp[i-1][j] + a[i][j];
				}
				else {
					dp[i][j] = Math.max(dp[i-1][j-1], dp[i-1][j]) + a[i][j];
				}
			}
		}
		
		int max = 0;
		for(int i = 0; i < n; i++) {
			if(max < dp[n-1][i]) {
				max = dp[n-1][i];
			}
		}
		
		System.out.println(max);
		
	}
	
}
