## 序列型动态规划源代码

### LeetCode 300

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        #max_len = 1
        # dp[i] 代表以nums[i]j结尾，最长的LIS是多少
        dp = [1 for _ in range(n)]

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            #max_len = max(max_len, dp[i])
                    
        return max_len
```

### LeetCode 55

```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        n = len(nums)
        # dp = [False for _ in range(n)]
        # dp[0] = True
        # for i in range(1, n):
        #     for j in range(i):
        #         if dp[j] and j + nums[j] >= i:
        #             dp[i] = True
        #             break
        # return dp[n - 1]
        max_far = nums[0]
        for i in range(1, n):
            if i <= max_far and nums[i] + i >= max_far:
                max_far = nums[i] + i
        return max_far >= n - 1
```

### LeetCode 45

```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        # dp = [1e8 for _ in range(n)]
        # dp[0] = 0
        # for i in range(1, n):
        #     for j in range(i):
        #         if dp[j] != 1e8 and j + nums[j] >= i:
        #             dp[i] = min(dp[i], dp[j] + 1)
        # return dp[n - 1]
        start, end = 0, 0
        jumps = 0
        while end < n - 1:
            jumps += 1
            max_far = end
            # 尝试当前可以跳到的最远的位置所有之前的位置
            # 开始寻找下一次跳跃找到下一个可以跳到最远的地方
            for i in range(start, end + 1):
                if i + nums[i] > max_far:
                    max_far = i + nums[i]
            start = end + 1
            end = max_far
        return jumps
```

### LeetCode 123
```python
# 解法一
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        p1 = [0 for _ in range(n)]
        p2 = [0 for _ in range(n)]
        # 从前往后找一个当前位置之前可以获得的最大收益
        min_price = prices[0]
        for i in range(1, n):
            min_price = min(min_price, prices[i])
            p1[i] = max(p1[i - 1], prices[i] - min_price)
        
        # 注意并不一定是当前这个位置买或者卖，是当前位置之前或之后的任意一次买卖交易的最大收益
        # 从后往前找一个当前位置之后可以获得的最大收益
        max_price = prices[-1]
        for j in range(n - 2, -1, -1):
            max_price = max(max_price, prices[j])
            p2[j] = max(p2[j + 1], max_price - prices[j])
        
        res = 0
        for i in range(n):
            res = max(res, p1[i] + p2[i])
        return res
        

# 解法二
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        # 完成两次交易总共有会处于五种状态
        # 未持有 -> 第一次持有 -> 第一次卖出 -> 第二次持有 -> 第二次卖出
        # 分别对应0次交易，1次交易，2次交易
        dp = [[0 for j in range(5 + 1)] for i in range(n + 1)]

        # 初始化
        for j in range(1, 6):
            dp[0][j] = -1
        dp[0][1] = 0
        for i in range(1, n + 1):
            # 手中未持有股票
            for j in range(1, 6, 2):
                # 前一天手中也未持有股票
                dp[i][j] = dp[i - 1][j]
                # 前一天持有了（并不是前一天买入，可能是很多天前买入的），今天卖了
                if j > 1 and i > 1 and dp[i - 1][j - 1] != -1:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + prices[i - 1] - prices[i - 2])

            # 手中持有股票
            for j in range(2, 6, 2):
                # 前一天未持有，今天买入的
                dp[i][j] = dp[i -1][j - 1]
                # 前一天也持有了，今天计算收益
                if i > 1 and dp[i -1][j] != -1:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j] + prices[i - 1] - prices[i - 2])

        res = 0
        # 收益的计算只能是三个点，不买股票  第一次卖出  第二次卖出
        for j in range(1, 6, 2):
            res = max(res, dp[n][j])
        return res
```

### LeetCode 188

```python
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        if k > n // 2:
            res = 0
            for i in range(n - 1):
                res += max(prices[i + 1] - prices[i], 0)
            return res
        # 完成两次交易总共有会处于五种状态
        # 未持有 -> 第一次持有 -> 第一次卖出 -> 第二次持有 -> 第二次卖出 ...... -> 第2k + 1 次
        # 分别对应0次交易，1次交易，2次交易
        dp = [[0 for j in range(2 * k + 1 + 1)] for i in range(n + 1)]
        
        # 初始化
        for j in range(1, 2 * k + 1 + 1):
            dp[0][j] = -1
        dp[0][1] = 0
        for i in range(1, n + 1):
            # 手中未持有股票
            for j in range(1, 2 * k + 1 + 1, 2):
                # 前一天手中也未持有股票
                dp[i][j] = dp[i - 1][j]
                # 前一天持有了（并不是前一天买入，可能是很多天前买入的），今天卖了
                if j > 1 and i > 1 and dp[i - 1][j - 1] != -1:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + prices[i - 1] - prices[i - 2])
                    
            # 手中持有股票
            for j in range(2, 2 * k + 1 + 1, 2):
                # 前一天未持有，今天买入的
                dp[i][j] = dp[i -1][j - 1]
                # 前一天也持有了，今天计算收益
                if i > 1 and dp[i -1][j] != -1:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j] + prices[i - 1] - prices[i - 2])
                    
        res = 0
        # 收益的计算只能是三个点，不买股票  第一次卖出  第二次卖出 ...... -> 第2k + 1 次
        for j in range(1, 2 * k + 1 + 1, 2):
            res = max(res, dp[n][j])
        return res
```



### LeetCode 123

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        dp = [[0 for j in range(5)] for i in range(n)]

        for i in range(1, n):            
            #手中未持有股票的状态 0/2/4
            for j in range(2,5,2):
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + prices[i] - prices[i-1])

            #手中持有股票的状态 1/3 
            for j in range(1,5,2):
                dp[i][j] = max(dp[i][j-1], dp[i-1][j] + prices[i] - prices[i-1])

        res = 0
        for j in range(0,5,2):   #j => 0/2/4 未持有的时候才能计算收益
            res = max(res, dp[n-1][j])   #最后一row的最大值
        return res
```

### LeetCode 123
# 自研算法 不正确
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)

        dp = [[0 for j in range(3)] for i in range(n)]
        k = 0
        #for 循环 从第一天开始循环
        for i in range(1, n):            
            #第一次交易
            j = 1
            dp[i][j] = max(dp[i][j-1], dp[i-1][j]+prices[i]-prices[i-1])

            #第二次交易
            j = 2
            #dp[i][j] = max(dp[i-1][j-1]+prices[i]-prices[i-1], max(dp[i][j-1], dp[i-1][j]+prices[i]-prices[i-1]))
            dp[i][j] = max(dp[i][j-1], dp[k][j]+prices[i]-prices[k])

            if dp[i][j] > dp[i-1][j]:
                k = i

        print('dp[n-1]:', dp[n-1])
        return max(dp[n-1])
```


### LeetCode 123
# 自研算法 不正确
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)

        dp = [[0 for j in range(3)] for i in range(n)]
        k = 0
        #for 循环 从第一天开始循环
        for i in range(1, n):            
            #第一次交易
            j = 1
            dp[i][j] = max(dp[i][j-1], dp[i-1][j]+prices[i]-prices[i-1])

            #第二次交易
            j = 2
            #dp[i][j] = max(dp[i-1][j-1]+prices[i]-prices[i-1], max(dp[i][j-1], dp[i-1][j]+prices[i]-prices[i-1]))
            dp[i][j] = max(dp[i][j-1], dp[k][j]+prices[i]-prices[k])

            if dp[i][j] > dp[i-1][j]:
                k = i

        print('dp[n-1]:', dp[n-1])
        return max(dp[n-1])
```

