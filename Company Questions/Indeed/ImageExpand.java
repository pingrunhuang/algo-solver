package CodeChallenge.Indeed;

/*
* Problem Statement
A binary image is an image consisting of black and white pixels.

You are given a binary image with a height of H pixels and a width of W pixels as pi,j, a rectangular array of H×W characters. pi,j corresponds to the pixel at the i-th row from the top and j-th column from the left in the binary image. If pi,j = ., the corresponding pixel is white; if pi,j = #, the corresponding pixel is black.

Additionally, you are also given two integers A and B. Your task is to produce a new image with a height of A×H pixels and a width of B×W pixels, by arranging A×B copies of the given image in A rows and B columns. Output the obtained image in the same format as the input.

Constraints
1≤H≤10
1≤W≤10
1≤A≤10
1≤B≤10
pi,j is either . or #.
Input
Input is given from Standard Input in the following format:

H W A B
p1,1p1,2…p1,W
p2,1p2,2…p2,W
:
pH,1pH,2…pH,W
Output
Print (A×H)×(B×W) characters qi,j representing the obtained image with a height of A×H pixels and a width of B×W pixels, in the following format:

q1,1q1,2…q1,B×W
q2,1q2,2…q2,B×W
:
qA×H,1qA×H,2…qA×H,B×W
Here, qi,j corresponds to the pixel at the i-th row from the top and j-th column from the left in the obtained image. If the corresponding pixel is white, qi,j must be .; if the corresponding pixel is black, qi,j must be #.

Sample Input 1
Copy
6 7 2 3
...#...
..#.#..
.#...#.
.#####.
.#...#.
.#...#.
Sample Output 1
Copy
...#......#......#...
..#.#....#.#....#.#..
.#...#..#...#..#...#.
.#####..#####..#####.
.#...#..#...#..#...#.
.#...#..#...#..#...#.
...#......#......#...
..#.#....#.#....#.#..
.#...#..#...#..#...#.
.#####..#####..#####.
.#...#..#...#..#...#.
.#...#..#...#..#...#.
Given is an image with a height of 6 pixels and a width of 7 pixels. By arranging copies of this image in 2 rows and 3 columns, print a new image with a height of 12 pixels and a width of 21 pixels.

Sample Input 2
Copy
6 7 1 1
...#...
..#.#..
.#...#.
.#####.
.#...#.
.#...#.
Sample Output 2
Copy
...#...
..#.#..
.#...#.
.#####.
.#...#.
.#...#.
If H=W=1, the output image will be the same as the input.
* */

import java.util.Scanner;

public class ImageExpand {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int H = scanner.nextInt();
        int W = scanner.nextInt();
        int A = scanner.nextInt();
        int B = scanner.nextInt();
        String[] origin_image = new String[H];
        String[] new_image = new String[A*H];
        for (int i=0;i<H;i++){
            origin_image[i] = scanner.next();
        }

        for (int i=0;i<A*H;i++){
            int row;
            if (i < H){//on the first block
                row = i;
            }else{
                row = i % H;
            }
            StringBuilder stringBuilder = new StringBuilder();
            for (int j=0;j<B;j++){
                stringBuilder.append(origin_image[row]);
            }
            new_image[i] = stringBuilder.toString();
        }

        for (int i = 0;i<new_image.length;i++){
            System.out.println(new_image[i]);
        }

    }

}
