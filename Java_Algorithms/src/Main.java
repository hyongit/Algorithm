import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args) {
        HashMap<Integer, String> map1 = new HashMap();
        map1.put(1, "사과");
        map1.put(2, "바나나");
        map1.put(3, "포도");

        HashMap<String, String> map2 = new HashMap();
        map2.put("DaveLee", "사과");
        map2.put("Dave", "바나나");
        map2.put("David", "포도");

        System.out.println(map1.get(1)); // 사과
    }
}