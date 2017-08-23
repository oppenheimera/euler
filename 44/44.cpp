#include <iostream>
#include <math.h>
#include <cmath>

int nth_pentagonal(int n) 
{
    return n * (3 * n - 1) / 2;
}

bool is_pentagonal(int n)
{
    if (n > 0) {
        float i = (sqrt((24 * n) + 1) + 1) / 6;
        if (i - (int) i == 0 and i > 0) {
            return true;
        }
    }
    return false;
}

bool satisfies_both_conditions(int i, int j) 
{
    bool add_cond = is_pentagonal(nth_pentagonal(i) + nth_pentagonal(j));
    bool sub_cond = is_pentagonal(nth_pentagonal(i) - nth_pentagonal(j));
    if (add_cond and sub_cond) {
        return true;
    }
    return false;
}

int main() 
{
    int result = 0;
    bool notfound = true;
    int i = 1; 
    while (notfound) {
        ++i;
        int n = nth_pentagonal(i);
        for (int j = i-1; j > 0; --j) {
            int m = nth_pentagonal(j);
            if (is_pentagonal(n-m) and is_pentagonal(n+m)) {
                result = n-m;
                notfound = false;
                break;
            }
        }
    }
    std::cout << result << "\n";
    
}