
def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        ugly = [2, 3, 5]
        for factor in ugly:
            while n % factor == 0:
                n /= factor
        return n == 1

