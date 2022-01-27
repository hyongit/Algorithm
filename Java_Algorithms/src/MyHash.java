import java.util.*;
import java.io.*;

public class MyHash {
    public Slot[] hashTable;

    //생성자
    public MyHash(Integer size) {
        this.hashTable = new Slot[size];
    }

    //내부 클래스
    public class Slot {
        String value;
        //생성자
        Slot(String value){
            this.value=  value;
        }
    }
    
    // 해쉬 함수
    // Key가 문자열일 때, 문자열 앞 글자를 숫자로 변환해서, 
    // Division 기법을 사용하여 Key에 대한 주소 계산.
    // Division : 가장 간단한 해쉬 함수 중 하나로 나누기의 나머지 값을 사용
    public Integer hashFunc(String key) {
        return (int)(key.charAt(0)) % this.hashTable.length;
    }

    public boolean saveData(String key, String value) {
        Integer address = this.hashFunc(key); // 해당 객체를 저장하는 주소 가져옴
        if(this.hashTable[address] != null) { // 데이터가 저장 되어 있다면
            this.hashTable[address].value = value; // value값만 바꿔줌
        } else {
            this.hashTable[address] = new Slot(value); // 해당 address에 Slot 객체 없다면
        }
        return true;
    }

    public String getData(String key) {
        Integer address = this.hashFunc(key);
        if(this.hashTable[address] != null) { // 해당 address에 객체 있다!
            return this.hashTable[address].value;
        } else {
            return null;
        }
    }

    public static void main(String[] args){
        MyHash mainObject = new MyHash(20);
        mainObject.saveData("DaveLee", "01022223333");
        mainObject.saveData("fun-coding", "01033334444");
        System.out.println(mainObject.getData("DaveLee"));
    }

}
