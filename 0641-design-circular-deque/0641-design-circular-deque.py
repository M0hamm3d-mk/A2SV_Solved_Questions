class ListNode():
    def __init__(self,val=-1,next=None,prev=None):
        self.val = val
        self.next = next
        self.prev = prev
class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.front = ListNode()
        self.rear = self.front
        self.n = 0

    def insertFront(self, value: int) -> bool:
        if self.n >= self.k:
            return False
        if self.n == 0 or self.front.val == -1:
            node = ListNode(value)
            self.front = node
            self.rear = node
        else:
            node = ListNode(value,self.front,)
            self.front.prev = node
            self.front = node
        self.n += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.n >= self.k:
            return False
        
        if self.n == 0 or self.rear.val == -1:
            node = ListNode(value)
            self.rear = node
            self.front = node
        else:
            node = ListNode(value,None,self.rear)
            self.rear.next = node
            self.rear = node
        self.n += 1
        return True
        

    def deleteFront(self) -> bool:
        if self.n == 0 or  self.front.val == -1:
            return False
        self.front = self.front.next
        if self.front:
            self.front.prev = None 
        self.n -= 1
        return True

    def deleteLast(self) -> bool:
        if self.n == 0 or self.rear.val == -1 :
            return False
        self.rear = self.rear.prev
        self.n -= 1
        return True
        

    def getFront(self) -> int:
        if self.n == 0:
            return -1
        return self.front.val
        

    def getRear(self) -> int:
        if self.n == 0:
            return -1
        return self.rear.val
        

    def isEmpty(self) -> bool:
        return self.n == 0
        

    def isFull(self) -> bool:
        return self.n == self.k
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()