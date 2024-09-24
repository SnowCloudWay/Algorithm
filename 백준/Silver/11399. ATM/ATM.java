import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {

		PriorityQueue<Integer> pq = new PriorityQueue<>();
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		StringTokenizer str = new StringTokenizer(br.readLine());
		int pre = 0;
		int result = 0;
		
		
		for(int i = 0; i < n; i++) {
			pq.add(Integer.parseInt(str.nextToken()));
		}
		
		while(pq.peek() != null) {
			if(pq.peek() == null) break;
			result += pre + pq.peek();
			pre += pq.poll();
		}
		
		System.out.println(result);
		
	}
	
}
