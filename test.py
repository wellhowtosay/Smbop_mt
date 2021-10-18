class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplication(self, pHead):
        pre = pHead
        while pre:
            cur = pre
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
            pre.next = cur.next
            pre = cur.next
        return pHead


def get_list(ls):
    dummy = ListNode(0)
    p = dummy
    for i in ls:
        p.next = ListNode(i)
        p = p.next
    return dummy.next


ls = [1, 2, 2, 3, 3, 3, 3, 4, 5, 5]
h = get_list(ls)
s = Solution()
p = s.deleteDuplication(h)
ret = []
while p:
    ret.append(p.val)
    p = p.next
pass
