package CodeChallenge.Indeed;

/**
 * Problem Statement
 There is a rectangular board divided into a grid with H rows and W columns. Each square of the grid is painted in either black or white. Below, we will denote the square at the i-th row from the top and j-th column from the left as (i,j). You are given the color of (i,j) as a character ci,j. If ci,j = ., (i,j) is white; if ci,j = #, (i,j) is black. Here, (1,1) and (H,W) are always white.

 There is a piece placed at (1,1). Your objective is to transfer the piece to (H,W). The following two kinds of operations can be used to move the piece:

 Normal move: Let the square currently occupied by the piece be (y,x). Move the piece to one of the following: (y,x+1), (y+1,x), (y,x−1) and (y−1,x). Here, the destination may not be a black square or a non-existent square. This operation may be executed any number of times.

 Warp: Let the square currently occupied by the piece be (y,x). Move the piece to (y+D,x+R). Here, the values of R and D are predetermined. This operation cannot be executed if (y+D,x+R) is black or the square does not exist. This operation may be executed at most once (you may choose not to execute this).

 Determine whether it is possible to transfer the piece to (H,W). If the transfer is possible, find the minimum necessary number of operations (both kinds of operations count).

 Constraints
 2≤H≤10
 2≤W≤10
 −(H−1)≤D≤H−1
 −(W−1)≤R≤W−1
 The pair (D,R) is different from all of the following: (0,0),(0,1),(1,0),(0,−1) and (−1,0).
 ci,j is either . or #.
 c1,1 and cH,W are both ..
 Input
 Input is given from Standard Input in the following format:

 H W D R
 c1,1c1,2…c1,W
 c2,1c2,2…c2,W
 :
 cH,1cH,2…cH,W
 Output
 If it is possible to transfer the piece to (H,W), print the minimum necessary number of operations.

 If it is possible to transfer the piece to (H,W), print -1.

 Sample Input 1
 Copy
 3 6 2 1
 ...#..
 ..##..
 ..#...
 Sample Output 1
 Copy
 5
 It is possible to transfer the piece from (1,1) to (3,6) in five operations, as follows:

 Normal move: (1,1)→(1,2)
 Normal move: (1,2)→(1,3)
 Warp: (1,3)→(3,4)
 Normal move: (3,4)→(3,5)
 Normal move: (3,5)→(3,6)
 It is not possible to transfer the piece in fewer operations.

 Sample Input 2
 Copy
 3 7 2 1
 ..#..#.
 .##.##.
 .#..#..
 Sample Output 2
 Copy
 -1
 Since Warp can only be used once, the transfer is not possible.

 Sample Input 3
 Copy
 6 6 -2 0
 .#....
 .#.#..
 .####.
 .#..#.
 .##.#.
 ....#.
 Sample Output 3
 Copy
 21
 The values of D and R may be zero or negative.

 Sample Input 4
 Copy
 3 4 -1 -2
 ....
 ....
 ....
 Sample Output 4
 Copy
 5
 You may choose not to use Warp.


 */
// TODO
public class Warping {
}
