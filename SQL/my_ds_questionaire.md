1. 给定一组数据如下：  
```
----------------------------------
id              | course
----------------------------------
20011111        | 数学
20011112        | 物理
20011113        | 化学
20011114        | 地理
20011111        | 历史
20011112        | 语文
20011113        | 物理
20011113        | 英语
20011114        | 化学
20011112        | 数学
20011111        | 数学
...             | ...
...             | ...
```
key是学生的学号，value是对应的学生选的课程，（注意，因为不同学期是允许选同一门课程的，所以同一个学生选的课程名称可能会重复），要求统计出每个同学选择课程数。如果给定的数据是以RDD的形式呢？

### 答案
- sql做法：
    如果数据是存储在关系型数据库中，可以考虑使用`select key, count(distinct value) from tablename group by key;`
- 传统内存编程式的做法：
    如果传入的数据是文件的形式，可以考虑把整个数据集读入内存中，做成一个dictionary，key值是每个学生的学号，value值是一个course组成的`set`。然后求出每个`set`对应的长度即可。
- rdd的方式：
    1. groupByKey的做法
    ```scala
    rdd.groupByKey(record=>(record._t, record._2.sum))
    ```
    2. 避免使用groupByKey带来的不同partition之间直接做shuffle的问题
    ```scala
    val zero = new collection.mutable.Set[String]()
    val result = rdd.aggregateByKey(
        zero
    )(
        (set, v) => set+=v,
        (set1, set2) => set1 ++= set2
    )
    ```

2. 算法题：给定一个二维数组，代表一张图，图中每个点的值要么是1，要么是0。1代表该点是陆地，0代表该点是大海，对于某一个点，如果这个点的上或下或左或右都是1，则几个点可以组成一个岛。给定一张图，输出这张图中包含最大岛的面积（包含多少个点）。算法复杂度是多少呢？
```
// 输入
[[1,0,1,0,0],
[1,1,1,0,1],
[1,1,1,0,1],
[0,1,1,0,1]]

// 输出：10

// 输入：
[[1,0,1,0,0],
[1,1,1,0,1],
[1,1,1,0,1],
[0,1,1,1,1]]
// 输出：14
```

### 答案
```python
def matrix2Grid(matrix):
    '''
    Transform the matrix element into the form of tuple (x,y)
    x: color
    y: hasTraverse
    '''
    return [[[col, 0] for col in row] for row in matrix]

class Solution:
    def dfs(self, i, j, matrix):
        result = 0
        # margin situation
        if 0<=i<len(matrix) and 0<=j<len(matrix[i]) and matrix[i][j][1]!=1:
            result+=1
            matrix[i][j][1] = 1
            # left
            if j-1>=0 and matrix[i][j][0]==matrix[i][j-1][0]:
                result += self.dfs1(i, j-1, matrix)
            # right
            if j+1<len(matrix[i]) and matrix[i][j][0]==matrix[i][j+1][0]:
                result += self.dfs1(i, j+1, matrix)
            # up
            if i-1>=0 and matrix[i][j][0]==matrix[i-1][j][0]:
                result += self.dfs1(i-1, j, matrix)
            # down
            if i+1<len(matrix) and matrix[i][j][0]==matrix[i+1][j][0]:
                result += self.dfs1(i+1, j, matrix)
        return result

    def solve(self, matrix):
        maximumBlocks = 0
        for i,_ in enumerate(matrix):
            for j,_ in enumerate(matrix[i]):
                result = self.dfs1(i, j, matrix)
                # update the maximum number of linked blocks
                if maximumBlocks < result:
                    maximumBlocks = result
        return maximumBlocks
```
3. 阐述你对于闭包(closure)的理解，并且举一个你在实际工作中或者个人学习的时候使用闭包抽象出共性代码的例子。