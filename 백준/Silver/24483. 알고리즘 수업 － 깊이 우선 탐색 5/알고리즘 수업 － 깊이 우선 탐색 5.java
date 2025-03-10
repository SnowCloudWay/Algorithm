import java.io.*;
import java.util.*;

public class Main {

    static int N, M, R;
    static int cnt;
    static int[] depth;
    static int[] visited;
    static ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        long result = 0;

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());

        depth = new int[N+1];

        for (int i = 0; i <= N; i++) {
            graph.add(new ArrayList<>());
            depth[i] = -1;
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int v1 = Integer.parseInt(st.nextToken());
            int v2 = Integer.parseInt(st.nextToken());
            graph.get(v1).add(v2);
            graph.get(v2).add(v1);
        }

        for (int i = 0; i <= N; i++)
            Collections.sort(graph.get(i));

        visited = new int[N+1];
        cnt = 1;
        dfs(R, 0);

        for (int i = 1; i < visited.length; i++)
            result += ((long) visited[i] * depth[i]);

        sb.append(result);
        System.out.println(sb);

    }

    static void dfs(int v, int nowDepth) {
        visited[v] = cnt;
        depth[v] = nowDepth;
        for (int w : graph.get(v)) {
            if (visited[w] == 0) {
                cnt++;
                dfs(w, nowDepth + 1);
            }
        }
    }
}
