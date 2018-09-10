/*
 * hex2bin.c v0.01
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
 * Compilation: gcc -Wall hex2bin.c -o hex2bin
 *
 * Usage: ./hex2bin hexNumber0 hexNumber1 ... hexNumberN
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
	printf("\tThis program is  a converter of  hexadecimal numbers or base 16 to binary\n");
	printf("\tstrings. It requires specifying one or more numbers in hexadecimal format\n");
	printf("\tas arguments.\n\n");
	printf("\tUsage:\t\t./%s hexNum0 hexNum1 ... hexNumN\n\n", self);
	printf("\tExample:\t./%s 1f3a c4b6 78d0\n\n", self);
	printf("\tOutput:\t\t1f3a -> 0001 1111 0011 1010\n");
	printf("\t\t\tc4b6 -> 1100 0100 1011 0110\n");
	printf("\t\t\t78d0 -> 0111 1000 1101 0000\n\n");
}

int main(int argc, char *argv[]) {

	if(argc == 1) {
		help(basename(argv[0]));
		return 1;
	}

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
			if ((argv[i][c] < 48 || argv[i][c] > 57) &&
				(argv[i][c] < 65 || argv[i][c] > 70) &&
				(argv[i][c] < 97 || argv[i][c] > 102)) {
				printf("%s -> Is not hexadecimal value!", argv[i]);
				flag = 1;
				break;
			}
		}

		if (flag == 0) {
			printf("%s -> ", argv[i]);
			for (c = 0; c <= strlen(argv[i]) - 1; c++) {
				switch (argv[i][c]) {
				case 48:	printf("0000 ");break;
				case 49:	printf("0001 ");break;
				case 50:	printf("0010 ");break;
				case 51:	printf("0011 ");break;
				case 52:	printf("0100 ");break;
				case 53:	printf("0101 ");break;
				case 54:	printf("0110 ");break;
				case 55:	printf("0111 ");break;
				case 56:	printf("1000 ");break;
				case 57:	printf("1001 ");break;
				case 65:
				case 97:	printf("1010 ");break;
				case 66:
				case 98:	printf("1011 ");break;
				case 67:
				case 99:	printf("1100 ");break;
				case 68:
				case 100:	printf("1101 ");break;
				case 69:
				case 101:	printf("1110 ");break;
				case 70:
				case 102:	printf("1111 ");break;
				}
			}
		}
		printf("\n");
	}

	return 0;
}

