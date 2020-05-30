import heapq


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        n = len(lists)

        head = ListNode(None)
        heap = [(lists[i].val, i) for i in range(n) if lists[i]]
        for i in range(n):
            lists[i] = lists[i].next if lists[i] else None
        heapq.heapify(heap)  # O(logN)   #一定要用heapify来做 时间复杂度低

        cur = head
        while heap:
            val, i = heapq.heappop(heap)  # O(logK)
            cur.next = ListNode(val)
            cur = cur.next
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))  # O(logK)
                lists[i] = lists[i].next

        return head.next
