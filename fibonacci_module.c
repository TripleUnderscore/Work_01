

#include <stdint.h>

/* gcc -shared -Wl,-soname,Fibonacci_module -o fibonacci_module.so -fPIC fibonacci_module.c */

uint64_t fibonacci_module(uint64_t indice)
{
	uint64_t n_1 = 1, n_2 = 1, tmp;

	if (indice == 0)
	{
		return 0;
	}
	else
	{
		for (uint64_t i = 2; i < indice; i++)
		{
			tmp = n_1;
			n_1 = tmp + n_2;
			n_2 = tmp;
		}
		return n_1;
	}
}
