import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.Arrays;

class Coordinate implements Comparable<Coordinate> {
	private int x;
	private int y;
	
	public Coordinate(int x, int y) {
		this.x = x;
		this.y = y;
	}
	
	public String toString() {
		return this.x + " " + this.y;
	}
	
	public int compareTo(Coordinate c) {
		return Integer.compare(this.x, c.x);
	}
	
	// 좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬
	public static class YXComp implements Comparator<Coordinate> {
		public int compare(Coordinate c1, Coordinate c2) {
			if(c1.y < c2.y) return -1;
			if(c1.y > c2.y) return 1;
			if(c1.x < c2.x) return -1;
	        if(c1.x > c2.x) return 1;
			return 0;
		}
	}
}

public class Main {
	
	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		Coordinate[] data = new Coordinate[n];
		
		for(int i = 0; i < n; i++) {
			String[] coordinate = br.readLine().split(" ");
			int x = Integer.parseInt(coordinate[0]);
			int y = Integer.parseInt(coordinate[1]);
			data[i] = new Coordinate(x, y);
		}
		
		Arrays.sort(data, new Coordinate.YXComp());
		for(Coordinate d : data)
			System.out.println(d);
		
	}

}
