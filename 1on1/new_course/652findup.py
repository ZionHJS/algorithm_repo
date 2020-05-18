class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        dup = defaultdict(lambda: [])
        ans = []

        def preorder(root):
            if not root:
                return
            dup[root.val].append(root)
            preorder(root.left)
            preorder(root.right)
        preorder(root)

        print("dup:", dup)

        def is_same(root1, root2):
            if not root1 and not root2:
                return True
            elif root1 and not root2:
                return False
            elif root2 and not root1:
                return False
            elif root1.val != root2.val:
                return False

            left = is_same(root1.left, root2.left)
            right = is_same(root2.right, root2.right)

            return left and right

        for key in dup:
            print("key:", key, "len:", len(dup[key]))
            added = set()
            for i in range(len(dup[key])-1):
                if i not in added:
                    for j in range(i+1, len(dup[key])):
                        if i not in added and j not in added:
                            if is_same(dup[key][i], dup[key][j]):
                                print("add-i:", i, "add-j:", j)
                                added.add(i)
                                added.add(j)
                                ans.append(dup[key][i])
        return ans
