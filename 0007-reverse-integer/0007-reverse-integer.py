class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        num = x
        reversed_number =0 
        sign=0
        if num<0:
            sign=-1
            num=-1*num

        while num !=0:
            digit = num%10
            reversed_number = reversed_number*10+digit
            num=num//10
        
        if sign==-1:
            reversed_number=reversed_number*(-1)
        if reversed_number >(-2**31) and reversed_number<((2**31)-1) :
            return reversed_number
        else:
            return 0
