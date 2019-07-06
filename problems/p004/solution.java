/**
 * Project Euler: Problem #004
 *
 * @author   Alexander Arzhanov
 * @version  07/02/18
 */
 
package problems.p004;
import problems.util.EulerSolvable;


// Palindrome
public final class eu004 implements EulerSolvable {

    /**
    * Solve by factorizing the input parameter.
    *
    * @param in  Number of digits that product numbers made of (String in in[0]).
    * @return    The largest palindrome (String).
    */
    @Override
    public String solve(String... in) {
        
        int digits = Integer.parseInt(in[0]);
        
        // Implement (long) pow
        long max = 1;
        for (int i = 0; i < digits; i++) max *= 10;
        
        long p = 0;    
        for (long m = max - 1; m >= max / 10; m--) {
            for (long n = m; n >= max / 10; n--) {
                
                if (m * n < p) break;     // optimization: don't search if less that found pali
                
                if (pali(m * n) > p) p = m * n;                 
            }
        }
        
        return Long.toString(p);
    }
    
    /** 
    * Check if input is a palindrome.
    *
    * @param inp  Number to check.
    * @return     The palindrome itself, otherwise zero.
    */
    private long pali(long inp) {
        
        long d = inp;
        long r = 0;
        
        while (d != 0) {
            r = r * 10 + d % 10;
            d /= 10;
        }
        
        if (r == inp) return r;
        else return 0L;        
    }
    
    // Stand-alone test-run
    public static void main(String args[]) {
        
        System.out.println("\n ANS: " + new eu004().solve("2"));
        
    }    
}