#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <cmath>
#include <climits> 

class Solution {
#define MAX 0x7fffffff
#define MIN -2147483648
#define MASK 0x1

public:
    int reverse(int x) {
        int pop = x;
        int rev = 0;
        
        while (x != 0) {
            //pop 
            pop = x % 10;
            x = x / 10;

            //push
            if(rev > (INT_MAX/10) || (rev ==INT_MAX/10 && pop > 7)) return 0;
            if(rev < (INT_MIN/10) || (rev == INT_MIN/10 && pop > 8)) return 0;
            rev = rev * 10 + pop; //+ve
        }
        return rev;
    }
};
