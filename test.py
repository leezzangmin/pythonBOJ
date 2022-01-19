# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans=[head.val]
        while True:
           # print(head,'asdf')
            if ans[-1]!=head.val:
                ans.append(head.val)
            if head.next==None:
                break
            head=head.next
        print(ans)
        return ans

a=Solution()
a.deleteDuplicates(  ListNode{val: 1, next: ListNode{val: 1, next: ListNode{val: 2, next: None} } }  )