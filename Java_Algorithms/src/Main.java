import java.io.*;
import java.util.*;


public class Main{
    public static void main(String[] args) {
        String str = "바나나 : 1000원, 사과 : 2000원, 배 : 3000원";
        String target = "사과";
        int target_num = str.indexOf(target); // 13
        String result = str.substring(target_num, (str.substring(target_num).indexOf("원")+target_num)); // 13 ~ 9+13(22)
        System.out.println(result);
    }
}