#include "stdio.h"
/* Possible performance enhancement: Save the last `size` column, and
   add and subtract it to save `size` recomputations.
 */
int pl(int x, int y, int gridserial) {
  int rackid = x+10;
  int powerlevel = y * rackid;
  powerlevel += gridserial;
  powerlevel *= rackid;
  powerlevel = (powerlevel/100)%10;
  powerlevel -= 5;

  return powerlevel;
}

int squarelevel(int x, int y, int size, int gridserial) {
  int total = 0;
  for (int xi = x; xi < x+size; xi++) {
    for (int yi = y; yi < y+size; yi++) {
      total += pl(xi,yi,gridserial);
    }
  }
  return total;
}

int main() {
  int gridserial = 7139;
  int maxx = 0;
  int maxy = 0;
  int maxsize = 0;
  int power = 0;
  for (int size = 0; size <= 300; size++) {
    printf("Processing %dx%d.\n", size,size);
    printf("   Current: (%d,%d,%d) = %d.\n", maxx,maxy,maxsize,power);
    for (int x = 0; x < 300-size; x++) {
      for (int y = 0; y < 300-size; y++) {
	int mypower = squarelevel(x,y,size,gridserial);
	if (mypower > power) {
	  power = mypower;
	  maxx = x;
	  maxy = y;
	  maxsize = size;
	}
      }
    }
  }
  printf("Max: (%d,%d,%d) = %d\n", maxx, maxy, maxsize, power);
  
  return 0;
}
