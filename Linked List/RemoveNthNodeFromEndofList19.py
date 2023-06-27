'''
19. Remove Nth Node From End of List
Medium

Given the head of a linked list, remove the nth node 
from the end of the list and return its head.

Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

Follow up: Could you do this in one pass?
'''
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        while n > 0 and right:
            right = right.next
            n -= 1
        while right:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next
    
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
list1 = LinkedList()
list1.addNode(1)
list1.addNode(1)
list1.addNode(2)
list1.addNode(3)
list1.addNode(4)
list1.addNode(5)
list1.printList()
s1 = Solution()
list1.head = s1.removeNthFromEnd(list1.head, n=2)
list1.printList()