
#include <iostream>
#include <time.h>

using namespace std;
int main()
{
    time_t start = time(NULL);
    int q1, c1, c2 = 0;
    cin >> q1;
    const int q = q1;
    int a[q];

    for (int j = 0; j < q; j++)
            cin >> a[j];
        
    for(int i = 1; i <= 1000; i++)
    {
        
        c1 = 0;
        for (int j = 0; j < q; j++)
        {
            if(i % a[j] == 0)
            {
                c1++;
                // cout << a[j];
            }
        }
        if(c1 == q)
            c2++;
    }
    cout << c2 << endl;
    
    time_t end = time(NULL);
    std::cout<<"Execution Time: "<< (double)(end-start)<<" Seconds"<<std::endl;
    return 0;
}
