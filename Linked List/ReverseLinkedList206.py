'''
206. Reverse Linked List
Easy

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 
Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?'''
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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev
    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        newHead = head
        if head.next:
            newHead = self.reverseListRecursive(head.next)
            head.next.next = head
        head.next = None
        return newHead

list1 = LinkedList()
list1.addNode(1)
list1.addNode(2)
list1.addNode(4)
list1.printList()


s1 = Solution()
list1.head = s1.reverseList(list1.head)
list1.printList()
list2 = LinkedList()
list2.addNode(1)
list2.addNode(2)
list2.addNode(4)
list2.printList()
list2.head = s1.reverseListRecursive(list2.head)
list2.printList()