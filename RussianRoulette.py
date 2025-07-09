# [WIP] russin roulette
# emptik if you see this you suck at minecraft and life

import tkinter as tk
from tkinter import messagebox
import random
import time

# config
mag = 1  # least number of bullet
bullet = 6  # highest value of bullet, hitting this number will kill whoever is playing

chance = mag / bullet
print("death chance (total bullets vs blanks, div by 2 for the actual player): ", (chance * 100) / 2, "%")

# stuff
hammer = 0  # deciding factor
max_value = 0  # this doesnt function lol [WIP]
player = 1  # starting player; 1 is human, 0 is bot

# la roulette
def roulette():
    global mag, bullet, hammer, player, max_value

    hammer = random.randint(mag, bullet)  # random number from 1 to 6, if the number is 6, it is a real bullet
    max_value += 1

    if player == 1:
        status_label.config(text="Playing against yourself.")
    else:
        status_label.config(text="Playing against bot.")

    root.update()
    time.sleep(random.randint(1,3))

    if (hammer == bullet or max_value == bullet) and player == 1: 
        messagebox.showinfo("Result", "death.")
        player = 0  
    elif (hammer == bullet or max_value == bullet) and player == 0: # cooked :skull:
        messagebox.showinfo("Result", "survival.")
        player = 1  
    else:
        status_label.config(text="blank.") # phew
        root.update()
        time.sleep(random.randint(1,3))
        player = 1 - player
        
def restart_game():
    global hammer
    hammer = random.randint(mag, bullet)
    status_label.config(text="Ready to play?")

def start_game():
    roulette()

# ui shit
root = tk.Tk()
root.title("Russian Roulette")
root.geometry("300x200")

status_label = tk.Label(root, text="pull the trigger?", font=("Arial", 14))
status_label.pack(pady=20)

play_button = tk.Button(root, text="shoot", command=start_game, font=("Arial", 12))
play_button.pack(pady=10)

quit_button = tk.Button(root, text="i get out", command=root.quit, font=("Arial", 12))
quit_button.pack(pady=10)

root.mainloop()
