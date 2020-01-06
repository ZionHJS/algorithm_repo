"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
import queue


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        # user bfs get all node
        nodes_list = self.get_nodes_list(node)

        # copy node old=>new
        old_to_new = {}
        for n in nodes_list:
            old_to_new[n] = Node(n.val, [])

        # copy neighbors
        for n in nodes_list:
            new_node = old_to_new[n]
            for neighbor in n.neighbors:
                new_neighbor = old_to_new[neighbor]
                new_node.neighbors.append(new_neighbor)
        return old_to_new[node]

    def get_nodes_list(self, node):
        q = queue.Queue()
        s = set()
        q.put(node)
        s.add(node)
        while q.qsize():
            head = q.get()
            for neighbor in head.neighbors:
                if neighbor not in s:
                    s.add(neighbor)
                    q.put(neighbor)
        return list(s)
