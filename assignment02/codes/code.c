#include <stdio.h>

int main() {
    // Coordinates of points A and B
    int x1 = 4, y1 = -3; // Point A
    int x2 = 8, y2 = 5;  // Point B

    // Ratio
    int m = 3, n = 1;

    // Calculate coordinates of the dividing point P
    int Px = (m * x2 + n * x1) / (m + n);
    int Py = (m * y2 + n * y1) / (m + n);

    // Print the result
    printf("The coordinates of point P that divides the segment AB in the ratio %d:%d are (%d, %d)\n", m, n, Px, Py);

    return 0;
}
