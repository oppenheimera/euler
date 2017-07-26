import java.util.ArrayList;
import java.util.Collections;

/*
A perfect number is a number for which the sum of its proper divisors is 
exactly equal to the number. For example, the sum of the proper divisors 
of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less 
than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. 
By mathematical analysis, it can be shown that all integers greater than 
28123 can be written as the sum of two abundant numbers. However, this upper 
limit cannot be reduced any further by analysis even though it is known that 
the greatest number that cannot be expressed as the sum of two abundant 
numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum 
of two abundant numbers.
*/
public class NonAbundantSums {
    public static boolean twoSumDecision(int target, ArrayList<Integer> L) {
        /* decision problem: do any two integers i in L sum to n?
        * depends on L being sorted */
        int lowPointer = 0;
        int highPointer = L.size() - 1;
        while (lowPointer <= highPointer) {
            int tempSum = L.get(lowPointer) + L.get(highPointer);
            if (tempSum == target) return true;
            else if (tempSum > target) highPointer -= 1;
            else lowPointer += 1;
        }
        return false;
    }

    public static ArrayList<Integer> getDivisors(int n) {
        ArrayList<Integer> divisorList = new ArrayList<>();
        divisorList.add(1);
        for (int i = 2; i < Math.sqrt(n); i++) {
            if (n % i == 0) {
                divisorList.add(i);
                if (i != n/i) {
                    divisorList.add(n/i);
                }
            } else if (Math.floor(Math.sqrt(n)) * Math.floor(Math.sqrt(n)) == n) {
                Collections.addAll(divisorList, (int) Math.sqrt(n), (int) Math.sqrt(n));
            }
        }
        return divisorList;
    }

    public static Integer sumArrayList(ArrayList<Integer> L) {
        int sum = 0;
        for (int i : L) sum += i;
        return sum;
    }

    public static boolean isAbundant(int n) {
        if (sumArrayList(getDivisors(n)) > n) return true;
        return false;
    }

    public static void main(String[] args) {
        // generate abundants
        ArrayList<Integer> L = new ArrayList<>();
        int sum = 0;

        //these fuckers are counting duplicates
        for (int i = 11; i <= 28123; i++) if (isAbundant(i)) L.add(i);

        //bound provided by http://mathworld.wolfram.com/AbundantNumber.html
        for (int j = 1; j <= 20161; j++) if (!twoSumDecision(j, L)) sum += j;
        
        System.out.print("The answer is "); System.out.println(sum);

    }
}