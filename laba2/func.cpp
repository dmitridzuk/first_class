#include <math.h>
#include "func.h"
float Rectangle::S()
{
	return a * b;
}
float Rectangle::P()
{
	return (a+b)*2;
}
float Rectangle::D()
{
	return sqrt(a * a + b * b);
}