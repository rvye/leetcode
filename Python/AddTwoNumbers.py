class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = [2, 4, 3]
        l2 = [5, 6, 4]


        for i in range(3):
            o = l1[i] + l2[i]
            o = [{l1[i]} + {l2[i]}]
