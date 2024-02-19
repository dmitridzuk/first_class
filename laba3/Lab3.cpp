
#include <iostream>
#include <cstring>

class String {
private:
    char* str;

public:
    //  онструктор по умолчанию
    String() : str(nullptr) {}

    //  онструктор с параметром
    String(const char* s) {
        str = new char[strlen(s) + 1];
        strcpy_s(str, strlen(s) + 1, s);
    }

    //  онструктор копировани€
    String(const String& other) {
        str = new char[strlen(other.str) + 1];
        strcpy_s(str, strlen(other.str) + 1, other.str);
    }

    // ќператор присваивани€ копированием
    String& operator=(const String& other) {
        if (this != &other) {
            delete[] str;
            str = new char[strlen(other.str) + 1];
            strcpy_s(str, strlen(other.str) + 1, other.str);
        }
        return *this;
    }

    // ƒеструктор
    ~String() {
        delete[] str;
    }

    // ћетод дл€ вывода строки
    void print() {
        std::cout << str << std::endl;
    }
};

int main() {
    String s1("Hello");
    String s2 = s1; // используем конструктор копировани€
    String s3;
    s3 = s2; // используем оператор присваивани€ копированием

    s1.print();
    s2.print();
    s3.print();

    return 0;
}