from board import Board
import time

class Button:
    
    def __init__(self, gpio_object, pin):
        self.__board = gpio_object
        self.pin = pin
        self.__button()
        self.__pressed = False
        
    @property
    def pressed(self):
        return self.__pressed

    @pressed.setter
    def pressed(self, value):
        self.__pressed = value

    def __button(self):
        self.__board.GPIO.setup(self.pin, self.__board.GPIO.IN, pull_up_down = self.__board.GPIO.PUD_UP)
        
    def __my_callback(self, channel):
        self.pressed = True
  
rpi = Board()

while True:
    button = Button(rpi, 24)
    if button.pressed:
        print('Button Pressed')
        button.pressed = False
        time.sleep(0.2)
rpi.GPIO.cleanup()