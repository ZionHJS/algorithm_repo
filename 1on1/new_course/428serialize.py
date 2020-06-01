class Codec:
    def serialize(self, root: 'Node') -> str:
        if not root:
            return []
        res = "[" + str(root.val)
        for child in root.children:
            print("child:", child)
            res += (self.serialize(child))
        return res + "]"

    def deserialize(self, data: str) -> 'Node':
        # 先处理data
        def data_list(data):
            i = 0
            stack = []
            tmp = []
            while i < len(data):
                if data[i] == "[":
                    stack.append(tmp)
                    tmp = []

        root = Node(data[0])
        root.children = set()
        if len(data) > 1:
            for i in range(1, len(data)):
                root.children.add(self.deserialize(data[i]))
