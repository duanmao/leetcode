# https://leetcode.com/problems/integer-to-english-words/discuss/70632/Recursive-Python
# most concise one

# Try to get rid of most of the ".strip()"
class Solution:
    def numberToWords(self, num: int) -> str:
        LESS_THAN_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        TENS = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        THOUSANDS = ["", "Thousand", "Million", "Billion"]

        def convert(num):
            if num == 0:
                return []
            elif num < 20:
                return [LESS_THAN_20[num]]
            elif num < 100:
                tens = int(num / 10)
                return [TENS[tens]] + convert(int(num % 10))
            elif num < 1000:
                hundreds = int(num / 100)
                return convert(hundreds) + ["Hundred"] + convert(int(num % 100))

        if num == 0: return "Zero"
        i = 0
        word = ""
        while num:
            if num % 1000: # important for cases like 1000000
                word = " ".join([" ".join(convert(int(num % 1000))), THOUSANDS[i], word])
            num = int(num / 1000)
            i += 1

        return word.strip()


class Solution:
    def numberToWords(self, num: int) -> str:
        LESS_THAN_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        TENS = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        THOUSANDS = ["", "Thousand", "Million", "Billion"]
        
        def convert(num):
            if num < 20:
                return LESS_THAN_20[num]
            elif num < 100:
                tens = int(num / 10)
                return " ".join([TENS[tens], convert(int(num % 10))]).strip()
            else:
                hundreds = int(num / 100)
                return " ".join([convert(hundreds), "Hundred", convert(int(num % 100))]).strip()
        
        if num == 0: return "Zero"
        i = 0
        word = ""
        while num:
            if num % 1000: # important for cases like 1000000
                word = " ".join([convert(int(num % 1000)), THOUSANDS[i], word])
            num = int(num / 1000)
            i += 1
            
        return word.strip()
