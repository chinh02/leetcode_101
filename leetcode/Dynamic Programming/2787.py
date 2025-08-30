n = 10
x = 2

def numberOfWays(n: int, x: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (n+1)
        dp[0] = 1

        for i in range(1,n+1):
            val = i**x
            print(val)
            if val > n:
                break
            for j in range(n, val-1, -1):
                print(j)
                dp[j] = (dp[j] + dp[j - val])
                print(dp)
        return dp[n]

print(numberOfWays(n,x))