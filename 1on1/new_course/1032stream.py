class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.isend = False


class StreamChecker:
    def __init__(self, words: List[str]):
        self.words = set()
        for word in words:
            self.words.add(word[::-1])
        self.root = TrieNode(None)
        self.root.isend = True

    def query(self, letter: str) -> bool:
        head = TrieNode(letter)
        head.children[self.root.val] = self.root
        self.root = head
        return self.dfs(self.root, "", 0)

    def dfs(self, root, tmp, cnt):
        if not root.val or root.isend or cnt > 2000:
            return tmp in self.words
        tmp += root.val
        if tmp in self.words:
            return True
        cnt += 1
        if root.children:
            for child in root.children:
                if self.dfs(root.children[child], tmp, cnt):
                    return True
        return False
