# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        list = []
        sorted_ = self.LinkedListToList(head, list)

        if not sorted_:
            return None

        mid = len(sorted_)//2
        root = TreeNode(sorted_[mid])
        root.left = self.genTree(root, sorted_[:mid])
        root.right = self.genTree(root, sorted_[mid+1:])

        return root

    def genTree(self, node, list):
        if not list:
            return None

        mid = len(list)//2
        root = TreeNode(list[mid])
        root.left = self.genTree(root, list[:mid])
        root.right = self.genTree(root, list[mid+1:])

        return root

    def LinkedListToList(self, node, list):
        if node == None:
            return list

        list.append(node.val)
        self.LinkedListToList(node.next, list)
        return list
