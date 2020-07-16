#include <iostream>
#include<math.h>

using namespace std;

long long unsigned int ffact(long long unsigned int n)
{
//	long long unsigned int m = n % 10000;
	cout << n << endl;
	if (n <= 1) return 1;
	for (int i = 7; i > 0; i--)
	{
//		cout << n << '-' << i << endl;
		if (n % (int)pow(5, i) == 0) 
			return (ffact(n - 1)*n / (int)pow(10, i) )% 100;
	}
	return (ffact(n - 1) * n) % 100;

}
int main()
{
	long long unsigned int n = 7205759403792793;
	cin >> n;
//	for (int i = 65000; i <= 65500; i++)
//		cout << i << ": " << ffact(i) << endl;
	cout << ffact(n)  ;
    return 0;
}
