import queue
from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        # bfs
        q = queue.Queue()
        dq = deque()
        dq.append(root)
        q.put(root)
        direction = True
        while q.qsize():
            n = q.qsize()
            tmp_res = []
            for i in range(n):
                cur_root = q.get()
                tmp_res.append(cur_root.val)
                if cur_root.left:
                    q.put(cur_root.left)
                if cur_root.right:
                    q.put(cur_root.right)
            if direction:
                res.append(tmp_res)
                direction = False
            else:
                res.append(tmp_res[::-1])
                direction = True
        return res
