from tkinter import *

window = Tk()
window.title('My first GUI programm')
window.minsize(width=500, height=300)

# Label
my_label = Label(text='I am a Label', font=('Arial', 24, 'bold'))
my_label.pack(side="left")

# my_label['text'] = 'New Text'
# my_label.config(text="New Text")

# Button
def button_clicked():
    # print('I got clicked')
    if input_info.get() != "":
        new_text = input_info.get()
    else: 
        new_text = 'Type something'
    my_label.config(text=new_text)


button = Button(text='Click me', command=button_clicked)
button.pack()


# Entry 
input_info = Entry(width=10)
input_info.pack()

    

window.mainloop()