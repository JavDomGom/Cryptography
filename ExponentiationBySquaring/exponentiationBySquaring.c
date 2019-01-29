/* 
 * exponentiationBySquaring.c v0.01
 * Copyleft - 2019  Javier Dominguez Gomez
 * Written by Javier Dominguez Gomez <jdg@member.fsf.org>
 * GnuPG fingerprint: 94AD 19F4 9005 EEB2 3384 C20F 5BDC C668 D664 8E2B
 * Madrid, Spain
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Compilation: gcc -Wall exponentiationBySquaring.c -o exponentiationBySquaring
 *
 * Usage: ./exponentiationBySquaring
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

char *dec2bin(int);

int main(int argc, char *argv[]) {

	// A^B mod n = x
	// You can change this values.
	long long A = 17;
	long long B = 300;
	long long n = 40555;

	// Initial value for x
	long long x = 1;

	char *p = dec2bin(B);
	printf("B_(10): %lld\nB_(2):  %s (32 bits)\n\n", B, p);

	int i, k = strlen(p), y = 0;

	for (i = k - 1; i >= 0; i--, y++) {
		printf("b_%-2d = %c\t", i, p[y]);
		long xPow2 = pow(x, 2);

		if (p[y] == '0') {
			printf("x = %lld^2 mod %lld", x, n);
			x = xPow2 % n;
		} else if (p[y] == '1') {
			printf("x = %lld^2 * %lld mod %lld", x, A, n);
			x = (xPow2 * A) % n;
		}
		printf(" -> x = %lld\n", x);
	}

	free(p);
	return 0;
}

char *dec2bin(int n) {
	int c, d, count;
	char *p;

	count = 0;
	p = (char*) malloc(32 + 1);

	if (p == NULL) {
		exit(EXIT_FAILURE);
	}

	for (c = 31; c >= 0; c--) {
		d = n >> c;

		if (d & 1) {
			*(p + count) = 1 + '0';
		} else {
			*(p + count) = 0 + '0';
		}
		count++;
	}
	*(p + count) = '\0';

	return p;
}

