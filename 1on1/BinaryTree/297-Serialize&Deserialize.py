# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    def __init__(self):
        self.ser_str = ''
        self.s_idx = -1

    def serialize(self, root):
        if not root:
            self.ser_str += "null,"
            return None

        # preorder
        self.ser_str += str(root.val) + ","
        self.serialize(root.left)
        self.serialize(root.right)

        print("ser_str:", self.ser_str)
        return self.ser_str

    def deserialize(self, data):
        e_idx = self.next_idx(self.s_idx, data)
        if data[s_idx+1:e_idx].isdigit():
            root = TreeNode(int(data[s_idx+1:e_idx]))
        else:
            self.s_idx = self.next_idx(e_idx, data)
            self.deserialize(data)

        self.s_idx = e_idx

        return root

    def next_idx(self, s_idx, data):
        e_idx = s_idx

        if s_idx == len(data)-1:
            return None

        for i in range(s_idx+1, len(data)-1):
            if data[i] == ",":
                e_idx = i
                break

        return e_idx
