public class Node<T> {
    T data;
    // next 필드의 타입은 자신과 같은 객체를 참조할 수 있는 변수여야 하므로 Node<T> 타입
    public Node<T> next = null;

    public Node(T data){
        this.data = data;
    }

    public static void main(String[] args) {
        Node<Integer> node1 = new Node<Integer>(1);
        Node<Integer> node2 = new Node<Integer>(2);
        Node<Integer> node3 = new Node<Integer>(3);

        node1.next = node2;
        Node head = node1;
    }
}
