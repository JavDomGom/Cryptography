/*
 * date2epoch.c v0.01
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
 * Compilation: gcc -Wall date2epoch.c -o date2epoch
 *
 * Usage: ./date2epoch
 */

#include <stdio.h>
#include <time.h>

int main(int argc, char *argv[]) {

	int year, month, day, hour, minute, second;
	struct tm t;
	time_t tod;

	printf("Year: ");
	scanf("%d", &year);
	printf("Month: ");
	scanf("%d", &month);
	printf("Day: ");
	scanf("%d", &day);
	printf("Hour: ");
	scanf("%d", &hour);
	printf("Minute: ");
	scanf("%d", &minute);
	printf("Second: ");
	scanf("%d", &second);

	t.tm_year = year - 1900;
	t.tm_mon = month - 1;	// Month [0-11]
	t.tm_mday = day;
	t.tm_hour = hour + 1;	// GMT+1
	t.tm_min = minute;
	t.tm_sec = second;
	t.tm_isdst = 0;		// DST = 0
	tod = mktime(&t);

	printf("Timestamp epoch: %ld\n", (long) tod);
}

