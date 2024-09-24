import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int n = Integer.parseInt(br.readLine());
		StringTokenizer str = new StringTokenizer(br.readLine());
		
		int[] a = new int[n];
		int[] dp = new int[n];
		
		for(int i = 0; i < n; i++) {
			a[i] = Integer.parseInt(str.nextToken());
		}
		
		dp[0] = a[0];
		int lengthOfLIS = 1;
		
		for (int i = 1; i < n; i++) {
			 
			int key = a[i];
			
			// 만약 key가 LIS의 마지막 값보다 클 경우 추가해준다. 
			if (dp[lengthOfLIS - 1] < key) {
				lengthOfLIS++;
				dp[lengthOfLIS - 1] = key;
			} 
			else {
				int lo = 0;
				int hi = lengthOfLIS;
				while (lo < hi) {
					int mid = (lo + hi) >>> 1;
					
					if(dp[mid] < key) {
						lo = mid + 1;
					}
					else {
						hi = mid;
					}
 
				}

				
				dp[lo] = key;
			
			}
			
		}

		System.out.println(n - lengthOfLIS);
		
		

	}

}
