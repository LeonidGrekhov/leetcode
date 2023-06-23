'''
83. Remove Duplicates from Sorted List
Easy

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Example 1:

Input: head = [1,1,2]
Output: [1,2]
Example 2:

Input: head = [1,1,2,3,3]
Output: [1,2,3]

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
'''
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            cur = cur.next
        return head

# Function to create a linked list from a list
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
list1.addNode(3)
list1.printList()
s1 = Solution()
list1.head = s1.deleteDuplicates(list1.head)
list1.printList()