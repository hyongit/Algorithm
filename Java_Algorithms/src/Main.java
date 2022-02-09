import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) {
        ArrayList<Integer> dataList = new ArrayList<Integer>();
        dataList.add(9);
        dataList.add(2);
        dataList.add(4);

        for(int i = 0; i<dataList.size()-1; i++) {
            if(dataList.get(i) > dataList.get(i+1)) {
                // Collections.swap(ArrayList명, swap할 idx, swap할 idx)
                Collections.swap(dataList, i, i+1);
            }
        }
        System.out.println(dataList);
    }
}