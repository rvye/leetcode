class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # Testcase One

        l1 = [2, 4, 3]
        l2 = [5, 6, 4]

        z1 = int(l1[2]) + int(l2[2])
        z2 = int(l1[1]) + int(l2[1])
        z3 = int(l1[0]) + int(l2[0])


        if z2 >= 10:
            z1 += 1
            z2 = 0
        elif z3 >= 10:
            z3 = 0

        output = str(z1) + str(z2) + str(z3)

        output = [int(x) for x in str(output)][::-1]

        # print(output)

        # Testcase Two

        k1 = [0]
        k2 = [0]

        k = str(int(k1[0]) + int(k2[0]))
        k = [int(x) for x in str(k)][::-1]

        (k)
