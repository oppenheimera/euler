#include <iostream>
#include <math.h>
#include <vector>

int LIMIT = 28123;

bool is_abundant(int n) 
{
    int sum = 0;
    for (int i = 1; i < n/2 + 1; ++i) {
        if (n % i == 0) {
            sum += i;
        }
    }
    return sum > n;
}

bool two_sum_decision(int target, std::vector<int> v)
{
    int low_pointer = 0;
    int high_pointer = v.size() - 1;
    while (low_pointer <= high_pointer) {
        int temp_sum = v.at(low_pointer) + v.at(high_pointer);
        if (temp_sum == target) { return true; }
        else if (temp_sum > target) { high_pointer -= 1; }
        else { low_pointer += 1; }
    }
    return false;
}

int main()
{   
    std::vector<int> abundants;
    int sum = 0;

    for (int i = 1; i < LIMIT; ++i) {
        if (is_abundant(i)) { 
            abundants.push_back(i); 
        }
    }
    for (int n = 1; n < LIMIT; ++n) {
        if (!two_sum_decision(n, abundants)) {
            sum += n;
        }
    }

    std::cout << sum << "\n";    
   
    return 0;
}