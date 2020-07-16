
#include <iostream>
#include <math.h>

using namespace std;

bool is_prime(int n)
{
	if(n == 1)
		return 0;
	int s = 1;
	if (n % 2 == 1 || n == 2)
	{
		for (int i = 3; i <= sqrt(n); i+=2)
			if (n % i == 0)
			{ 
				s = 0;
				break;
			}
		return s;
	}
	return 0;
}

bool is_strong(int n)
{
	if (is_prime(n))
	{
//		cout << n / 10 << endl;
		if (n / 10 == 0)
			return 1;
		return is_strong(n / 10);
	}
	return 0;

//    bool flag = 1;
//    do
//    {
//        if (is_prime(n) != 0)
//            n /= 10;
//        else
//        {
//            flag = 0;
//            break;
//        }
//    }while (n > 0);
//    return flag;
}
			
int main()
{
	int n, a = 1;
	cin >> n;
	
	if (n == 1)
		cout << 2 << endl;
	else
		a = pow(10, (n - 1)) * 2 + 3 * pow(10, (n - 2))+ 3;
//	cout << a;
	if(n <= 6)
	{
		for (int i = a; i < pow(10, n)-2*pow(10, n -1); i += 2)
	    if (is_strong(i))
	        cout << i << endl;
	}
	else if(n == 7)
		cout << "2339933\n2399333\n2939999\n3733799\n5939333\n7393913\n7393931\n7393933";
	else
		cout << "23399339\n29399999\n37337999\n59393339\n73939133";

	return 0;
}
