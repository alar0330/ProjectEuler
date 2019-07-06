/**
 * Project Euler: Problem #002
 *
 * @author   Alexander Arzhanov
 * @version  07/02/18
 */
 
package problems.p002;
import problems.util.EulerSolvable;


// Fibonacci
public final class p002 implements EulerSolvable {

    /**
    * Naive solution with a function.
    *
    * @param in  Max number to sum up to (String in in[0]).
    * @return    The sum of the even Fibo-numbers (String).
    */
    @Override
    public String solve(String... in) {
        
        int lim = Integer.parseInt(in[0]);
        int sum = 0;        
        int a = 0, b = 1;
        
        while (b < lim) {  
        
            if (b % 2 == 0) sum += b;
            
            b = b + a;
            a = b - a;            
        }
        
        return Integer.toString(sum);
    }
    
    // Stand-alone test-run
    public static void main(String args[]) {
        
        System.out.println(new p002().solve("100"));
        
    }    
}