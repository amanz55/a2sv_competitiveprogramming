class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            return 1/(self.myPow(x,abs(n)))
        if n==0:
            return 1
        if n % 2 == 0:
            rr = self.myPow(x, n/2)
            return rr*rr
        return x*self.myPow(x,n-1)