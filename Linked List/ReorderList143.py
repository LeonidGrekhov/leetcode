'''
143. Reorder List
Medium

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:


Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
 

Constraints:

The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
'''
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def addNode(self,node):
        node = ListNode(node)
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
    
    def printList(self):
        if self.head is None:
            print("no nodes")
        else:
            temp = self.head
            while temp:
                if temp.next:
                    end = "->"
                else:
                    end = "\n"
                print(temp.val,end=end)
                temp = temp.next
    
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find middle
        self.printHead(head)
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge two halfs
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        self.printHead(head)
        return head
    def printHead(self, head):
        temp = head
        while temp:
                if temp.next:
                    end = "->"
                else:
                    end = "\n"
                print(temp.val,end=end)
                temp = temp.next
    

list1 = LinkedList()
list1.addNode(1)
list1.addNode(2)
list1.addNode(3)
list1.addNode(4)
list1.addNode(5)
list1.printList()


s1 = Solution()
list1.head = s1.reorderList(list1.head)
list1.printList()
