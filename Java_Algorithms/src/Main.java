import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        for(int num=0; num<3; num++) {
            for(int index=0; index<n; index++){
                System.out.print(index + " ");
            }
            System.out.println();
        }
    }
}