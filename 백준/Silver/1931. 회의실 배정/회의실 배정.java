
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		int[][] meetingTimes = new int[n][2];
		
		for(int i = 0; i < n; i++) {
			StringTokenizer str = new StringTokenizer(br.readLine());
			meetingTimes[i][0] = Integer.parseInt(str.nextToken());
			meetingTimes[i][1] = Integer.parseInt(str.nextToken());
		}
		
		Arrays.sort(meetingTimes, (o1, o2) -> (o1[1] == o2[1] ? o1[0] - o2[0] : o1[1] - o2[1]));
		
		int endTime = 0;
		int count = 0;
		
		
		for(int i = 0; i < n; i++) {
			if(meetingTimes[i][0] >= endTime) {
				endTime = meetingTimes[i][1];
				count += 1;
			}
				
		}
		
		System.out.println(count);
		
	}

}
