import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()
screen.listen()
screen.onkey(player.go_up,"Up")

car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.add_car()
    car_manager.move_car()

    #detect car collision
    for  car in car_manager.cars:
        if car.distance(player) <20:
            game_is_on = False
            scoreboard.game_over()

    # crossed successfully
        if player.crossed_finish_line():
            player.go_to_start()
            car_manager.level_up()
            scoreboard.increase_level()


screen.exitonclick()



