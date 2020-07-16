// Example program
#include <iostream>

using namespace std;
int bmm(int a, int b);

int main()
{  
    int n2,max;
    cin >> n2;
    
    const int n = n2;

    int x[n];
    for (int i = 0; i < n; i++)
    {
        cin >> x[i];
    }
    max = bmm(x[0],x[1]);

    for (int i = 0; i < (n-1); i++)
        for (int j = i + 1; j < n; j++)
            {

            max = max < bmm(x[i],x[j]) ? bmm(x[i],x[j]) : max;
            }
    
    cout<<(max);
    return 0;
}

int bmm(int a, int b)
{
    int x = a < b? a : b;
    int y = a > b? a : b;
    int out = 1;

    while (out != 0)
    {
        out = y % x;
        y = x;
        x = out;
    }
    return y;
}
