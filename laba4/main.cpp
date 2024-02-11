#include <SFML/Graphics.hpp>
#include <iostream>

int main()
{
    sf::RenderWindow window(sf::VideoMode(1920, 1080), "SFML works!");
    
    
    
    //int a;
    //std::cout << "Input number of objects (less then 10): ";
    //std::cin >> a;


    sf::CircleShape shape(200.f);
    shape.setFillColor(sf::Color::Yellow);
    shape.setPosition(700, 270);
    window.draw(shape);
    
    sf::CircleShape shape1(80, 3);
    shape1.setFillColor(sf::Color::Magenta);
    shape1.setPosition(500, 270);
    window.draw(shape1);

    sf::RectangleShape shape2;
    shape2.setSize({ 100, 200 });
    shape2.setRotation(-20);
    shape2.setFillColor(sf::Color::Blue);
    shape2.setPosition(300, 270);
    window.draw(shape2);

    sf::RectangleShape shape3(sf::Vector2f(150, 5));
    shape3.setFillColor(sf::Color::Red);
    shape3.setPosition(1100, 270);
    window.draw(shape2);
    
 
    while (window.isOpen())
    {
        sf::Event event;
        while (window.pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
                window.close();
        }

        window.clear();
        window.draw(shape);
        window.draw(shape1);
        window.draw(shape2);
        window.draw(shape3);
        window.display();
    }
}