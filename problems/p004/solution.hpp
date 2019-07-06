
/**
 *  @file    eu004.hpp
 *  @author  Alexander Arzhanov
 *  @version 30/01/18
 *
 ***********
 *  @brief   Project Euler: Problem #004
 ***********
**/

#pragma once

#include <type_traits>    // NEED: enable_if

/**
 *  @brief  Naive implementation with nested palindrome lamdba-function.
 *
 *  @tparam    T    Type of input param (must be an integral type).
 *  @param   digits Number of digits that product numbers made of.
 *  @return         The largest palindrome.
**/
template <class T, class = typename std::enable_if<std::is_integral<T>::value>::type>
long eu004(T digits) {
    
    // Lambda returns input if it is palindrome, zero otherwise
    auto pali = [](long inp) {
        
        long d = inp;
        long r = 0;
        
        while (d != 0) {
            r = r * 10 + d % 10;
            d /= 10;
        }
        
        if (r == inp) return r;
        else return 0L;
    };
    
    long max = 1;
    for (int i = 0; i < digits; i++) max *= 10;
    
    long p = 0;    
    for (long m = max - 1; m >= max / 10; m--) {
        for (long n = m; n >= max / 10; n--) {
            
            if (m * n < p) break;   // optimization: don't search if less that found pali
            
            if (pali(m * n) > p) p = m * n;
             
        }
    }
    
    return p;
}