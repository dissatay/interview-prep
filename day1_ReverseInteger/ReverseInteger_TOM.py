class Solution(object):
    def reverse(self, x):

        if x == 0:
            return 0

            # get sign, make abs
        sign = 1 if (x >= 0) else -1
        x = abs(x)

        # get digits
        digits = []
        while x > 0:
            digit = x % 10
            x = x / 10
            digits.append(digit)

        # print(digits)
        digits.reverse

        i = 0
        while i < len(digits):
            if digits[i] == 0:
                i += 1
            else:
                break

        for j in range(i):
            digits.pop(0)

        # print(digits)

        if len(digits) == 0:
            return 0

        x = 0
        v = 0
        L = len(digits)
        for i in range(L):
            v = digits[L - i - 1] * pow(10, i)
            # print(str(digits[L-i-1]) + "  ,  " +str(v))
            x = x + v

        x = sign * x

        if x >= -pow(2, 31) and x <= (pow(2, 31) - 1):
            return x
        else:
            return 0

