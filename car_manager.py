from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = MOVE_INCREMENT

    def create_car(self):
        num = random.randint(1, 6)
        if num == 1:
            car = Turtle()
            car.shape("square")
            car.color(random.choice(COLORS))
            car.shapesize(1, 2)
            car.penup()
            rand_y = random.randint(-250, 250)
            car.goto(300, rand_y)
            self.all_cars.append(car)

    def move(self):
        for cars in self.all_cars:
            cars.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
