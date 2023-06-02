class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False

        x = [int(y) for y in str(x)]
        i = len(x)
        j = 0
        reverse =[]
        
        while i > 0:
            reverse.append(x[i-1])
            i -= 1
            j += 1

        if reverse == x:
            return True
        else:
            return False