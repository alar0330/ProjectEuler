/**
 * Project Euler: Problem #005
 *
 * @author   Alexander Arzhanov
 * @version  10/02/18
 */
 
package problems.p005;
import problems.util.EulerSolvable;


// Largest evenly-divisible
public final class eu005 implements EulerSolvable {

    /**
    * Naive implementation with dumb mod-divisions (with some speed enhancements).
    *
    * @param in  Max divisor (String in in[0]).
    * @return    The smaller numbers that is evenly divisible by all numbers up to `max` (String).
    */
    @Override
    public String solve(String... in) {
        
        // Convert input
        int max = Integer.parseInt(in[0]);
      
        long n = 0;
        boolean loop = true;
        
        while (loop) {

            loop = false;
            n += max;
            
            for (int d = max; d > 2; d--)
                if (n % d != 0) {
                    loop = true;
                    break;
                }
        }
        
        return Long.toString(n);
    }
    
    // Stand-alone test-run
    public static void main(String args[]) {
        
        System.out.println("\n ANS: " + new eu005().solve("20"));
        
    }    
}