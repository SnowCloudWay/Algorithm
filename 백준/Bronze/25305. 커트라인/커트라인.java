import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Arrays;
import java.util.Collections;

public class Main {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer str = new StringTokenizer(br.readLine());
		
		int n = Integer.parseInt(str.nextToken());
		int cut = Integer.parseInt(str.nextToken());
		Integer[] score = new Integer[n];
		
		StringTokenizer str2 = new StringTokenizer(br.readLine());
		
		for(int i = 0; i < n; i++) {
			score[i] = Integer.parseInt(str2.nextToken());
		}
		
		Arrays.sort(score, Collections.reverseOrder());
		
		System.out.println(score[cut - 1]);
		
	}

}
