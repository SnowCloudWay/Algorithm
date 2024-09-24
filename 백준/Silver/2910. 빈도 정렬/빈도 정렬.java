import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st1 = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(st1.nextToken());
        int c = Integer.parseInt(st1.nextToken());
        StringTokenizer st2 = new StringTokenizer(br.readLine());
        HashMap<Integer, int[]> map = new HashMap<>(n); // 0은 개수, 1은 인덱스
        int idx = 0;
        while (st2.hasMoreTokens()){
            int in = Integer.parseInt(st2.nextToken());
            if (map.containsKey(in))
                map.put(in, new int[]{map.get(in)[0]+1, map.get(in)[1]});
            else map.put(in, new int[]{1, idx++});
        }
        map.entrySet().stream().sorted(new Comparator<Map.Entry<Integer, int[]>>() {
            @Override
            public int compare(Map.Entry<Integer, int[]> o1, Map.Entry<Integer, int[]> o2) {
                if (o2.getValue()[0]==o1.getValue()[0])
                    return o1.getValue()[1]-o2.getValue()[1];
                return o2.getValue()[0]-o1.getValue()[0];
            }
        }).forEach(i->{
            for (int j=0; j<i.getValue()[0]; j++)
                sb.append(i.getKey()+" ");
            });
        System.out.print(sb);
    }
}
