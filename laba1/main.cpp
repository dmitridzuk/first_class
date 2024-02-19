#include <iostream>
#include "func.h"
using namespace std;

int main()
{
    setlocale(LC_ALL, "rus");

    std::string filename = "input.txt";

    gd::appendTimeToFile(filename);

    std::cout << "Информация записана в файл " << filename << std::endl;

    return 0;
}