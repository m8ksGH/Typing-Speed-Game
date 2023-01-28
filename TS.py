from pyfiglet import figlet_format
from termcolor import colored

ascii_art = figlet_format('WELCOME TO TYPING SPEED GAME!!!')
colored_ascii = colored(ascii_art, 'yellow')
print(colored_ascii)

import sys
import time

def anything(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.02)

anything("Greetings player here is a test to check your Typing speed, please try to type the sentence as fast as you can thank you!\n")

name = input("Please Enter you name: ")

import time
import tkinter as tk

def typing_speed_test(words):
    start_time = time.time()

    # get the user's input
    typed_text = input("\n" +  name + " type the following text as fast as you can: \n\n" + words + "\n")

    # calculate the elapsed time
    elapsed_time = time.time() - start_time

    # compare the typed text to the original text
    if typed_text == words:
        print("\nCORRECTLY COMPLETED! ")
        root = tk.Tk()
        root.title("Typing Speed Checker")
        root.geometry("600x300")


        label = tk.Label(root, text="CORRECTLY COMPLETED! \nPlease click the X button on the \nupperright \ncorner to show your speed", width= 600, height= 300,
        bg= "black", fg= "yellow", font=('Arial',30,'bold'))

        label.pack()

        root.mainloop()
        
    else:
        print("\nNOT COMPLETED CORRECTLY! \nPlease try again.")
        root = tk.Tk()
        root.title("Typing Speed Checker")
        root.geometry("600x300")


        label = tk.Label(root, text="NOT COMPLETED CORRECTLY! \nPlease try again. \nPlease. click the X button on the \nupperright \ncorner to show your speed", width= 600, height= 300,
        bg= "black", fg= "yellow", font=('Arial',25,'bold'))

        label.pack()

        root.mainloop()
       

    # calculate the typing speed (in words per minute)
    typing_speed = len(words.split()) / (elapsed_time / 60)
    print("\nYour typing speed is {:.0f} words per minute.".format(typing_speed))
    root = tk.Tk()
    root.title("Typing Speed Checker")
    root.geometry("600x300")


    label = tk.Label(root, text="Your\n typing speed is {:.0f} words\n per minute.".format(typing_speed), width= 600, height= 300,
    bg= "black", fg= "yellow", font=('Arial',30,'bold'))

    label.pack()

    root.mainloop()

# test the typing speed test function
typing_speed_test("Aesop was one of the great Greek writers. He is best known for his fables, stories that have a moral. They teach us something about how we should live our lives.")

