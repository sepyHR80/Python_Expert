class Solution:
    def isPalindrome(self, x: int) -> bool:
            if x < 0 :
                return False
                
            else :
                num = str(x)
                list_1 = list(num)
                return True if int((''.join(list_1[::-1]))) == x else False
     