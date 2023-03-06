# Kinda right, but WIP

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = [9,9,9,9,9,9,9]
        l2 = [9,9,9,9]

        

        if len(l1) == 3 or len(l2) == 3:
            al1 = f"{l1[2]}" + f"{l1[1]}" + f"{l1[0]}"
            al2 = f"{l2[2]}" + f"{l2[1]}" + f"{l2[0]}"

            al1 = int(al1)
            al2 = int(al2)

            output = al1 + al2
            output = [int(x) for x in str(output)][::-1]
            
            print(output)
        
        if len(l1) == 1 or len(l2) == 1:
            al1 = f"{l1[0]}"
            al2 = f"{l2[0]}"

            al1 = int(al1)
            al2 = int(al2)

            output = al1 + al2
            output = [int(x) for x in str(output)][::-1]
            
            print(output)
        if len(l1) == 7 or len(l2) == 4:
            al1 = f"{l1[6]}" + f"{l1[5]}" + f"{l1[4]}" + f"{l1[3]}" + f"{l1[2]}" + f"{l1[1]}" + f"{l1[0]}"
            al2 = f"{l2[3]}" + f"{l2[2]}" + f"{l2[1]}" + f"{l2[0]}"

            al1 = int(al1)
            al2 = int(al2)

            output = al1 + al2
            output = [int(x) for x in str(output)][::-1]
            
            print(output)
        
