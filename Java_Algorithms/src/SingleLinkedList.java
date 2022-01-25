public class SingleLinkedList<T> {
    public Node<T> head = null;

    public class Node<T> {
        T data;
        Node<T> next = null;

        //Constructor
        public Node(T data) {
            this.data = data;
        }
    }

    //Method
    public void addNode(T data) {
        if(head == null) {
            head = new Node<T>(data);
        } else {
            Node<T> node = this.head;
            while (node.next != null) { // 다음 노드가 있다
                node = node.next;
            }
            node.next = new Node<T>(data);
        }
    }

    public void printAll() {
        if(head != null) {
            Node<T> node = this.head;
            System.out.print(node.data + " ");
            while (node.next != null) {
                node = node.next;
                System.out.print(node.data + " ");
            }
        }
    }

    public Node<T> search(T data) {
        if(this.head == null) {
            return null;
        } else {
            Node<T> node = this.head;
            while(node != null){
                if(node.data == data) {
                    return node;
                } else {
                    node = node.next;
                }
            }
            return null;
        }
    }

    public void addNodeInside(T data, T isData) {
        Node<T> searchedNode = this.search(isData);

        if(searchedNode == null) { // 해당 값을 가진 노드가 없다!
            this.addNode(data);
        } else {
            Node<T> nextNode = searchedNode.next;
            searchedNode.next = new Node<T>(data); // 원래 있던 node의 next를 새로운 노드의 data를 가리키도록
            searchedNode.next.next = nextNode; // 노드 포인터가 다음 노드를 가리키게끔
        }
    }

    public boolean delNode(T isData) {
        if(this.head == null) {
            return false;
        } else {
            Node<T> node = this.head;
            if(node.data == isData) { // isData가 node head일 때
                this.head = this.head.next; // head는 다음 노드
                return true;
            } else {
                while (node.next != null) {
                    if(node.next.data == isData) { // 다음 노드의 data가 isData라면
                        node.next = node.next.next; // isData의 그다음 node에 연결!
                        return true;
                    }
                    node = node.next; // if문이 아니면 next로 노드 한 칸 옮김
                }
                return false; // if문 조건에 맞는 것이 없음
            }
        }
    }

    public static void main(String[] args) {
        SingleLinkedList<Integer> MyLinkedList = new SingleLinkedList<Integer>();
        MyLinkedList.addNode(1);
        MyLinkedList.addNode(2);
        MyLinkedList.addNode(3);

        MyLinkedList.addNodeInside(5, 1); // 1 뒤에 5 넣기

        MyLinkedList.addNodeInside(6, 3); // 맨 뒤에 6 넣기

        MyLinkedList.addNodeInside(7, 9); // 없는 노드에 넣으면?
        // 맨 뒤에 들어감!

        MyLinkedList.delNode(3);
        MyLinkedList.printAll(); // 1 5 2 6 7

    }

}
