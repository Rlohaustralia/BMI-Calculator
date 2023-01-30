# Question 2: It is not About Fat


from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("BMI Caculator")


# Definig functions

def compute_bmi():
    height = float(txtFirst.get())
    weight = float(txtSecond.get())
    bmi = weight / (height ** 2)
    bmi = round(bmi,4)
    messagebox.showinfo('BMI result',bmi)


# Adding labels

FirstEnterLabel = Label(window, text="Enter your height in m: ")
FirstEnterLabel.grid(row=0, column=0)

SecondEnterLabel = Label(window, text="Enter your weight in kg: ")
SecondEnterLabel.grid(row=1, column=0)


# Adding entry

txtFirst = StringVar()
entFirst = Entry(window, width = 15, textvariable = txtFirst)
entFirst.grid(row=0, column=1)

txtSecond = StringVar()
entSecond = Entry(window, width = 15, textvariable = txtSecond)
entSecond.grid(row=1, column=1)


# Adding button

btnCompute = Button(window, text='Compute BMI', width=10, command=compute_bmi)
btnCompute.grid(row=2, column=0, columnspan=2, padx=5, pady=(0,10))


window.mainloop()
