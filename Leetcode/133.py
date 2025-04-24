"""
# Definition for a Node.
"""
graph = {  
    "$id":"1",
    "neighbors":[  
        {  
            "$id":"2",
            "neighbors":[  
                {  
                "$ref":"1"
                },
                {  
                "$id":"3",
                "neighbors":[  
                    {  
                        "$ref":"2"
                    },
                    {  
                        "$id":"4",
                        "neighbors":[  
                            {  
                            "$ref":"3"
                            },
                            {  
                            "$ref":"1"
                            }
                        ],
                        "val":4
                    }
                ],
                "val":3
                }
            ],
            "val":2
        },
        {  
            "$ref":"4"
        }
    ],
    "val":1
    }

def generate_graph(graph):
    pass


class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
    def __repr__(self):
        return "{}:{}".format(self.val, self.neighbors)

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        cloned_node = Node(node.val, [])
        visited_node = {}
        self.dfs(visited_node, node)

        return visited_node[node.val]
    
    def dfs(self, visited_dict, cur_node):
        if visited_dict.get(cur_node.val):
            return visited_dict[cur_node.val]
        else:
            visited_dict[cur_node.val] = Node(cur_node.val, [])
            for node in cur_node.neighbors:
                visited_dict[cur_node.val].neighbors.append(self.dfs(visited_dict, node))
            return visited_dict[cur_node.val]
    

if __name__ == "__main__":



    root = Node(1, [Node(2, [Node(4, [Node])]),3])




        


        