import tkinter
import pandas

import os
os.system('say "Beer time."')

def button_clicked():
    print("button clicked")
    code_list = {row.symbol: row.morse for (index, row) in df.iterrows()}
    # print(code_list)
    phrase = (my_input.get()).upper()
    word_right = True

    while word_right == True:
        try:
            output_list = [code_list[symbol] for symbol in phrase]
            print(output_list)
        except KeyError:
            print("Do not enter spaces")
            word_right = False
        else:
            print("Entering else")
            word_right = False
    my_output.config(text=output_list)

df = pandas.read_csv("morse.csv")

window = tkinter.Tk()

window.title("Morse Code Generator")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

my_label = tkinter.Label(text = "Your Text: ", font=("Arial", 24, "italic"))
my_label.grid(column = 0, row = 0)

my_input = tkinter.Entry(width = 50)
my_input.grid(column = 1, row = 0)

my_output = tkinter.Label(text = "Morse Code:", font = ("Arial", 24, "italic"))
my_output.grid(column=1, row=2, columnspan=2)

my_button = tkinter.Button(text= "Generate", command=button_clicked, font=("Arial", 24, "italic"))
my_button.grid(column = 0, row = 1)

window.mainloop()