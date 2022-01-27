import java.util.*;
import java.io.*;

//Open Hash
public class MyHash {
    public Slot[] hashTable;

    //생성자
    public MyHash(Integer size) {
        this.hashTable = new Slot[size];
    }

    //내부 클래스
    public class Slot {
        String key;
        String value;
        Slot next; //링크드 리스트 포인터
        //생성자
        Slot(String key, String value){
            this.key = key;
            this.value = value;
            this.next = null;
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
        if(this.hashTable[address] != null) { // 앞 글자 똑같아서 충돌 발생!
            // 링크드리스트 헤드
            Slot findSlot = this.hashTable[address];
            Slot prevSlot = this.hashTable[address];

            while (findSlot != null) {
                // 내가 원하는 key에 해당하는 Slot이 있는 경우 값 변경만 해주면 됨
                if (findSlot.key == key) {
                    findSlot.value = value;
                    return true;
                } else { // 그렇지 않다면 순회!
                    prevSlot = findSlot;
                    findSlot = findSlot.next;
                }
            }
            prevSlot.next = new Slot(key, value);

        } else {
            this.hashTable[address] = new Slot(key, value); // 해당 key, address에 Slot 객체 없다면
        }
        return true;
    }

    public String getData(String key) {
        Integer address = this.hashFunc(key);
        if(this.hashTable[address] != null) { // 해당 address에 객체 있다!
            Slot findSlot = this.hashTable[address]; //헤드
            while (findSlot != null) {
                if(findSlot.key == key) {
                    return findSlot.value;
                } else {
                    findSlot = findSlot.next;
                }
            }
            return null;
        } else {
            return null;
        }
    }

    public static void main(String[] args){
        MyHash mainObject = new MyHash(20);
        mainObject.saveData("DaveLee", "01022223333");
        mainObject.saveData("fun-coding", "01033334444");
        mainObject.saveData("David", "01044445555");
        mainObject.saveData("Dave", "01055556666");
        System.out.println(mainObject.getData("Dave"));
    }

}
