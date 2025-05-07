"""
given a list of building with following format:
(left_coordinate, right_coordinate, height)
generate a list of skyline (a tuple with first element as the left coordinate, second element as the height) that contain all the buildings

example:
[[1,4,5], [3,6,7], [5,9,5]]
generate
[(1,5), (3,7), (5,9)]
"""
import random
import heapq


def generate_random_buildings(num_buildings):
    upper_bound = 10
    lower_bound = 1
    result = []
    for _ in range(num_buildings):
        left = random.randint(lower_bound, upper_bound)
        right = random.randint(left+1, upper_bound+1)
        result.append([
            left,
            right, 
            random.randint(lower_bound, upper_bound)
        ])
        lower_bound = left+1
        upper_bound += 1
    return result

from collections import defaultdict

class Solution(object):
    
    def getSkyline(self, buildings):
        START = -1
        END = 1
        events = [] # 事件
        for building in buildings:
            left, right, h = building
            events.append([left, -h, START])
            events.append([right, h, END])
        events.sort(key=lambda x:(x[0],x[1]))
        result, hight_heap, hight_count = [], [0], defaultdict(int)
        hight_count[0] = 1
        for event in events:
            position, hight, t = event
            prev_max = -hight_heap[0]
            if t==START:
                hight_count[-hight]+=1
                heapq.heappush(hight_heap, hight)
            else:
                hight_count[hight]-=1
                while hight_heap and hight_count[-hight_heap[0]]==0:
                    heapq.heappop(hight_heap)

            if prev_max != -hight_heap[0]:
                result.append([position, -hight_heap[0]])

        return result

if __name__ == "__main__":
    buildings = [[2,4,3], [3,5,6], [6,9,2], [7,8,5]]
    s = Solution()
    print(s.getSkyline(buildings))
    buildings = [[0,2,3],[2,5,3]]
    print(s.getSkyline(buildings))
    buildings = generate_random_buildings(4)
    print(buildings)
    print(s.getSkyline(buildings))
    buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
    print(buildings)
    print(s.getSkyline(buildings)) # [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
