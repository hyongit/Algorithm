class Node {
    Node left;
    Node right;
    int value;
    // 생성자
    public Node(int data) {
        this.value = data;
        this.left = null;
        this.right = null;
    }
}

public class NodeMgmt {
    Node head = null;

    // 메서드 : 트리에 데이터 넣음
    public boolean insertNode(int data) {
        // CASE1 : Node가 하나도 없을 때
        if (this.head == null) {
            this.head = new Node(data);
        } else {
            // CASE2 : Node가 하나 이상 들어가 있을 때
            Node findNode = this.head;
            while (true) {
                // CASE2-1 : 현재 Node의 왼쪽에 Node가 들어가야 할 때
                if (data < findNode.value) {
                    if (findNode.left != null) {
                        findNode = findNode.left; // 한 칸 내려가서 비교
                    } else {
                        findNode.left = new Node(data);
                        break;
                    }
                    // CASE2-2 : 현재 Node의 오른쪽에 Node가 들어가야 할 때
                } else {
                    if (findNode.right != null) {
                        findNode = findNode.right;
                    } else {
                        findNode.right = new Node(data);
                        break;
                    }
                }

            }
        }
        return true;
    }

    public Node search(int data) {
        // CASE1 : Node가 하나도 없을 때
        if (this.head == null) {
            return null;
            // CASE2 : Node가 하나 이상일 때
        } else {
            Node findNode = this.head;
            while (findNode != null) {
                if (findNode.value == data) {
                    return findNode;
                } else if (data < findNode.value) {
                    findNode = findNode.left;
                } else {
                    findNode = findNode.right;
                }
            }
            return null;
        }
    }

