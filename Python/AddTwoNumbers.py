class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = [2, 4, 3]
        l2 = [5, 6, 4]

        z1 = int({l1[2]}) + int({l2[2]})
        z2 = int({l1[1]}) + int({l2[1]})
        z3 = int({l1[0]}) + int({l2[0]})
    
        z1 = str(z1)
        z2 = str(z2)
        z3 = str(z3)

        out = f"{z1}{z2}{z3}"
        print(out)
