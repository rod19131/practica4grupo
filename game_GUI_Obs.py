# Parte de Oscar Fuentes 19816
import random
# Clase del obstaculo
class Object:
    def _init_(self, x, y):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20

    def move_down(self):
        band = random.randint(1, 50) 
        if band == 1:
            for i in range(1,3):
                self.x += 10
        elif band == 2:
            for i in range(1,3):
                self.x -= 10
        self.y += 10

    def draw(self, canvas):
        canvas.create_oval(self.x, self.y, self.x + self.width, self.y + self.height, fill="orange")