import tkinter as tk
import random


#create a window

window = tk.Tk()
window.geometry("600x400")
window.config(bg = "#6699CC")
window.resizable(width=False,height=False)
window.title("Guess The Number-BRAIN'IN'")


TARGET = random.randint(100, 500)
RETRIES = 0
 
 
def retry(text):
    result.configure(text=text)
 
# Create a new game
def new_game():
    guess_b.config(state='normal')
    global TARGET, RETRIES
    TARGET = random.randint(0, 1000)
    RETRIES = 0
    retry(text="Guess a number between\n 100 and 500")
 
# Continue the ongoing game or end it
def play_game():
    global RETRIES
 
    choice = int(number_form.get())
    if choice >500 or choice<0:
        
        retry("check your input")
     
    if choice != TARGET:
        RETRIES += 1
     
        result = "Wrong Guess!! Try Again"

        
    retry(result)
 

 

# Entry Fields
guessed_number = tk.StringVar()
number_form = tk.Entry(window,font=("Arial",14),textvariable=guessed_number)

 

number_form.place(x=100, y=150)
exit_b = tk.Button(window,text="EXIT",font=("Arial",14),fg="#b82741", bg="White",command=exit)
exit_b.place(x=300,y=320)
# Heading of our game
title = tk.Label(window,text="Guess The Number Game",font=("Arial",24,"bold","italic"),fg="black",bg="#6699CC")
 
# Result and hints of our game
result = tk.Label(window, text="Click on Play to start a new game", font=("Arial", 12, "normal", "italic"),fg = "White", bg="#6699CC", justify=tk.LEFT)
 
# Display labels
title.place(x=100, y=50)
result.place(x=100, y=210)
play_b = tk.Button(window, text="PLAY",font=("Arial",14,"bold","italic"),fg="Black",bg="#6699CC",command=new_game)
guess_b = tk.Button(window,text="GUESS",font=("Arial",12), fg="#13d675",bg="Black",command=play_game)
play_b.place(x=200,y=320)
guess_b.place(x=350,y = 147)
window.mainloop()

