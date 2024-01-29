#pragma once
class   Rectangle
{
private:
    float a;
    float b;
public:
    Rectangle(float a, float b) : a(a), b(b)
    {
    }
    float S();
    float P();  
    float D();
};