'''
Given an absolute path for a file (Unix-style), simplify it. 

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
path = "/a/../../b/../c//.//", => "/c"
path = "/a//b////c/d//././/..", => "/a/b/c"

In a UNIX-style file system, a period ('.') refers to the current directory, so it can be ignored in a simplified path. Additionally, a double period ("..") moves up a directory, so it cancels out whatever the last directory was.

Corner Cases:

1. Did you consider the case where path = "/../"?
    In this case, you should return "/".
2. Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
    In this case, you should ignore redundant slashes and return "/home/foo".
'''

class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path_set = path.split("/")
        node_list = []
        for node in path_set:
            if node == '' or node=='.':
                continue
            if node == '..':
                if len(node_list)!=0:
                    node_list.pop()
            else:
                node_list.append(node)
        return '/'+'/'.join(node_list)


if __name__ == "__main__":
    s = Solution()
    assert s.simplifyPath("/home/") == "/home"
    assert s.simplifyPath("/a/./b/../../c/") == "/c"
    assert s.simplifyPath("/a/../../b/../c//.//") == "/c"
    assert s.simplifyPath("/a//b////c/d//././/..") == "/a/b/c"
        