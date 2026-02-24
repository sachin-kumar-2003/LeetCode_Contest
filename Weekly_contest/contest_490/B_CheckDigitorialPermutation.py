class Solution:
    def isDigitorialPermutation(self, n: int) -> bool:
        def fact(number):
            factorial = 1
            for i in range(1, number+1):
                factorial = ( factorial * i)
            return factorial 
        total_fact = 0
        num = n
        while n:
            rem = n % 10
            total_fact += fact(rem)
            n = n // 10
        org = list(str(num))
        arr = list(str(total_fact))
        print(org)
        print(arr)
        org.sort()
        arr.sort()
        return org == arr