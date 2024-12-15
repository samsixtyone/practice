class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class mylink:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = None
            return 

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node
        new_node.next = None

    def display(self):
        current = self.head
        while current:
            print (current.data, end=" -> ")
            current = current.next

    def checkCycle(self) -> bool:
        dummy = Node(1)
        dummy.next = head
        slow = fast = dummy 

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if slow is fast:
                return True
        return False

    def delete_dups(self):
        current = head
        while current and current.next: 
            if current.value == current.next.vaule:
                current.next = current.next.next
            else:
                current = current.next
        return head

    def merge_lists(self, list1, list2):
        d = Node(1)
        current = d
        if list1 and list2:
            if list1.value < list2.value:
                current.next = list1
                current = list1
                list1 = list1.next
            else:
                current.next = list2
                current = list2
                list2 = list2.next
        
        current.next  = list1 if list1 else list2
        return d.next   # actual head

    def add_gcd(self):
        prev    = head
        current = head.next
        while current:
            gcd = math.gcd(prev.value, current.value)
            g   = Node(gcd)
            prev.next = g
            g.next = current
            prev = current
            current = current.next
    return head


if __name__ == "__main__":
    ll = mylink()
    ll.append(1)
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.display()
    
