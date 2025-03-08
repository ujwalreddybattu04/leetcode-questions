class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Edge case: handling overflow
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX  # Overflow case

        # Determine the sign of the result
        negative = (dividend < 0) ^ (divisor < 0)

        # Work with positive values
        dividend, divisor = abs(dividend), abs(divisor)

        quotient = 0
        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1  # Double the temp divisor
                multiple <<= 1  # Double the quotient contribution

            dividend -= temp  # Subtract the largest found multiple
            quotient += multiple  # Add to the result

        # Apply the sign
        return -quotient if negative else quotient

        