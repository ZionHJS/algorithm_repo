class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        visited = set()
        visited.add((p1[0], p1[1])), visited.add(
            (p2[0], p2[1])), visited.add((p3[0], p3[1]))

        # find the diagonal point
        dis_points = []
        for p in visited:
            dis_points.append((self.get_dis(p4, p), p))

        if len(dis_points) == 3:
            dis_points.sort(key=lambda x: x[0])
            dia_dis1, dia_point = dis_points.pop()
            edge1, n1_point = dis_points.pop()
            edge2, n2_point = dis_points.pop()
            if (edge1 == edge2) and dia_dis1 == edge1+edge2:
                edge3 = self.get_dis(dia_point, n1_point)
                edge4 = self.get_dis(dia_point, n2_point)
                dia_dis2 = self.get_dis(n1_point, n2_point)
                return dia_dis1 == dia_dis2 and edge1 == edge2 == edge3 == edge4

        return False

    def get_dis(self, p1, p2):
        return abs(p1[0]-p2[0])**2 + abs(p1[1]-p2[1])**2
