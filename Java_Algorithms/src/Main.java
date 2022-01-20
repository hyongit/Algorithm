import java.util.Stack;

public class Main{
    public static void main(String[] args){
        Stack<Integer> stack_int = new Stack<Integer>();

        stack_int.push(1);
        stack_int.push(2);
        stack_int.push(3);

        System.out.println(stack_int.pop()); //3
    }
}