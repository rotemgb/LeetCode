# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:  
    
    def addTwoNumbers(self, l1, l2, c = 0):
        # add the 2 digits and the carry (c)
        val = l1.val + l2.val + c   
        # update the carry
        if val >= 10:
            val = val - 10
            c = 1
        else:
            c = 0
        # create a new node with the sum
        res = ListNode(val)
        # if there are still digits in any of the linked lists, keep recurring
        # if one of the lists is done, create a dummy node with value 0 and keep recurring
        if l1.next or l2.next:
            if l1.next is None:
                l1.next = ListNode(0)
            elif l2.next is None:
                l2.next = ListNode(0)
                
            res.next = self.addTwoNumbers(l1.next, l2.next, c)
        # if both lists are done, but c is not zero, create another node for c
        elif c != 0:
            res.next = ListNode(1)
            
        return res
        
