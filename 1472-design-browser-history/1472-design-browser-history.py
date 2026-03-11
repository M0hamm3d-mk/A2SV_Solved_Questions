class Node():
    def __init__(self, val='',next=None,prev=None):
        self.val = val
        self.next = None
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.home = Node(homepage)
        self.tail = self.home
        self.curr = self.home

    def visit(self, url: str) -> None:
        node = Node(url,None,self.curr)
        self.curr.next = node
        self.tail = node
        self.curr = node

    def back(self, steps: int) -> str:
    
        while self.curr.prev and steps:
            self.curr = self.curr.prev
            steps -= 1

        return self.curr.val

    def forward(self, steps: int) -> str:

        while self.curr.next and steps:
            self.curr = self.curr.next
            steps -= 1

        return self.curr.val



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)