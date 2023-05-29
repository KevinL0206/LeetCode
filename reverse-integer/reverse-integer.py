class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int


        """

       
        is_negative = False
        if x < 0:
            is_negative = True
            x = -x

        
        reversed_num = 0
        while x > 0:
            
            if reversed_num > (2**31 - 1) // 10:
                return 0
            reversed_num = reversed_num * 10 + x % 10
            x //= 10

        return -reversed_num if is_negative else reversed_num