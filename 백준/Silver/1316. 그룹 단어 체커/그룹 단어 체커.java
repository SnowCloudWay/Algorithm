import java.io.BufferedReader;
import java.io.*;
import java.util.*;
public class Main {
    static int solution(String str){
        HashMap<Character, Integer> map = new HashMap<>();
        for(int i = 0; i < str.length(); i++){
            char c = str.charAt(i);
            if(map.containsKey(c)){
                if(i != map.get(c)+1){
                    return 0;
                }
                map.put(c, map.get(c)+1);
            }
            else{
                map.put(c, i);
            }
        }
        return 1;
    }
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int result = 0;
        for(int i = 0; i < n; i++){
            String str = br.readLine();
            result += solution(str);
        }
       System.out.println(result);
    }
}