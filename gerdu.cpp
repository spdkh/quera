// Example program
#include <iostream>

int main()
{
  int n,x,y;
  int a, b;
  int i, j;
  a = -1;

  std::cin >> n >> x >> y;
  if (x>y)
    b = n / y +1;
  else
    b = n / x+1;
    for (i = 0; i < b; i++)
    {
        for (j = 0; j < b; j++)
        {
            if((i * x) + (j * y) == n) 
            {
                std::cout << i << " " << j;
                a = 1;
                break;
            }
        }
        if(a > -1)
            break;
    }

    if (i == b && j == b)
        std::cout<<-1;
}
