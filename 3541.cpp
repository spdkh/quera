// Example program
#include <iostream>

using namespace std;
int main()
{
    unsigned int n;
    cin >> n;
    unsigned int k;
    unsigned int c = 0;
    for (unsigned int i = 1; i <= int(n/3); i++)
        for (unsigned int j = i; j <= int(n/2)+1; j++)
        {
            k = n - i - j;
            if (k >= i && k >= j)
            if (i + j > k &&  i + k > j && k + j > i)
            {
                 c++;
                 //cout << i << j << k << endl;
            }
        }
    cout << c;
    return 0;
}
