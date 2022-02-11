import java.util.*;
import java.io.*;

//Comparable 구현 방법
//정렬할 객체에 Comparable interface를 implements 후, CompareTo() 메서드를 오버라이드 해서 사용

class Student implements Comparable<Student> {
    String name;
    int kor;
    int eng;
    int math;

    public Student(String name, int kor, int eng, int math) {
        this.name = name;
        this.kor = kor;
        this.eng = eng;
        this.math = math;
    }

    //오름차순 정렬
    //현재 객체 < 파라미터로 넘어온 객체 : 음수 리턴
    //현재 객체 == 파라미터로 넘어온 객체 : 0 리턴
    //현재 객체 > 파라미터로 넘어온 객체 : 양수 리턴
    //양수 리턴 시 객체 자리 변경, 내림차순 시 부호 방향 반대로!
    @Override
    public int compareTo(Student student) {
        if (this.kor < student.kor) {
            return 1; //kor에 대해서 내림차순
        } else if (this.kor == student.kor) {
            if (this.eng > student.eng) {
                return 1; //kor 같으면 eng에 대해서는 오름차순
            } else if (this.eng == student.eng) {
                if (this.math < student.math) {
                    return 1; //eng 같으면 math에 대해서는 내림차순
                } else if (this.math == student.math) {
                    //this.name이 student.name보다 사전순으로 뒤에 올 경우 양수 반환
                    if (this.name.compareTo(student.name) > 0) {
                        return 1; //모든 점수가 같으면 사전 순으로 증가하는 순
                    }
                }
            }
        }
        return -1; // this.kor이 student.kor보다 클 경우 자리 바꿀 필요 없음!
    }
}

public class BOJ_10825 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        String name;
        int kor,math,eng;
        Student student;
        ArrayList<Student> slist = new ArrayList<Student>();

        for(int i=0; i<n; i++){
            name = sc.next();
            kor = sc.nextInt();
            eng = sc.nextInt();
            math = sc.nextInt();
            student = new Student(name,kor,eng,math);
            slist.add(student);
        }

        Collections.sort(slist);
        for(int i=0; i<n; i++){
            System.out.println(slist.get(i).name);
        }
    }
}