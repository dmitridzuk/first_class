#include <iostream>
#include "func.h"
int main()
{
    float dlina, shirina;
    std::cin >> "input dlina rectangle " >> dlina >> "\n";
    std::cin >> "input shirina rectangle " >> shirina >> "\n";
    Rectangle rectangle(dlina, shirina);
    std::cout << "Ploshad: " << rectangle.S() << "\n";
    std::cout << "Perimetr: " << rectangle.P() << "\n";
    std::cout << "Diagonal: " << rectangle.D() << "\n";
}