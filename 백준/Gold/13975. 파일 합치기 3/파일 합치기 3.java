import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(br.readLine());
		
		for(int tc = 0; tc < T; tc++) {
			
			int n = Integer.parseInt(br.readLine());
			StringTokenizer str = new StringTokenizer(br.readLine());
			
			PriorityQueue<Long> pq = new PriorityQueue<>();
			for(int i = 0; i < n; i++) {
				pq.add(Long.parseLong(str.nextToken()));
			}
			
			long result = 0;
			
			while(true) {
				if(pq.size() == 1) break;
				long num1 = pq.poll();
				long num2 = pq.poll();
				
				result += num1 + num2;
				pq.add(num1 + num2);
			}
			
			System.out.println(result);
			
		}

	}

}
