

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main  {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int num = Integer.parseInt(br.readLine());
		StringTokenizer str = new StringTokenizer(br.readLine());
		int count = 0;
		int pn;
		
		for(int i = 0; i < num; i++) {
			pn = Integer.parseInt(str.nextToken());
			for(int j = 2; j <= pn; j++) {
				if(j == pn) {
					count++;
				}
				if(pn % j == 0) {
					break;
				}
			}
		}
		
		System.out.println(count);
		
	}

}
