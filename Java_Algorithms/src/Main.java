import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) {
        int n = 4;
        int[] passenger = {2,1,2,2};
        int[][] train = {
                {1,2}, {1,3}, {2,4}
        };

        int[] new_passenger = new int[n+1];
        Arrays.fill(new_passenger, 0);

        for(int i=0; i<passenger.length; i++){
            new_passenger[i+1] = passenger[i];
        }

        for(int i=0; i<n+1; i++){
            System.out.print(new_passenger[i] + " ");
        }
        System.out.println();

        int[] answer = new int[2];
        int max = 0;

        boolean[] visited = new boolean[n+1];
        Arrays.fill(visited, false);
        ArrayList<Integer>[] graph = new ArrayList[n+1];
        for(int i=0; i<=n; i++){
            graph[i] = new ArrayList<Integer>();
        }

        for(int i=0; i<train.length; i++) {
            graph[train[i][0]].add(train[i][1]);
        }

//        for(int i=0; i<=n; i++){
//            System.out.println(graph[i]);
//        }

        Queue<Integer> q = new LinkedList<Integer>();
        q.offer(1);
        while(!q.isEmpty()) {
            int now = q.poll();
            for(int i=0; i < graph[now].size(); i++){
                int nextNode = graph[now].get(i);
                if(visited[nextNode] == false) {
                    visited[nextNode] = true;
                    q.offer(nextNode);
                    new_passenger[nextNode] += new_passenger[now];
                    System.out.println(new_passenger[nextNode]);
                }
            }
        }

        for(int i=1; i<new_passenger.length; i++){
            if(max<new_passenger[i]){
                max = new_passenger[i];
                answer[0] = i;
                answer[1] = max;
            } else if (max == new_passenger[i]) {
                max = new_passenger[i];
                answer[0] = i;
                answer[1] = max;
            }
        }

        for(int i=0; i<answer.length; i++){
            System.out.print(answer[i] + " ");
        }
    }
}