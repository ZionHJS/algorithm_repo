class Node:
    def __init__(self):
        self.children = {}
        self.isend = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        runner = self.root
        for c in word:
            if c not in runner.children:
                runner.children[c] = Node()
            runner = runner.children[c]
        runner.isend = True

    def search(self, word: str) -> bool:
        runner = self.root
        for c in word:
            if c not in runner.children:
                return False
            runner = runner.children[c]
        if runner.isend:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        runner = self.root
        for c in prefix:
            if c not in runner.children:
                return False
            runner = runner.children[c]
        return True
