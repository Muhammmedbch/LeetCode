class Solution:
    def myPow(self, x: float, n: int) -> float:

        const = x
        is_negative = False

        if n < 0:
            is_negative = True
            n = abs(n)

        elif n == 0:
            return 1

        result = 1.0

        while n > 0:
            if n % 2 == 1:
                result *= x

            x *= x
            n //= 2

        if is_negative:
            result = 1 / result

        return result