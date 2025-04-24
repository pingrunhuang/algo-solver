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



def solution(buildings):
    prev_x1, prev_x2, prev_y = 0, buildings[0][0], 0
    result = []
    for skyline in sorted(buildings, key=lambda x: x[0]):
        x1, x2, y = skyline
        # case 2
        if x1 <= prev_x2:
            # case d
            if y < prev_y:
                result.append((prev_x2, y))
            elif y > prev_y:
                # case a, b 
                result.append((x1, y))
                # special case for b to add the skyline at tail
                if x2 < prev_x2:
                    result.append((prev_x2, 0))
                    result.append((x2, prev_y))
        # case 1
        else:
            result.append((x1, y))
        prev_x1, prev_x2, prev_y = x1, x2, y
    result.append((prev_x2, 0))
    return result


class Corner:
    def __init__(self, x, y, t):
        self.x = x
        self.y = y
        self.t = t # s means start, e means end
    def __repr__(self):
        return f"[{self.x}, {self.y}, start]" if self.t==1 else f"[{self.x}, {self.y}, end]" 


class Solution(object):

    def remove(self, value, heap):
        idx = heap.index(value)
        heap[idx] = heap[-1]
        heap.pop()
        heapq.heapify(heap)

    def getSkyline(self, buildings):
        skyline = []
        for building in buildings:
            skyline.append(Corner(building[0], building[2], 1))
            skyline.append(Corner(building[1], building[2], 2))
        sorted_skyline = sorted(skyline, key=lambda x:(x.x, x.t, -x.y))
        height_heap = [0]
        result = []
        # heapq only pop the smallest, so need to transform the largest y into negative
        for corner in sorted_skyline:
            if corner.t == 1:
                heap_highest = -heapq.nsmallest(1, height_heap)[0]
                if heap_highest < corner.y:
                    print(corner)
                    result.append((corner.x, corner.y))
                heapq.heappush(height_heap, -corner.y)
            else:
                heap_highest = -heapq.nsmallest(1, height_heap)[0]
                if heap_highest == corner.y:
                    heapq.heappop(height_heap)
                    second = -heapq.nsmallest(1, height_heap)[0]
                    # corner case: end overlap start
                    if second != corner.y:
                        result.append((corner.x, second))
                elif corner.y < heap_highest:
                    self.remove(-corner.y, height_heap)
        return result


if __name__ == "__main__":
    buildings = [[2,4,3], [3,5,6], [6,9,2], [7,8,5]]
    s = Solution()
    print(s.getSkyline(buildings))
    buildings = [[0,2,3],[2,5,3]]
    print(s.getSkyline(buildings))
    buildings = generate_random_buildings(4)
    print(buildings)