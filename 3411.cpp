#include <iostream>
#include<math.h>

using namespace std;

long long unsigned int ffact(long long unsigned int n)
{
//	long long unsigned int m = n % 10000;
//	cout << n << endl;
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
	cout << log(16);
//	long long unsigned int n;
//	cin >> n;
//	for (int i = 1; i <= 1000; i++)
//		cout << i << ": " << ffact(i) << endl;
//	cout << ffact(n)  ;
    return 0;
}
