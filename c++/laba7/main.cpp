#include <SFML/Graphics.hpp>
#include <cstdlib>
#include <ctime>
#include <vector>
void createNewTargets(std::vector<sf::Sprite>& targets, sf::Texture& targetTexture)
{
    for (int i = 0; i < 7; i++)
    {
        sf::Sprite target;
        target.setTexture(targetTexture);
        target.setPosition(static_cast<float>(rand() % 1920), static_cast<float>(rand() % 1080)); // Установка случайной позиции мишени
        targets.push_back(target);
    }
}

int main()
{
    sf::RenderWindow window(sf::VideoMode(1920, 1080), "New Game!");
    
    sf::Texture targetTexture;
    if (!targetTexture.loadFromFile("Images/meteor.png"))
    {
        return -1;
    }

    std::vector<sf::Sprite> targets; // Вектор спрайтов объектов-мишеней

    // Создание объектов-мишеней и добавление их в вектор


    createNewTargets(targets, targetTexture);

    sf::Texture backgroundTexture;
    if (!backgroundTexture.loadFromFile("Images/background.png"))
    {
        return -1;
    }

    sf::Sprite background;
    background.setTexture(backgroundTexture);

    sf::Texture spaceshipTexture;
    if (!spaceshipTexture.loadFromFile("Images/spaceship.png"))
    {
        return -1;
    }

    sf::Sprite spaceship;
    spaceship.setTexture(spaceshipTexture);
    spaceship.setPosition(400, 300); // Установка начальной позиции корабля

    float spaceshipSpeed = 0.3f; // Скорость перемещения корабля

    sf::Texture meteorTexture;
    if (!meteorTexture.loadFromFile("Images/3.jpg"))
    {
        return -1;
    }

    sf::Texture bulletTexture;
    if (!bulletTexture.loadFromFile("Images/bullet.jpg"))
    {
        return -1;
    }

    std::vector<sf::Sprite> meteors; // Вектор спрайтов метеоров
    std::vector<sf::Sprite> bullets; // Вектор спрайтов пуль

    srand(static_cast<unsigned int>(time(0)));

    float bulletSpeed = 2.0f;
    sf::Vector2f velocity(0.0f, 0.0f);
    while (window.isOpen())
    {
        sf::Event event;
        while (window.pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
            {
                window.close();
            }
            else if (event.type == sf::Event::KeyPressed)
            {

                if (event.key.code == sf::Keyboard::W)
                {
                    velocity.y = -spaceshipSpeed; // Движение вверх
                }
                else if (event.key.code == sf::Keyboard::A)
                {
                    velocity.x = -spaceshipSpeed; // Движение влево
                }
                else if (event.key.code == sf::Keyboard::S)
                {
                    velocity.y = spaceshipSpeed; // Движение вниз
                }
                else if (event.key.code == sf::Keyboard::D)
                {
                    velocity.x = spaceshipSpeed; // Движение вправо
                }
                else if (event.key.code == sf::Keyboard::Space)
                {
                    // Создание пули и добавление в вектор пуль
                    sf::Sprite bullet;
                    bullet.setTexture(bulletTexture);
                    bullet.setPosition(spaceship.getPosition());
                    bullets.push_back(bullet);
                }
            }
            else if (event.type == sf::Event::KeyReleased)
            {
                if (event.key.code == sf::Keyboard::W || event.key.code == sf::Keyboard::S)
                {
                    velocity.y = 0.0f; // Остановка по вертикали
                }
                else if (event.key.code == sf::Keyboard::A || event.key.code == sf::Keyboard::D)
                {
                    velocity.x = 0.0f; // Остановка по горизонтали
                }
            }
        }

        spaceship.move(velocity);
        sf::Sprite meteor;
        if (meteor.getPosition().y > 1080)
        {
            float randomX = static_cast<float>(rand() % 1920); // Случайная позиция по X
            float randomY = static_cast<float>(-rand() % 1080); // Случайная позиция по Y
            meteor.setPosition(randomX, randomY);
        }
        if (spaceship.getPosition().x < 0)
            spaceship.setPosition(0, spaceship.getPosition().y);
        else if (spaceship.getPosition().x > 1920 - spaceship.getGlobalBounds().width)
            spaceship.setPosition(1920 - spaceship.getGlobalBounds().width, spaceship.getPosition().y);
        if (spaceship.getPosition().y < 0)
            spaceship.setPosition(spaceship.getPosition().x, 0);
        else if (spaceship.getPosition().y > 1080 - spaceship.getGlobalBounds().height)
            spaceship.setPosition(spaceship.getPosition().x, 1080 - spaceship.getGlobalBounds().height);

        meteor.move(0, bulletSpeed);

        // Перебор всех пуль в векторе и обновление их позиции
        for (size_t i = 0; i < bullets.size(); i++)
        {
            bullets[i].move(0, -bulletSpeed);
            // Проверка столкновения пули с метеором
            if (bullets[i].getGlobalBounds().intersects(meteor.getGlobalBounds()))
            {
                // Удаление пули и метеора из векторов
                bullets.erase(bullets.begin() + i);
                meteor.setPosition(1920, -1080);
                break;
            }
        }
        for (size_t i = 0; i < bullets.size(); i++)
        {
            for (size_t j = 0; j < targets.size(); j++)
            {
                if (bullets[i].getGlobalBounds().intersects(targets[j].getGlobalBounds()))
                {
                    // Удаление пули и объекта-мишени из векторов
                    bullets.erase(bullets.begin() + i);
                    targets.erase(targets.begin() + j);
                    break;
                }
            }
        }
        if (targets.empty())
        {
            createNewTargets(targets, targetTexture);
        }

        window.clear();
        window.draw(background);
        window.draw(spaceship);
        window.draw(meteor);

        for (const auto& target : targets)
        {
            window.draw(target);
        }

        for (const auto& bullet : bullets)
        {
            window.draw(bullet);
        }
        window.display();
    }
    return 0;
}