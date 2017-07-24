import java.util.ArrayList;

public class Triangular {
    ArrayList<Integer> generateTriangularNumbersUpTo(int n) {
        ArrayList<Integer> answer = new ArrayList<Integer>();
        return answer;
    }

    static Integer triangularNumberN(int n) {
        return (n * (n+ 1)) / 2;
    }

    static Integer numberOfDivisors(int n) {
        Integer count = 0;
        Integer sqrt = (int) Math.sqrt(n);

        for (int x = 1; x <= sqrt; x++) {
            if (n % x == 0) {
                count += 2;
            }
        }
        if (sqrt * sqrt == n) {count--;}
        return count;
    }
    
    public static void main(String[] args) {        
        int n = 1;
        while (numberOfDivisors(n) < 500) {n++;}
        System.out.println(triangularNumberN(n));
    }
}
