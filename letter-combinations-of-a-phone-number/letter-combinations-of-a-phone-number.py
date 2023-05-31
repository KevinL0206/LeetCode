class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]

        """
        phoneLetters = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
        }

        if len(digits) == 0:
            return []

        result = ['']
        for digit in digits:
            letters = phoneLetters[digit]
            temp = []
            for combination in result:
                for letter in letters:
                    temp.append(combination + letter)
            result = temp

        return result




