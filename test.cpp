#include <iostream>
#include <string>
/* run this program using the console pauser or add your own getch, system("pause") or input loop */
// #include "x.h"
using namespace std;

template <class T>
T sum(T a, T b)
{
	return a + b;
}
int main() {
	cout << sum(1.2, 2.3);
	auto p = 2;
//	cout << p * 2;
	// x <char> aa('a');
	// x <double> bb(5);
	string a = "hello";
//	char* b = "world";
	cout << endl << a.length();
//	b.shrink_to_fit();
	return 0;
}