'''
You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, 
then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree. 


Input: 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
Output: 
Merged tree:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


Summary:
Dealing with binary tree could be achieved by recursion or stack method
'''
# TODO: review later
from collections import deque
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.right = None
        self.left = None

class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1==None:
            return t2
        if t2==None:
            return t1
        t1.val=t1.val+t2.val

        t1.left=self.mergeTrees(t1.left,t2.left)
        t1.right=self.mergeTrees(t1.right,t2.right)
        return t1

    def mergeTreesWithQueue(self, t1, t2):
        # don't try to introduce a third tree
        queue=deque()
        if t1 == None:
            return t2
        if t2 == None:
            return t1
        queue.append((t1, t2))
        result_tree = TreeNode(0)
        while len(queue)!=0:
            cur_pair = queue.popleft()
            cur_tree1 = cur_pair[0]
            cur_tree2 = cur_pair[1]

            if cur_tree1 and cur_tree2:
                cur_tree1.val += cur_tree2.val

                if not cur_tree1.left and cur_tree2.left:
                    # only in this situation can I just asign the tree2's left node without appending it since there are no nodes left after this node in tree1
                    cur_tree1.left = cur_tree2.left
                else:
                    queue.append((cur_tree1.left, cur_tree2.left))
                if not cur_tree1.right and cur_tree2.right:
                    cur_tree1.right = cur_tree2.right
                else:
                    queue.append((cur_tree1.right, cur_tree2.right))
        return t1
            # if tree1 and tree2:
            #     cur_node = TreeNode(tree1.val + tree2.val)
            #     if tree1.left and tree2.left:
            #         cur_node.left = TreeNode(tree1.left.val + tree2.left.val)
            #         queue.append((tree1.left, tree2.left))
            #     if not tree1.left and tree2.left:
            #         cur_node.left = TreeNode(tree2.left.val)
            #         queue.append((None, tree2.left))
            #     if tree1.left and not tree2.left:
            #         cur_node.left = TreeNode(tree1.left.val)
            #         queue.append((tree1.left, None))
            # elif tree1 and not tree2:
            #     cur_node = tree1
            #     if tree1.left:
            #         queue.append((tree1.left, None))
            # elif not tree1 and tree2:
            #     cur_node = tree2
            #     if tree2.left:
            #         queue.append((None, tree2.left))
            
        return result_tree


        

    def bfs(self, root):
        queue = deque()
        if root==None:
            return
        queue.append(root)
        while len(queue)!=0:
            current_node = queue.popleft()
            if current_node.left!=None:
                queue.append(current_node.left)
            if current_node.right!=None:
                queue.append(current_node.right)
            print(str(current_node.val)+ '->', end=' ')


if __name__=='__main__':
    solution = Solution()
    tree1 = TreeNode(1)
    tree1.right=TreeNode(2)
    tree1.left=TreeNode(3)
    tree1.left.left=TreeNode(5)

    tree2=TreeNode(2)
    tree2.right=TreeNode(3)
    tree2.right.right=TreeNode(7)
    tree2.left=TreeNode(1)
    tree2.left.right=TreeNode(4)

    m=solution.mergeTreesWithQueue(tree1,tree2)
    solution.bfs(m)