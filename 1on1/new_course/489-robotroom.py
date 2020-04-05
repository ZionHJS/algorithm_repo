# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """
import random


class Solution:
    def __init__(self):
        self.turn_cnt = 0
        self.cur_x, self.cur_y = 0, 0
        self.map = {}
        self.x_, self.y_ = [-1, 0, 1, 0], [0, 1, 0, -1]

    def cleanRoom(self, robot):
        self.map[(self.cur_x, self.cur_y)] = 1
        robot.clean()
        while robot.move():
            self.cur_x = self.cur_x + self.x_[self.turn_cnt]
            self.cur_y = self.cur_y + self.y_[self.turn_cnt]
            self.map[(self.cur_x, self.cur_y)] = 1
            robot.clean()
        self.nxt_x = self.cur_x + self.x_[self.turn_cnt]
        self.nxt_y = self.cur_y + self.y_[self.turn_cnt]
        self.map[(self.nxt_x, self.nxt_y)] = 0

        # try turn left or right

        rnd = random.randint(0, 1)
        if rnd:
            robot.turnLeft()
            self.turn_cnt -= 1
            if self.turn_cnt < 0:
                self.turn_cnt = 3
            self.cleanRoom(robot)
        else:
            robot.turnRight()
            self.turn_cnt += 1
            if self.turn_cnt > 3:
                self.turn_cnt = 0
            self.cleanRoom(robot)

    def nxt_turn(self):
        rnd = random.randint(0, 1)
