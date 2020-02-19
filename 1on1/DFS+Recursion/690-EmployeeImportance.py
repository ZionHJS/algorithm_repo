class Solution:
    def __init__(self):
        self.total_value = 0

    def getImportance(self, employees: List['Employee'], id: int) -> int:

    def dfs(self, employees, id):
        for employee in employees:
            if employee[0] == id:
                self.total_value += employee[1]
                if employee[2]:
                    for subordinate in employee[2]:
                        self.v(employees, subordinate)
                else:
                    return
