class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return root

            # inorder traversal   post-order???
        stack = []
        trav = root
        head = Node(None)  # the dummy node
        prev = None

        while trav or stack:
            while trav:
                stack.append(trav)
                trav = trav.left

            trav = stack.pop()   # => get the left-end node
            # just deal with the dummy node of head
            if not head.right:
                head.right = trav

            # pred, succ links
            if prev:
                prev.right = trav
                trav.left = prev
            prev = trav
            trav = trav.right

        # make circular
        prev.right = head.right
        head.right.left = prev

        return head.right
