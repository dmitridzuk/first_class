#include <SFML/Graphics.hpp>

int main()
{
    // Создание окна
    sf::RenderWindow window(sf::VideoMode(1920, 1080), "SFML Image");

    // Загрузка изображений
    sf::Texture backgroundTexture;
    if (!backgroundTexture.loadFromFile("1.jpg"))
    {
        return -1; // Проверка на успешную загрузку изображения
    }
    sf::Sprite background(backgroundTexture);

    sf::Texture spaceshipTexture;
    if (!spaceshipTexture.loadFromFile("2.jpg"))
    {
        return -1; // Проверка на успешную загрузку изображения
    }
    sf::Sprite spaceship(spaceshipTexture);

    // Начальные позиции изображений
    background.setPosition(0, 0);
    spaceship.setPosition(400, 300);

    // Главный цикл приложения
    while (window.isOpen())
    {
        // Обработка событий
        sf::Event event;
        while (window.pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
            {
                window.close();
            }
        }

        // Управление перемещением корабля с помощью клавиш
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

        // Отрисовка изображений
        window.clear();
        window.draw(background);
        window.draw(spaceship);
        window.display();
    }

    return 0;
}
