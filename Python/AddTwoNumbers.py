class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = [2, 4, 3]
        l2 = [5, 6, 4]

        z1 = str(int(l1[2]) + int(l2[2]))
        z2 = str(int(l1[1]) + int(l2[1]))
        z3 = str(int(l1[0]) + int(l2[0]))


        print(z1)
        print(z2)
        print(z3)
