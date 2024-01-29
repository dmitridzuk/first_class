#include <iostream>
#include "func.h"
int main()
{
    float a, b;
    std::cin >> a >> b;
    Rectangle rectangle(a, b);
    std::cout << "Ploshad: " << rectangle.S() << "\n";
    std::cout << "Perimetr: " << rectangle.P() << "\n";
    std::cout << "Diagonal: " << rectangle.D() << "\n";
}