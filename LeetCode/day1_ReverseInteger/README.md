source: https://leetcode.com/problems/reverse-integer/

*notes*: 
- keep binary calculator closeby
- when problems involves __reversing__ use __stacks__ pop and push functionality
- before hand get the limits of the function ie MIN MAX values for argument
- work incrementally: +ve ints -> -ve ints -> 0, 1, MIN, MAX, edges
- useful libraries to have
\<stdio.h>
\<stdlib.h>
\<cmath>
\<climits> 

**Time**: O(log10(x)) - length of the integer given  
**Space**: O(1) - only need 3 ints to store result + intermediaries  
