/**
 *  @author  Alexander Arzhanov
 *  @version 28/01/18
 *
 ***********
 *  @brief   Project Euler: Problem #001
 ***********
**/

#pragma once

#include <type_traits>    // NEED: enable_if


/**
 *  @brief  Naive implementation with explicit mod-checks.
 *
 *  Uses template-restriction (SFINAE / type traits).
 *
 *  @tparam T   Type of the input (must be of an integral type).
 *  @tparam D   Type traits guard.
 *  @param  lim The upper limit for the sum (must be of an integral type).
 *  @return     The answer.
**/
template <class T, class D = typename std::enable_if<std::is_integral<T>::value>::type>
T p001(T lim) {
    
    T acc = 0;
    
    for (T x = 0; x < lim; x++) {
        
        if (!(x % 3) || !(x % 5)) {
            acc += x;
        }
    }
    
    return acc;
}