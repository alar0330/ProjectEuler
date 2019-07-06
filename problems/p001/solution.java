/**
 * Project Euler: Problem #001
 *
 * @author   Alexander Arzhanov
 * @version  03/02/18
 */

package problems.p001; 
import problems.util.EulerSolvable;


public final class p001 implements EulerSolvable {
    
    /**
    * Naive implementation.
    *
    * @param in  Max number to sum up to (String in in[0]).
    * @return    The sum of the filtered components (String).
    */
    @Override
    public String solve(String... in) {
        
        int lim = Integer.parseInt(in[0]);
        int sum = 0;
                
        for (int x = 0; x < lim; x++) {
            
            if ( (x % 3) == 0 || (x % 5) == 0 ) {
                sum += x;
            }
        }
        
        return Integer.toString(sum);
    }
    
    // Stand-alone test-run
    public static void main(String args[]) {
        
        System.out.println(new p001().solve("10"));
        
    }    
}
