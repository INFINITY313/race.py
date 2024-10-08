import arcade
import arcade.color
import arcade.color
import arcade.key
import arcade.key
import random


SCREEN_WIDTH = 1070
SCREEN_HEIGHT = 920
CAR_SPEED = 8
CAR_ANGLE = 20
WALL_SPEED = 6



class Car(arcade.Sprite):
    def update(self):
        if self.right > SCREEN_WIDTH:
            self.right = SCREEN_WIDTH
        elif self.left < 0:
            self.left = 0
        else:
            self.center_x += self.change_x

class Wall(arcade.Sprite):
    def update(self):
        self.center_y -= WALL_SPEED
        # if self.top <= 0:
            # self.bottom = SCREEN_HEIGHT
            # self.center_x = random.randint(360,SCREEN_WIDTH -360)

class Game(arcade.Window):

    def __init__(self,width: int = SCREEN_WIDTH, height: int = SCREEN_HEIGHT, title: str | None = 'Arcade Window'):
        super().__init__(width, height, title)
        self.bg = arcade.load_texture("assets/images/road.png")
        self.car = Car("assets/images/car1.png",0.4)
        self.wall = Wall("assets/images/wall.png",0.6)
        self.score = 0
        self.is_game = True
        self.setup()
    
    def setup(self):
        self.car.center_x = SCREEN_WIDTH /2
        self.car.center_y = 200
        self.wall.center_x = random.randint(360,SCREEN_WIDTH -360)
        self.wall.bottom = SCREEN_HEIGHT

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rectangle(SCREEN_WIDTH /2,SCREEN_HEIGHT /2,SCREEN_WIDTH,SCREEN_HEIGHT,self.bg)
        self.car.draw()
        self.wall.draw()
        if self.is_game == False:
            arcade.draw_text("oops,you crashed",SCREEN_WIDTH /2 -100,SCREEN_HEIGHT /2,arcade.color.RED_VIOLET,font_size=35)
        arcade.draw_text(f"score: {self.score}",40,SCREEN_HEIGHT - 50,arcade.color.BLACK,20)

    def update(self, delta_time: float):
        if self.is_game:
            if self.wall.top <= 0:
                self.score += 1
                self.wall.bottom = SCREEN_HEIGHT
                self.wall.center_x = random.randint(360,SCREEN_WIDTH -360)

            self.car.update()
            self.wall.update()
            if arcade.check_for_collision(self.car,self.wall):
                self.is_game = False
            

    def on_key_press(self, symbol: int, modifiers: int):
        if self.is_game:
            if symbol == arcade.key.LEFT:
                self.car.change_x = -CAR_SPEED
                self.car.angle = CAR_ANGLE
            elif symbol == arcade.key.RIGHT:
                self.car.change_x = CAR_SPEED
                self.car.angle = -CAR_ANGLE

    def on_key_release(self, symbol: int, modifiers: int):
        if self.is_game:
            if symbol in [arcade.key.LEFT,arcade.key.RIGHT]:
                self.car.change_x = 0
                self.car.angle = 0

window = Game()

arcade.run()