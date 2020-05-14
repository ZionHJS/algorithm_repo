 # 自己写一个dfs()吧 需要配置下 memo
  memo = defaultdict(lambda: [0, 0])

   def dfs(idx, M, switch):
        if (idx, M, switch) in memo:
            return memo[(idx, M, switch)]
        nxt = [0, 0]
        if switch:
            if idx+2*M >= len(A):
                return [sum(A[idx:]), 0]
            for i in range(1, 2*M+1):
                tmp = dfs(idx+i, max(M, i), False)
                if sum(A[idx:idx+i])+tmp[0] >= nxt[0]:
                    nxt = [sum(A[idx:idx+i])+tmp[0], tmp[1]]
        else:
            if idx+2*M >= len(A):
                return [0, sum(A[idx:])]
            for i in range(1, 2*M+1):
                tmp = dfs(idx+i, max(M, i), True)
                if sum(A[idx:idx+i])+tmp[1] >= nxt[1]:
                    nxt = [tmp[0], sum(A[idx:idx+i])+tmp[1]]
        memo[(idx, M, switch)] = nxt
        return nxt
    res = dfs(0, 1, True)
    return res[0]
