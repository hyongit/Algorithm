import java.io.*;
import java.util.*;

public class BOJ_15651 {
    static StringBuilder sb = new StringBuilder();
    static int[] selected;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        selected = new int[M+1];


        rec_func(N, M, 1);
        System.out.println(sb.toString());
    }

    // 재귀 함수
    // 만약 M 개를 전부 고름 => 조건에 맞는 탐색을 한 가지 성공한 것!
    // 아직 M 개를 고르지 않음 => k번째부터 M번째 원소를 조건에 맞게 고르는 모든 방법을 시도
    static void rec_func(int N, int M, int k) {
        if(k == M+1) { //다 골랐다!
            // selected[1...M] 배열이 새롭게 탐색된 결과
            for (int i=1; i<=M; i++) {
                sb.append(selected[i]).append(' ');
            }
            sb.append('\n');
            return; // DFS 종료
        } else {
            for(int cand = 1; cand<=N; cand++) {
                selected[k] = cand;
                // k+1번 ~ M번을 모두 탐색하는 일을 해야 하는 상황
                rec_func(N,M,k+1);
                selected[k] = 0;
            }
        }
    }
}
