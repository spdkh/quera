
#include <iostream>
#include <time.h>
int main()
{
	
	unsigned int W;
	unsigned int n;
	std::cin >> n >> W;
	// const unsigned long int W = W1;
	int* w = new int[n]; 
	long long bank = 0, max = 0;

	for(unsigned int i = 0; i < n; i++)
		std::cin >> w[i];
	time_t start = time(NULL);
	for (unsigned int i = 0; i < n; i++)
	{
		if(max == W || w[i] == W)
		{
			max = W;
			break;
		}

		for (unsigned int j = i; j <= n; j++)
		{
			// std::cout << i << " - " << j << std::endl;
			if(max == W)
				break;

			bank = 0;
			for (unsigned int k = i; k <= j; k++)
				bank += w[k];

			if(bank <= W && max < bank)
				max = bank;
			
		}
	}
	std::cout << max;
	delete[] w;  
	time_t end = time(NULL);
    std::cout<<"Execution Time: "<< (double)(end-start)<<" Seconds"<<std::endl;
    return 0;
}
