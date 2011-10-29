#include <sys/types.h>

#include <stdio.h>
#include <math.h>

int
ispentagonal(uint x)
{
	double n;

	n = (0.5 + sqrt(0.25 + 6 * x)) / 3;
	return ((uint)n == n);
}

uint
p044(void)
{
	uint n, m, s, d;

	for (m = 1;; ++m) {
		for (n = 1; n < m; ++n) {
			s = 0.5 * (n * (3 * n - 1) + m * (3 * m - 1));

			if (ispentagonal(s)) {
				d = 0.5 * (-3*n*n+3*m*m+n-m);

				if (ispentagonal(d))
					return (d);
			}
		}
	}
}

int
main(void)
{
	printf("%u\n", p044());
	return (0);
}
