#include <SFML/Graphics.hpp>
#include <Circle.hpp>
#include <Game.hpp>

int main()
{
    gd::Game game(1920, 1080, "Game");
    game.Setup(10);

    game.LifeCycle();
  
    return 0;
}