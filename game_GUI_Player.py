#Autor: Jose Rodriguez 19131

# Clase del jugador
class Player:
    def _init_(self, x, y, color):
        self.x = x
        self.y = y
        self.width = 25
        self.height = 25
        self.color = color

    def move_left(self):
        self.x -= 15

    def move_right(self):
        self.x += 15

    def move_up(self):
        self.y -= 15

    def move_down(self):
        self.y += 15

    def draw(self, canvas):
        canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, fill=self.color)