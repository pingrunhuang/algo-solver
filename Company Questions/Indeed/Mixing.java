package CodeChallenge.Indeed;

import java.util.Scanner;

/**
 * Problem Statement
 We have N ingredients, numbered 1 through N, used in making medicines. We will compound two medicines using these ingredients. Each medicine will be made by mixing K ingredients chosen from the N ingredients we have. Here, it is not possible to use an ingredient in both medicines at the same time.

 There are M rules that decide the efficacy of a medicine. The i-th rule is represented by a tuple of three integers (ai,bi,ui). Based on these rules, the efficacy of a medicine is calculated as below:

 (efficacy) = (the sum of ui over all i such that both ingredients ai and bi are used in the medicine)
 Here, if there does not exist i such that both ingredients ai and bi are used in the medicine, the efficacy of the medicine is 0.

 Find the maximum possible sum of the efficacies of the two medicines that we will compound.

 Constraints
 All input values are integers.
 4≤N≤8
 2≤K≤N⁄2
 1≤M≤N(N−1)⁄2
 1≤ai<bi≤N
 All pairs (ai,bi) are distinct.
 1≤ui≤100
 Input
 Input is given from Standard Input in the following format:

 N K M
 a1 b1 u1
 a2 b2 u2
 :
 aM bM uM
 Output
 Print the maximum possible sum of the efficacies of the two medicines that will be compounded.

 Sample Input 1
 Copy
 5 2 4
 1 2 20
 1 3 10
 2 4 10
 2 5 15
 Sample Output 1
 Copy
 25
 The efficacy of the medicine compounded from ingredients 1 and 3 is 10, and the efficacy of the medicine compounded from ingredients 2 and 5 is 15. These two medicine can be compounded at the same time for a total efficacy of 25, which is the maximum possible sum.

 Sample Input 2
 Copy
 7 3 3
 1 2 10
 1 3 10
 2 3 10
 Sample Output 2
 Copy
 30
 The efficacy of the medicine compounded from ingredients 1, 2 and 3 is 10+10+10=30. If this medicine is compounded, no matter what ingredients is used to compound the other medicine, the efficacy of that other medicine will be 0. The total efficacy will be 30 in this case, which is the maximum possible sum.

 Sample Input 3
 Copy
 8 4 8
 1 2 10
 2 3 20
 3 4 30
 4 5 40
 5 6 50
 6 7 60
 7 8 70
 1 8 80
 Sample Output 3
 Copy
 300

 *
 */
// TODO
public class Mixing {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

    }

}
