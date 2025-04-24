"""
N cars are going to the same destination along a one lane road.  The destination is target miles away.

Each car i has a constant speed speed[i] (in miles per hour), and initial position position[i] miles towards the target along the road.

A car can never pass another car ahead of it, but it can catch up to it, and drive bumper to bumper at the same speed.

The distance between these two cars is ignored - they are assumed to have the same position.

A car fleet is some non-empty set of cars driving at the same position and same speed.  Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.


How many car fleets will arrive at the destination?
"""
class Solution:
    def carFleet(self, target: int, position: list, speed: list):
        result = 0
        previous_arrial_time = -1
        # sort by position from far -> close
        cars = sorted(zip(position, speed), key=lambda x:x[0])
        # should traverse from close -> far
        for p, s in cars[::-1]:
            # if a car started at the further position can arrive earlier, it should 
            estimated_arrial = (target - p) / s
            # suppose I have car A and car B where B is ahead of A and A is just behind B
            # when it takes more time for A to arrive at destination then B, means A B will meet before destination
            # when A(previous) takes shorter time to arrive then B(current), then A is a fleet itself
            if previous_arrial_time < estimated_arrial:
                result+=1
                previous_arrial_time = estimated_arrial

        return result

def test1():
    s = Solution()
    target = 12
    position = [10,8,0,5,3]
    speed = [2,4,1,1,3]
    result = s.carFleet(target, position, speed)
    print(result)

if __name__ == '__main__':
    test1()