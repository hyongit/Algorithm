public class CloseHash {
    public Slot[] hashTable;

    //생성자
    public CloseHash(Integer size) {
        this.hashTable = new Slot[size];
    }

    //내부 클래스
    public class Slot {
        String key;
        String value;
        MyHash.Slot next; //링크드 리스트 포인터
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
            if (this.hashTable[address].key == key) { // key 찾았으면 value값만 바꿔주기
                this.hashTable[address].value = value;
                return true;
            } else { // 아니면 다음 Slot으로 옮기면서 key 동일할 때까지 찾아주기
                Integer currAddress = address + 1; // 한 칸씩 이동
                while(this.hashTable[currAddress] != null) { //null이 아닐 때까지만
                    if(this.hashTable[currAddress].key == key) { // key 찾았으면 value값 바꿔주기
                        this.hashTable[currAddress].value = value;
                    } else {
                        currAddress++;
                        if (currAddress >= this.hashTable.length) { //해쉬테이블의 길이 이상으로 갈 시
                            return false;
                        }
                    }
                }
                // 충돌 발생 했지만, 해당 key 없음!
                this.hashTable[currAddress] = new Slot(key, value);
                return true;
            }
        } else { // 충돌 안 발생
            this.hashTable[address] = new Slot(key, value);
        }
        return true;
    }

    public String getData(String key) {
        Integer address = this.hashFunc(key);
        if(this.hashTable[address] != null) { // 해당 address에 객체 있다!
            if(this.hashTable[address].key == key) { // key 찾았으면 value 리턴
                return this.hashTable[address].value;
            } else { // 아니면 주소 이동하면서 key 찾아야함
                Integer currAddress = address + 1;
                while(this.hashTable[address] != null) { // null이 아닐 때까지만
                    if(this.hashTable[address].key == key) { // 동일 key 찾았으면 value 리턴
                        return this.hashTable[address].value;
                    } else { // 아니면 주소 다음칸으로 이동
                        currAddress++;
                        if(currAddress >= this.hashTable.length) { // 테이블 밖으로 이동 시
                            return null; //null 리턴
                        }
                    }
                }
                return null; // 해당 key에 대한 value가 없다
            }
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
