import queue


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        n = len(image)
        m = len(image[0])
        if n == 0 or m == 0:
            return []

        # bfs
        q = queue.Queue()
        image[sr][sc] = newColor
        q.put([sr, sc])
        x_ = [0, 0, -1, 1]
        y_ = [-1, 1, 0, 0]
        while q.qsize():
            cur = q.get()
            #print("now_cur:", cur)
            for i in range(4):
                if self.is_valid(cur[1]+x_[i], cur[0]+y_[i], m, n):
                    if image[cur[0]+y_[i]][cur[1]+x_[i]] != 0 and image[cur[0]+y_[i]][cur[1]+x_[i]] != newColor:
                        image[cur[0]+y_[i]][cur[1]+x_[i]] = newColor
                        q.put([cur[0]+y_[i], cur[1]+x_[i]])

        return image

    def is_valid(self, x, y, m, n):
        return (x >= 0 and x < m) and (y >= 0 and y < n)
