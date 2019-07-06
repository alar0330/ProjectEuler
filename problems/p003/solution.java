/**
 * Project Euler: Problem #003
 *
 * @author   Alexander Arzhanov
 * @version  07/02/18
 */
 
package problems.p003;
import problems.util.EulerSolvable;


// Largest prime factor
public final class p003 implements EulerSolvable {

    /**
    * Solve by factorizing the input parameter.
    *
    * @param in  Number to factorize (String in in[0]).
    * @return    The largest prime factor (String).
    */
    @Override
    public String solve(String... in) {
        
        long num = Long.parseLong(in[0]);
        long ans = 0;
        
        // case: 0 or 1
        if (num < 2) return Long.toString(num);
        
        // reduce even
        while (num % 2 == 0) {
            num /= 2;
            ans = 2;
        }
        
        // reduce odd
        long lim = (long) Math.sqrt(num) + 1;
        long i = 3;
        
        while (i <= lim) {
            
            if (num % i == 0) {
                num /= i;
                lim = (long) Math.sqrt(num) + 1;
                ans = i;
                System.out.println(ans);
                continue;
            }
            
            i += 2;
        }
        
        // add the remainder factor (also self-prime case)
        if (num != 1) ans = num;
        
        return Long.toString(ans);
    }
    
    // Stand-alone test-run
    public static void main(String args[]) {
        
        System.out.println("\n ANS: " + new p003().solve("13195"));
        
    }    
}