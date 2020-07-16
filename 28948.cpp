#include <iostream>
#include <math.h>
using namespace std;
int main()
{
	string s;
	cin >> s;
	int l = s.length(), i = 0;
	
	while (s[i]!='\0')	
	{
		if(s[i] == '=')
		{
			
			if(i == 0)
				s.erase(i,1);
			else
			{
				i--;
				s.erase(i, 2);
			}
		}
		else
			i++;
		
	}
	cout<<s;
	return 0;
}
