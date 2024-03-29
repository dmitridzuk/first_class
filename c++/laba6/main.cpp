#include <SFML/Graphics.hpp>

int main()
{
    sf::RenderWindow window(sf::VideoMode(1920, 1080), "SFML Image");
    sf::Texture backgroundTexture;
    if (!backgroundTexture.loadFromFile("1.jpg"))
    {
        return -1; 
    }
    sf::Sprite background(backgroundTexture);

    sf::Texture spaceshipTexture;
    if (!spaceshipTexture.loadFromFile("2.jpg"))
    {
        return -1; 
    }
    sf::Sprite spaceship(spaceshipTexture);

    background.setPosition(0, 0);
    spaceship.setPosition(400, 300);

    while (window.isOpen())
    {

        sf::Event event;
        while (window.pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
            {
                window.close();
            }
        }
        sf::Vector2f movement(0.f, 0.f);
        float speed = 1/4.f;

        if (sf::Keyboard::isKeyPressed(sf::Keyboard::Up))
            movement.y -= speed;
        if (sf::Keyboard::isKeyPressed(sf::Keyboard::Down))
            movement.y += speed;
        if (sf::Keyboard::isKeyPressed(sf::Keyboard::Left))
            movement.x -= speed;
        if (sf::Keyboard::isKeyPressed(sf::Keyboard::Right))
            movement.x += speed;

        spaceship.move(movement);
        window.clear();
        window.draw(background);
        window.draw(spaceship);
        window.display();
    }
    return 0;
}
