class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyLL:
    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self,index:int) -> int:
        #assuming starting and ending as null;
        cur = self.left.next
        while cur and index > 0 :
            cur = cur.next
            index -= 1
        if cur and cur != self.right and index ==0: #cur exists and it is not out of bound and index ==0;
            return cur.val
        return -1        

    def addAtHead(self,val:int) -> None:
             newHead,next,prev = ListNode(val),self.left.next,self.left
             prev.next = newHead
             next.prev = newHead
             newHead.next = next
             newHead.prev = prev

    def addAtTail(self,val:int) -> None:
             newTail,next,prev = ListNode(val),self.right,self.right.prev
             prev.next = newTail
             next.prev = newTail
             newTail.next = next
             newTail.prev = prev

    def addAtIndex(self,index:int,val:int) -> None:
        cur  = self.left.next
        while cur and index > 0:
            cur = cur.next
            index-=1
        if cur and index==0 :
            newNode,prev,next = ListNode(val),cur.prev,cur
            prev.next = newNode
            next.prev = newNode
            newNode.prev=prev
            newNode.next=next



    def deleteAtIndex(self,index:int) -> None:  
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index-=1


        if cur and index == 0 and cur != self.right :

            prev,next = cur.prev,cur.next
            prev.next = next
            next.prev= prev

    def printdll(self) -> None:                
        cur = self.left.next
        while cur and cur != self.right:
            print(cur.val)
            cur = cur.next

init = MyLL()
init.addAtHead(4)
init.addAtHead(3)
init.addAtHead(2)
init.addAtHead(1)
init.addAtIndex(4,5)
init.addAtIndex(5,6)
init.addAtTail(9)
init.printdll()



