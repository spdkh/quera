#include <iostream>

using namespace std;

void ShowFibNth(long int a, long int b)
{
	if (a <= 1 && b <= 1)
		cout << 1 << endl;
	else
	{
		cout << a << endl;
		ShowFibNth(b - a, a);
	}	
}
int main()
{
	int a, b;
	cin >> a >> b;
	ShowFibNth(a, b);
	
	return 0;
}
