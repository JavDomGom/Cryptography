/*
 * dec2hex.c v0.01
 * Copyleft - 2018  Javier Dominguez Gomez
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
 * Compilation: gcc -Wall dec2hex.c -o dec2hex
 *
 * Usage: ./dec2hex decimalNumber0 decimalNumber1 ... decimalNumberN
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <libgen.h>
#include <getopt.h>
#include <ctype.h>

const float version = 0.01;
const int versionYear = 2018;

void help(char *self) {
	printf(" HELP\n\n");
	printf("\t%s v%1.2f (%d)\n\n", self, version, versionYear);
	printf("\tThis program is a converter of decimal numbers  or base 10 to hexadecimal\n");
	printf("\tnumbers or base 16. It requires specifying one or more numbers in decimal\n");
	printf("\tformat as arguments.\n\n");
	printf("\tUsage:\t\t./%s decimalNum0 decimalNum1 ... decimalNumN\n\n", self);
	printf("\tExample:\t./%s 123 456 7398\n\n", self);
	printf("\tOutput:\t\t123 -> 7B\n");
	printf("\t\t\t456 -> 1C8\n");
	printf("\t\t\t7398 -> 1CE6\n\n");
}

int main(int argc, char *argv[]) {

	if(argc == 1) {
		help(basename(argv[0]));
		return 1;
	}

	unsigned long long decimalNumber;
	int i, c, option, flag;

	while ((option = getopt(argc, argv, "vh")) != -1) {
		switch (option) {
		case 'v':
			fprintf(stdout, "v%1.2f\n", version);
			return 0;
			break;
		case 'h':
			help(basename(argv[0]));
			return 0;
			break;
		case '?':
			if (isprint(optopt))
				fprintf(stderr, "Unknow option '-%c'.\n", optopt);
			else
				fprintf(stderr, "Unknow char '\\x%x'.\n", optopt);
			return 1;
		default:
			return 1;
		}
	}

	for (i = 1; i < argc; i++) {
		flag = 0;
		for (c = 0; c <= strlen(argv[i]) - 1; c++) {
			if (argv[i][c] < 48 || argv[i][c] > 57) {
				printf("%s -> Is not decimal value!\n", argv[i]);
				flag = 1;
				break;
			}
		}

		if (flag == 0) {
			sscanf(argv[i], "%llu", &decimalNumber);
			printf("%llu -> %llX\n", decimalNumber, decimalNumber);
		}
	}

	return 0;
}
