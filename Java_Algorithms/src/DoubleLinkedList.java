public class DoubleLinkedList<T> {
    public Node<T> head = null;
    public Node<T> tail = null;

    public class Node<T> {
        T data;
        Node<T> prev = null;
        Node<T> next = null;

        //생성자
        public Node(T data) {
            this.data = data;
        }
    }

    public void addNode(T data) {
        if(this.head == null) { // head가 없을 때
            this.head = new Node<T>(data); // Node 하나 생성해서 넣어 줌
            this.tail = this.head; // 데이터가 하나이므로 tail도 head
        } else {
            Node<T> node = this.head; // 노드가 있을 때
            while(node.next != null) {
                node = node.next; // 끝까지 노드 이동
            }
            node.next = new Node<T>(data);
            node.next.prev = node; // node의 prev는 그 전 node를 가리켜야 함
            this.tail = node.next;
        }
    }

    public void printAll() {
        if (this.head != null) {
            Node<T> node = this.head;
            System.out.println(node.data); // head 출력
            while (node.next != null) {
                node = node.next;
                System.out.println(node.data);
            }
        }
    }

    // 원하는 데이터 Head에서부터 찾기
    public T searchFromHead(T isData) {
        if (this.head == null) {
            return null;
        } else {
            Node<T> node = this.head;
            while(node != null){
                if(node.data == isData) {
                    return node.data;
                } else {
                    node = node.next;
                }
            }
            return null; // 해당 데이터가 없다!
        }
    }

    //원하는 데이터 tail에서부터 찾기
    public T searchFromTail(T isData) {
        if(this.head == null) {
            return null;
        } else {
            Node<T> node = this.tail;
            while(node != null) {
                if(node.data==isData){
                    return node.data;
                } else {
                    node = node.prev;
                }
            }
            return null; // 해당 데이터가 없다!
        }
    }

    public boolean insertToFront(T existedData, T addData) {
        if(this.head == null) { //head가 없을 경우
            this.head = new Node<T>(addData);
            this.tail = this.head;
            return true;
        } else if (this.head.data == existedData) { //head가 내가 찾는 node일 경우
            Node<T> newHead = new Node<T>(addData);
            newHead.next = this.head;
            this.head = newHead;
            return true;
        } else { //head 외에 나머지 데이터가 내가 찾는 node
            Node<T> node = this.head;
            while (node != null) {
                if(node.data == existedData) {
                    Node<T> nodePrev = node.prev; // node.prev가 가리키는 아이 (전노드)를 변수에 넣어 놈
                    //nodePrev.next가 새로 생성한 노드임 !
                    nodePrev.next = new Node<T>(addData);
                    nodePrev.next.next = node;

                    nodePrev.next.prev = nodePrev;
                    node.prev = nodePrev.next;
                    return true;
                } else {
                    node = node.next;
                }
            }
            return false;
        }
    }

    public static void main(String[] args) {
        DoubleLinkedList<Integer> MyLinkedList = new DoubleLinkedList<Integer>();
        MyLinkedList.addNode(1);
        MyLinkedList.addNode(2);
        MyLinkedList.addNode(3);
        MyLinkedList.addNode(4);
        MyLinkedList.addNode(5);
        MyLinkedList.printAll();
        System.out.println("-----------------");

        MyLinkedList.insertToFront(3,2);
        MyLinkedList.printAll();
        System.out.println("-----------------");

        MyLinkedList.insertToFront(6,2);
        MyLinkedList.insertToFront(1,0);
        MyLinkedList.printAll();
        System.out.println("-----------------");

        MyLinkedList.addNode(6);
        MyLinkedList.printAll();
    }
}