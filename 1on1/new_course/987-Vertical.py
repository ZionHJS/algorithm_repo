class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        def dfs(idx, cur_res, root):
            if not root:
                return cur_res
            res[idx].append(root.val)
            if root.left:
                if idx-1 <= 0:
                    cur_res = [[]] + cur_res
                    idx += 1
                cur_res = dfs(idx-1, cur_res, root.left)
            if root.right:
                if idx+1 >= len(cur_res):
                    cur_res = cur_res + [[]]
                cur_res = dfs(idx+1, cur_res, root.right)
            return cur_res

        res = dfs(0, [[]], root)

        return res