    public boolean delete(int value) {
        boolean searched = false;

        Node currParentNode = this.head;
        Node currNode = this.head;

        // 코너 케이스1 : Node가 하나도 없을 때
        if(this.head == null){
            return false;
        // 코너 케이스2 : Node가 단지 하나만 있고, 해당 Node가 삭제할 Node일 때때
        } else {
            if(this.head.value == value && this.head.left == null && this.head.right == null){
                this.head = null;
                return true;
            }

            while(currNode != null){
                if(currNode.value == value){
                    searched = true;
                    break;
                } else if (value < currNode.value) {
                    currParentNode = currNode; // currNode를 Parent로 만둘고
                    currNode = currNode.left; // 왼쪽 아래 노드를 currNode로 만듦
                } else {
                    currParentNode = currNode;
                    currNode = currNode.right;
                }
            }

            if(searched == false) {
                return false;
            }
        }

        //여기까지 실행되면,
        //currNode에는 해당 데이터를 갖고 있는 Node,
        //currParentNode에는 해당 데이터를 가지고 있는 Node의 부모 Node
        //다 찾은거임

        //Case 1 : 삭제할 Node가 Leaf Node인 경우
        if(currNode.left == null && currNode.right == null){
            // currNode = value, 왼쪽에 연결된 상황
            if(value < currParentNode.value){
                currParentNode.left = null; // ParentNode의 left를 null로
                currNode = null; // 안 써도 무방
            } else {
                currParentNode.right = null;
                currNode = null;
            }
        // Case2-1: 삭제할 Node가 Child Node를 한 개 가지고 있을 경우 (왼쪽에 Child Node가 있을 경우)
        } else if (currNode.left != null && currNode.right == null) {
            // parent - curr(왼) - child(왼)
            if(value < currParentNode.value) {
                // 현재 노드 삭제, ParentNode를 currNode의 자식과 이어줌
                currParentNode.left = currNode.left;
                currNode = null;
            // parent - curr(오) - child(왼)
            } else {
                currParentNode.right = currNode.left;
                currNode = null;
            }
        // Case2-1: 삭제할 Node가 Child Node를 한 개 가지고 있을 경우 (오른쪽에 Child Node가 있을 경우)
        } else if (currNode.left == null && currNode.right != null) {
            // parent - curr(왼) - child(오)
            if(value < currParentNode.value) {
                currParentNode.left = currNode.right;
                currNode = null;
            // parent - curr(오) - child(오)
            } else {
                currParentNode.right = currNode.right;
                currNode = null;
            }
            return true;
        // Case3-1 : 삭제할 Node가 Child Node를 두 개 가지고 있고, 삭제할 Node가 부모 Node의 왼쪽에 있음
        } else {

            if (value < currParentNode.value) {
                Node changeNode = currNode.right; // 오른쪽 자식을 changeNode로 (head 역할)
                Node changeParentNode = currNode.right; // 오른쪽 자식을 changeNode의 Parent로

                while(changeNode.left != null) {
                    changeParentNode = changeNode;
                    changeNode = changeNode.left;
                }
                //여기까지 실행되면, changeNode에는 삭제할 Node의 오른쪽 Node 중에서,
                //가장 작은 값을 가진 Node가 들어있음 !!
                if(changeNode.right != null) {
                    //Case 3-1-2: changeNode의 오른쪽 Child Node가 있을 때
                    changeParentNode.left = changeNode.right;
                } else {
                    //Case 3-1-1: changeNode의 Child Node가 없을 때
                    changeParentNode.left = null;
                }

                //currParentNode의 왼쪽 Child Node에, 삭제할 Node의 오른쪽 자식 중,
                //가장 작은 값을 가진 changeNode를 연결 (currNode를 changeNode로 변경)
                currParentNode.left = changeNode;

                //parentNode의 왼쪽 Child Node가 현재, changeNode이고,
                //changeNode의 왼쪽/오른쪽 Child Node를 모두, 삭제할 currNode의
                //기존 왼쪽/오른쪽 Node로 변경
                changeNode.right = currNode.right;
                changeNode.left = currNode.left;

                currNode = null; // 안 써도 무방, 노드 삭제!
            // Case3-2 : 삭제할 Node가 Child Node를 두 개 가지고 있고, 삭제할 Node가 부모 Node의 오른쪽에 있음
            } else {
                Node changeNode = currNode.right; // 오른쪽 자식을 changeNode로 (head 역할)
                Node changeParentNode = currNode.right; // 오른쪽 자식을 changeNode의 Parent로

                while(changeNode.left != null) {
                    changeParentNode = changeNode;
                    changeNode = changeNode.left;
                }

                if(changeNode.right != null) {
                    //Case 3-2-2: changeNode의 오른쪽 Child Node가 있을 때
                    changeParentNode.left = changeNode.right;
                } else {
                    //Case 3-2-1: changeNode의 Child Node가 없을 때
                    changeParentNode.left = null;
                }

                //currParentNode의 오른쪽 Child Node에, 삭제할 Node의 오른쪽 자식 중,
                //가장 작은 값을 가진 changeNode를 연결 (currNode를 changeNode로 변경)
                currParentNode.right = changeNode;

                changeNode.right = currNode.right;
                changeNode.left = currNode.left;

                currNode = null;
            }

            return true;
        }
        return searched;
    }
    public static void main(String[] args) {
        NodeMgmt myTree = new NodeMgmt();
        myTree.insertNode(10);
        myTree.insertNode(15);
        myTree.insertNode(13);
        myTree.insertNode(11);
        myTree.insertNode(14);
        myTree.insertNode(18);
        myTree.insertNode(16);
        myTree.insertNode(17);
        myTree.insertNode(19);
        myTree.insertNode(7);
        myTree.insertNode(6);
        myTree.insertNode(8);

        System.out.println(myTree.delete(15));
        System.out.println("HEAD: " + myTree.head.value);
        System.out.println("HEAD LEFT: " + myTree.head.left.value);
        System.out.println("HEAD LEFT LEFT: " + myTree.head.left.left.value);
        System.out.println("HEAD LEFT RIGHT: " + myTree.head.left.right.value);

        System.out.println("HEAD RIGHT: " + myTree.head.right.value);
        System.out.println("HEAD RIGHT LEFT: " + myTree.head.right.left.value);
        System.out.println("HEAD RIGHT RIGHT: " + myTree.head.right.right.value);

        System.out.println("HEAD RIGHT RIGHT LEFT: " + myTree.head.right.right.left.value);
        System.out.println("HEAD RIGHT RIGHT RIGHT: " + myTree.head.right.right.right.value);

    }
}
