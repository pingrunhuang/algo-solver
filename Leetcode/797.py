'''
Example:
Input: [[1,2], [3], [3], []] 
Output: [[0,1,3],[0,2,3]] 
Explanation: The graph looks like this:
0--->1
|    |
v    v
2--->3
There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

Solution using: DFS
# TODO
'''


class Solution:
    def dfs(self, graph, start, end):
        '''
        This DFS method will output the following result
        [[0, 1, 3, 2, 3], [0, 1, 3, 2, 3]]
        which is caused by python taking path as global variable
        '''
        self.path.append(start)
        if start==end:
            self.paths.append(self.path)
            return
        for node in graph[start]:
            self.dfs(graph, node, end)

    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(graph)
        paths=[]
        path=[]
        if n==0:
            return paths
        def dfs(graph, paths, path, start, end):
            path.append(start)
            if start==end:
                paths.append(path)
                return
            for node in graph[start]:
                dfs(graph, paths, path, node, end)

        dfs(graph, paths, path, 0, n-1)
        return paths

    def allPathsSourceTarget1(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        target = len(graph)-1
        source = 0
        stack = [(source, [source])]
        results = []; path=[source]
        while stack:
            node, path = stack.pop()
            if node == target:
                results.append(path[:])
            for nbr in graph[node]:
                # using path+[] to avoid the path NoneType
                stack.append((nbr, path+[nbr]))
        return results

if __name__=='__main__':
    solution = Solution()
    t1=[[1,2,3], [2,3], [3], []]
    print(solution.allPathsSourceTarget(t1))