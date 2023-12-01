class Node:
    def __init__(self, value) -> None:
        self.value = value

        self.next = None

class CircularLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def insert_after_tail(self, val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        new_node.next = self.head
        self.tail = new_node
        return

    def traverse(self):
        temp = self.head.next
        while(temp!=self.head):
            print(temp.value,end='->')
            temp = temp.next
        print(temp.value)
        return 
    def delete(self,idx):
        if idx==0:
            return None
        c = 0
        temp  = self.head
        while(c<idx):
            if c==idx-2:
                temp.next = temp.next.next
                return 
            temp = temp.next
            c+=1
        return 


cl = CircularLinkedList()
cl.insert_after_tail('A')
cl.insert_after_tail('B')
cl.insert_after_tail('C')
cl.insert_after_tail('D')
cl.insert_after_tail('E')
cl.traverse()
cl.delete(3)
cl.traverse()
