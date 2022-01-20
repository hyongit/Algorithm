import java.util.*;

public class MyStack<T> {
    // [1] : ArrayList
    private ArrayList<T> stack = new ArrayList<T>();

    //[2] : push
    public void push(T item){
        stack.add(item);
    }

    //[3] : pop
    public T pop(){
        if (stack.isEmpty()) {
            return null;
        }
        else {
            //맨 마지막 인덱스 리턴
            return stack.remove(stack.size()-1);
        }
    }

    public boolean isEmpty(){
        return stack.isEmpty();
    }

    public static void main(String[] args){
        MyStack<Integer> ms = new MyStack<>();
        ms.push(1);
        ms.push(2);
        ms.push(3);

        System.out.println(ms.pop()); //3
        System.out.println(ms.pop()); //2
        System.out.println(ms.pop()); //1
        System.out.println(ms.isEmpty()); //true
    }
}
