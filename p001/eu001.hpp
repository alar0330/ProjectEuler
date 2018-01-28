/**
 * Project Euler: Problem #001
**/

#pragma once

#include <type_traits>    // NEED: std::enable_if


/**
 *  @brief  Naive implementation with explicit mod-checks.
 *
 *  @tparam T Type of the input, must be integer.
 *  @return The answer
**/
template <class T, class = typename std::enable_if<std::is_integral<T>::value>::type>
T eu001(T lim) {
    
    T acc = 0;
    
    for (T x = 0; x < lim; x++) {
        
        if (!(x % 3) || !(x % 5)) {
            acc += x;
        }
    }
    
    return acc;
}