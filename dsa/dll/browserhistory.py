class ListNode:
    def __init__(self,val, prev = None,next = None):
        self.val = val
        self.prev = prev
        self.next = next


class BrowserHistory:
    def __init__(self,val:str):
        self.i=0 #index pointer
        self.len = 1
        self.cur = ListNode(val)

    def visit(self,url:str) -> None:
        self.cur = ListNode(url,self.cur)
        self.cur.prev.next = self.cur
        # print(self.cur.val)
        self.i+=1

    def forward(self,steps:int) -> str:
        while self.cur.next and steps>0:
            self.cur = self.cur.next
            steps -= 1
        # print(self.cur.val)
        return self.cur.val

    def backward(self,steps:int) -> str:            
        while self.cur.prev and steps>0:
            self.cur = self.cur.prev
            steps -= 1
        # print(self.cur.val)
        return self.cur.val

    def printf(self):
        while self.cur.prev and self.i>0:
            self.cur = self.cur.prev
            self.i -= 1    
        while self.cur.next:
            print(self.cur.val)
            self.cur = self.cur.next

l = BrowserHistory('a')
l.visit('b')
l.visit('c')
l.visit('d')
l.visit('e')
l.visit('f')
l.visit('c')
# l.backward(5)
# l.forward(3)
l.printf()

