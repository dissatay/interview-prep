# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1, l2):
        head = 0;
        prevNode = 0

        if (l1 is None) and (l2 is None):
            return l1

        while (l1 is not None) and (l2 is not None):
            newVal = 0;
            loadTwice = False;
            if l1.val < l2.val:
                newVal = l1.val
                l1 = l1.next
            elif l1.val > l2.val:
                newVal = l2.val
                l2 = l2.next
            else:
                newVal = l1.val
                loadTwice = True
                l1 = l1.next
                l2 = l2.next
                # create new node
            newNode = ListNode(newVal)
            if prevNode != 0:
                prevNode.next = newNode
            else:
                head = newNode
                # linking the list so the new node is connected
            prevNode = newNode
            if loadTwice:
                newNode = ListNode(newVal)
                prevNode.next = newNode
                prevNode = newNode

        if (l1 is None) and (l2 is None):
            return head

        ll = l1 if (l1 is not None) else l2

        if prevNode != 0:
            prevNode.next = ll
        else:
            head = ll

        return head
