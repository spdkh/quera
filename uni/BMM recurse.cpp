#include <iostream>
#include <math.h>

using namespace std;

long long unsigned int BMM(long long unsigned int a, long long unsigned int b)
{
	long long unsigned int max, min;
	if (a >= b)
	{
		max = a;
		min = b;
	}	
	else
	{
		max = b;
		min = a;	
	}
	if (min == 0)
		return max;

	return BMM(max % min, min);
}

int main()
{
	long long int a, b;
	cin >> a >> b;
//	cout << 1001 % (-65) << endl;
	cout << BMM(abs(a), abs(b));
	
	return 0;
}
