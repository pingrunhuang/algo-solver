class Solution:
    def print_dag(self, adj):
        assert len(adj) == len(adj[0])
        num_nodes = len(adj)
        # init a list of number of nodes that connect to the target node
        inbounds = [0 for _ in range(num_nodes)]
        for i in range(num_nodes):
            for j in range(num_nodes):
                if adj[i][j]:
                    inbounds[j] += 1
        
        for _ in range(num_nodes):
            # find the start node
            start_node = 0
            while start_node<num_nodes and inbounds[start_node]!=0: 
                start_node+=1
            # the graph has cycles
            if start_node==num_nodes-1:
                break
            print(start_node)
            # update the reference list
            inbounds[start_node] = -1 # delete the node

            for j in range(num_nodes):
                if adj[start_node][j]:
                    inbounds[j]-=1

if __name__ == "__main__":
    adjacency_matrx = [
        [False, False, False, False, False, False, False, False, False],
        [True,  False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False],
        [True,  False, False, False, False, True , False, False, False],
        [False, True,  False, False, False, False, False, False, False],
        [False, False, False, True,  False, False, False, False, False],
        [False, False, False, False, True , False, True,  False, True ],
        [False, False, False, False, True , True , False, False, False]
    ]
    s = Solution()
    s.print_dag(adjacency_matrx)