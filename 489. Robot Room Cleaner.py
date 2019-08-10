# https://leetcode.com/problems/robot-room-cleaner/discuss/151942/Java-DFS-Solution-with-Detailed-Explanation-and-6ms-(99)-Solution
# https://leetcode.com/problems/robot-room-cleaner/discuss/153530/DFS-Logical-Thinking
# https://leetcode.com/problems/robot-room-cleaner/discuss/150132/Very-clear-Python-DFS-code-beat-99-%2B
# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
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

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        def rollback():
            robot.turnLeft()
            robot.turnLeft()
            robot.move()
            robot.turnLeft()
            robot.turnLeft()
            
        def dfs(x, y, xdire, ydire, cleaned):
            robot.clean()
            cleaned.add((x, y))
            for i in range(4):
                nbx, nby = x + xdire, y + ydire
                if ((nbx, nby) not in cleaned and robot.move()):
                    dfs(nbx, nby, xdire, ydire, cleaned)
                    rollback()
                robot.turnLeft() # <<<
                xdire, ydire = -ydire, xdire
            # rollback() # rollback here is also correct other than at <<<, which I need to figure out why
            
        cleaned = set()
        dfs(0, 0, 0, 1, cleaned) # it works no matter the robot initially facing which direction
