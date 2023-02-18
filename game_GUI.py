import tkinter as tk
import random
from game_GUI_Player import Player 
from game_GUI_Obs import Object

# Funcion de nuevo juego
def game_loop(canvas, Jugador1,Jugador2,objects):
    # movimiento jugador
    canvas.bind_all('<Left>', lambda event: Jugador1.move_left())
    canvas.bind_all('<Right>', lambda event: Jugador1.move_right())
    canvas.bind_all('<Up>', lambda event: Jugador1.move_up())
    canvas.bind_all('<Down>', lambda event: Jugador1.move_down())

    canvas.bind_all('<a>', lambda event: Jugador2.move_left())
    canvas.bind_all('<d>', lambda event: Jugador2.move_right())
    canvas.bind_all('<w>', lambda event: Jugador2.move_up())
    canvas.bind_all('<s>', lambda event: Jugador2.move_down())

    # movimiento de objetos
    for obj in objects:
        obj.move_down()

    # Revision de colisiones
    for obj in objects:
        if (Jugador1.x < obj.x + obj.width and Jugador1.x + Jugador1.width > obj.x and Jugador1.y < obj.y + obj.height and Jugador1.y + Jugador1.height > obj.y):
            #canvas.delete("all")
            canvas.create_text(300/2, 500/2, text=" Ganador \nJugador 2", font=("Arial", 32), fill="black")
            return

        if (Jugador2.x < obj.x + obj.width and Jugador2.x + Jugador2.width > obj.x and Jugador2.y < obj.y + obj.height and Jugador2.y + Jugador2.height > obj.y):
            #canvas.delete("all")
            canvas.create_text(300/2, 500/2, text=" Ganador \nJugador 1", font=("Arial", 32), fill="black")
            return
        
    # Agregar un objeto de manera aleatoria
    if random.randint(1, 6) == 1:
        obj = Object(random.randint(0, 300 - 20), 0 - 20)
        objects.append(obj)

    # limpiar canvas
    canvas.delete("all")

    # Dibujar jugador y objetos
    Jugador1.draw(canvas)
    Jugador2.draw(canvas)
    for obj in objects:
        obj.draw(canvas)


    # Actualizar el espacio
    canvas.update()

    # continuar con el loop de juego
    canvas.after(50, game_loop, canvas, Jugador1,Jugador2, objects)

# Crear una ventana 
root = tk.Tk()
root.title("Ejercicio git")

# Crear un nuevo espacio
canvas = tk.Canvas(root, width=300, height=500, bg="sky blue")
canvas.pack()

# Crear jugador
Jugador1 = Player(300/2 - 20/2, 500 - 20, 'green')
Jugador2 = Player(300/2 - 20/2, 500 - 20, 'blue')


# Create the objects
objects = []

# Empezar el juego 
game_loop(canvas, Jugador1, Jugador2, objects)

root.mainloop()