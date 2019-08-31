# https://leetcode.com/problems/car-fleet/discuss/139850/C%2B%2BJavaPython-Straight-Forward
# Time: O(nlogn), space: O(n)
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        runtime = [(target - pos) / spd for pos, spd in sorted(zip(position, speed), reverse = True)]
        fleet = 0
        prevTime = 0
        for curtime in runtime:
            if (curtime > prevTime): # the later car cannot catch the car in front of it
                # forms a new fleet, and the current fleet's time to arrive at the target
                # is bound by this car's runtime
                fleet += 1
                prevTime = curtime
        return fleet
