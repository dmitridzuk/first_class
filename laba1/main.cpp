#include <iostream>
#include "func.h"
using namespace std;

int main()
{
    setlocale(LC_ALL, "rus");

    std::string filename = "input.txt";

    la::increaseAndWriteRunNumber(filename);
    la::writeCurrentTime(filename);

    std::cout << "���������� �������� � ���� " << filename << std::endl;

    return 0;
}