#include <SFML/Graphics.hpp>
#include <iostream>



int main() {
    const int N = 5; // Задаем количество фигур

    sf::RenderWindow window(sf::VideoMode(800, 600), "SFML Shapes"); // Создаем окно

    // Создаем круги
    sf::CircleShape circles[N];
    for (int i = 0; i < N; i++) {
        circles[i].setRadius(50.f);
        circles[i].setFillColor(sf::Color::Green);
        circles[i].setPosition(100.f * i, 100.f);
    }

    // Создаем треугольники
    sf::ConvexShape triangles[N];
    for (int i = 0; i < N; i++) {
        triangles[i].setPointCount(3);
        triangles[i].setPoint(0, sf::Vector2f(0.f, 0.f));
        triangles[i].setPoint(1, sf::Vector2f(100.f, 0.f));
        triangles[i].setPoint(2, sf::Vector2f(50.f, 100.f));
        triangles[i].setFillColor(sf::Color::Blue);
        triangles[i].setPosition(100.f * i, 250.f);
    }

    // Создаем прямоугольники
    sf::RectangleShape rectangles[N];
    for (int i = 0; i < N; i++) {
        rectangles[i].setSize(sf::Vector2f(100.f, 50.f));
        rectangles[i].setFillColor(sf::Color::Red);
        rectangles[i].setPosition(100.f * i, 400.f);
    }

    // Создаем линии
    sf::VertexArray lines(sf::Lines, N * 2);
    for (int i = 0; i < N * 2; i += 2) {
        lines[i].position = sf::Vector2f(500.f, 50.f * i);
        lines[i].color = sf::Color::Yellow;
        lines[i + 1].position = sf::Vector2f(700.f, 50.f * i);
        lines[i + 1].color = sf::Color::Yellow;
    }

    while (window.isOpen()) {
        sf::Event event;
        while (window.pollEvent(event)) {
            if (event.type == sf::Event::Closed) {
                window.close();
            }
        }

        window.clear();

        // Отображаем круги, треугольники, прямоугольники и линии
        for (int i = 0; i < N; i++) {
            window.draw(circles[i]);
            window.draw(triangles[i]);
            window.draw(rectangles[i]);
        }
        window.draw(lines);

        window.display();
    }

    return 0;
}