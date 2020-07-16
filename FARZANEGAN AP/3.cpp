
#include <iostream>

using namespace std;
int main()
{
	int flag = 0;
	
	int n , r;
	cin >> n;

	for (int i = 3; i <= n / 4; i++)
	    for (int j = i + 1; j < n / 2; j++)
	    {
	        r = n - i - j;
	        if (r * r == i * i + j * j)
	        {		
	            cout << i << ' ' << j<< ' ' << r << endl;
	            flag = 1;
	            break;
	        }
	    if (flag == 1)
	        break;
	    }
	
	if (flag == 0)
	    cout << "Impossible";
   
    return 0;
}
