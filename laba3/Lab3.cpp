
#include <iostream>
#include <cstring>

class String {
private:
    char* str;

public:
    // ����������� �� ���������
    String() : str(nullptr) {}

    // ����������� � ����������
    String(const char* s) {
        str = new char[strlen(s) + 1];
        strcpy_s(str, strlen(s) + 1, s);
    }

    // ����������� �����������
    String(const String& other) {
        str = new char[strlen(other.str) + 1];
        strcpy_s(str, strlen(other.str) + 1, other.str);
    }

    // �������� ������������ ������������
    String& operator=(const String& other) {
        if (this != &other) {
            delete[] str;
            str = new char[strlen(other.str) + 1];
            strcpy_s(str, strlen(other.str) + 1, other.str);
        }
        return *this;
    }

    // ����������
    ~String() {
        delete[] str;
    }

    // ����� ��� ������ ������
    void print() {
        std::cout << str << std::endl;
    }
};

int main() {
    String s1("Hello");
    String s2 = s1; // ���������� ����������� �����������
    String s3;
    s3 = s2; // ���������� �������� ������������ ������������

    s1.print();
    s2.print();
    s3.print();

    return 0;
}