#include <iostream>
#include "func.h"
int main()
{
    float dlina, shirina;
    
    std::cout << "input dlina rectangle: ";
    std::cin >> dlina;
    
    std::cout << "input shirina rectangle: ";
    std::cin >> shirina;
    
    if ((dlina > 0) && (shirina > 0)) {
            
        Rectangle rectangle(dlina, shirina);
            
        std::cout << "Ploshad: " << rectangle.S() << "\n";
        std::cout << "Perimetr: " << rectangle.P() << "\n";
        std::cout << "Diagonal: " << rectangle.D() << "\n";
        
    }
    
    else
    {
        std::cout << "incorrect rectangle";
        return 0;
    }
}