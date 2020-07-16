#include <iostream>
#include <math.h>

using namespace std;

int main()
{
	int n, K;
	cin >> n >> K;
	
	int c[n], min = 5000, min2 = 5000, min_id, min_id2;
	int j = 0, k = 0, l = n / K + 1;
	int cluster[K][l]{};
	for (int i = 0; i < n; i++)
	{
		cin >> c[i];
		if (min > c[i])
		{
			min_id = i;		
			min = c[i];
		}
		else if (c[i] > min && min2 > c[i])
		{
			min_id2 = i;		
			min2 = c[i];
		}	
	}
	
	int cnt = 0, max[K]={0};
	for (int i = 0; i < n; i++)
	{
//		cout << i << k << j << c[i] << min << min2 << endl;
		if ((min == c[i] || c[i] == min2) && k < K - 1)	
		{
			if (j != 0)	
			{
//				cout << "why?";
				cluster[k + 1][0] = c[i];      
				k+=2;
			
				cnt++;
			}
			else
			{
				cluster[k][0] = c[i];
				k++;
				cnt++;
			}
			j = 0;
		}
		else
			{
			cluster[k][j] = c[i];
			j++;
			cnt++;
			}
		
		if ((i + 1) >= l * (k + 1))
		{
			k++;  
			j = 0;
		}
		
	}
	min = 5000;
	for (int k = 0; k < K; k++)
	{
		for (int j = 0; j < l; j++)
		{
			if (max[k] < cluster[k][j])
				max[k] = cluster[k][j];
//			cout << k << j << '-' <<cluster[k][j] << endl;
		}
//		cout << max[k] << endl;
}
	
	for (int k = 0; k < K; k++)
		if (min > max[k])
			min = max[k];
			
	cout << min;
	return 0;		
}
