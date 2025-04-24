package CodeChallenge.Indeed;


/**
 * 最优解问题
 * Problem Statement
 There is a road with a length of L meters that runs east-west, and there are N houses built along this road. The i-th house from the west is located xi meters east of the west end of the road, and there are ri people who live in the house.

 A station is going to be built on this road, and there was a discussion on the location of the station. Let the location of the station be P meters east of the west end of the road. According to the law, P must be a integer satisfying 0≤P≤L. After the discussion, it was decided that the location of the station will be chosen so that it minimizes the disutility calculated as follows:

 (disutility) = (the sum of (|xi−P|×ri) over all i (1≤i≤N))
 Here, |a| denotes the absolute value of a.

 Find the disutility when the location of the station is chosen to minimize it.

 Constraints
 All input values are integers.
 1≤L≤1010
 1≤N≤105
 0≤x1<x2<…<xN≤L
 1≤ri≤103
 Input
 The input is given from Standard Input in the following format:

 L N
 x1 r1
 x2 r2
 :
 xN rN
 Output
 Print the disutility when the location of the station is chosen to minimize it.

 Sample Input 1
 Copy
 100 3
 20 3
 50 2
 70 1
 Sample Output 1
 Copy
 110
 When P=40, the disutility is |20−40|×3+|50−40|×2+|70−40|×1=110. There is no location with a lower disutility.

 Sample Input 2
 Copy
 100 2
 0 1
 100 10
 Sample Output 2
 Copy
 100
 There may be houses at both ends of the road, and the station may also be built at these locations.

 Sample Input 3
 Copy
 10000000000 5
 3282894320 391
 4394338332 929
 6932893249 181
 7823822843 440
 9322388365 623
 Sample Output 3
 Copy
 5473201404068
 The input values or the expected output may not fit into 32-bit integers.
 */

import java.util.Scanner;
public class Location {

    static class House{
        long distance;
        int popularity;
        House(long d, int p){
            distance = d;
            popularity = p;
        }
    }

    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        long L = scanner.nextLong();
        int N = scanner.nextInt();
        House[] houses = new House[N];
        for (int i=0;i<N;i++){
            long x = scanner.nextLong();
            int r = scanner.nextInt();
            houses[i] = new House(x,r);
        }

        long min_efficiency = Long.MAX_VALUE;

        for (long P=0;P<=L;P++){
            long efficiency = 0;
            for (int i=0;i<N;i++){
                efficiency = efficiency + Math.abs(houses[i].distance - P) * houses[i].popularity;
            }
            if (min_efficiency > efficiency){
                min_efficiency = efficiency;
            }
        }
        System.out.println(min_efficiency);
    }

}
