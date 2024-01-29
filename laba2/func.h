#pragma once
class   Rectangle
{
private:
    float a;
    float b;
public:
    Rectangle(float dlina, float shirina) : a(dlina), b(shirina)
    {
    }
    float S();
    float P();  
    float D();
};