"""
In order to curb the spread of the novel covid-19 virus, the citizens of Hackerland need to be vaccinated on priority
There are center_nodes vaccination centers in hackerland where each center has a status denoted by status[i]:
- status 1: shortage of vaccines
- status 2: sufficient vaccines
- status 3: surplus vaccines

vaccines can be transferred from centers with a surplus to certeers with a deficit. 
There is a network of bidirectional roads betwen centers where the ith road is between cities center_from[i] and center_to[i].
Each road takes 1 unit of time to traverse.
Find the minimum time in where all deficient centers can receive a supply of vaccines from some surplus center.

Note:
idea here is how to verify bidirectional path by using BFS algorithms
"""


def findPath(node:int, center_from:list, center_to:list, status:list)->int:
    result = 0
    q = [(node, 0)]
    visited = [False for _ in range(len(status))]
    while q:
        cur_node, cur_dist = q.pop(0)
        visited[cur_node-1] = True
        if status[cur_node-1]==3:
            result = cur_dist
            break
        else:
            for i in range(len(center_from)):
                if center_from[i]==cur_node and not visited[center_to[i]-1]:
                    q.append((center_to[i], cur_dist+1))
                elif center_to[i]==cur_node and not visited[center_from[i]-1]:
                    q.append((center_from[i], cur_dist+1))
    return result


def findMinimumTime(center_from:list, center_to:list, status:list)->int:
    result = -1
    for i, s in enumerate(status):
        if s == 1:
            result = max(result, findPath(i+1, center_from, center_to, status))
    return result


if __name__=="__main__":
    center_from = [1,2,3,4,5,6]
    center_to = [2,3,4,5,6,1]
    status = [3,2,1,2,1,2]
    assert 2==findMinimumTime(center_from, center_to, status)
    center_from = [1,1,1,2,3,3,5,4]
    center_to = [2,4,3,4,4,5,6,6]
    status = [3,2,3,1,2,1]
    assert 2==findMinimumTime(center_from, center_to, status)
    center_from = [1,1,2,2,3,3]
    center_to = [2,3,4,5,6,7] 
    status = [2,2,2,3,2,2,1]
    assert 4==findMinimumTime(center_from, center_to, status)