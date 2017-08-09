#include <iostream>
#include <cmath>
#include <algorithm>

bool is_sub_string_divisible(int a[10])
{
    const int d1 = a[1]*100 + a[2]*10 + a[3];
    const int d2 = a[2]*100 + a[3]*10 + a[4];
    const int d3 = a[3]*100 + a[4]*10 + a[5];
    const int d4 = a[4]*100 + a[5]*10 + a[6];
    const int d5 = a[5]*100 + a[6]*10 + a[7];
    const int d6 = a[6]*100 + a[7]*10 + a[8];
    const int d7 = a[7]*100 + a[8]*10 + a[9];
    if ((d1 % 2 == 0) and (d2 % 3 == 0) and (d3 % 5 == 0) and (d4 % 7 == 0) 
        and (d5 % 11 == 0) and (d6 % 13 == 0) and (d7 % 17 == 0))
        return true;
    return false;
}

int permute_and_check()
{
    long sum = 0;
    int arr[10] = {0,1,2,3,4,5,6,7,8,9};
    std::sort(arr,arr+10);
    do {
        int a[10] = {arr[0],arr[1],arr[2],arr[3],arr[4],arr[5],arr[6],arr[7],arr[8],arr[9]};
        if (is_sub_string_divisible(a)) {
            long long_that_works = 
                (arr[0]*pow(10,9) + arr[1]*pow(10,8) + arr[2]*pow(10,7) + 
                arr[3]*pow(10,6) + arr[4]*pow(10,5) + arr[5]*pow(10,4) + 
                arr[6]*pow(10,3) + arr[7]*pow(10,2) + arr[8]*pow(10,1) + 
                arr[9]*pow(10,0));
            std::cout << long_that_works << " satisfies the conditions.\n";  
            sum += long_that_works;
        }
    } while (std::next_permutation(arr,arr+10));
    std::cout << "The sum is: " << sum << "\n";
    return sum;
}

int main() 
{
    permute_and_check();
}
