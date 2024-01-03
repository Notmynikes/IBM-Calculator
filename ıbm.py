import tkinter
from tkinter import messagebox

window = tkinter.Tk()
window.title("IBM Calculator")
window.config(padx=20, pady=20)
window.minsize(width=500, height=500)

def calculate_ibm():
    height=input_height.get()
    weight=input_weight.get()

    if height=="" or weight=="":
        result_label.config(text="Enter your height and weight")
    else:
        try:
            bmi=float(weight)/(float(height)/100)**2
            result_string=write_result(bmi)
            result_label.config(text=result_string)
        except:
            result_label.config(text="Enter a valid number")


input_label_1=tkinter.Label(text="Height")
input_label_1.pack()

input_height=tkinter.Entry(width=10)
input_height.pack()

input_label_2=tkinter.Label(text="Weight")
input_label_2.pack()

input_weight=tkinter.Entry(width=10)
input_weight.pack()

calculate_button=tkinter.Button(text="Calculate",command=calculate_ibm)
calculate_button.pack()

result_label=tkinter.Label(text="result")
result_label.pack()

def write_result(bmi):
    result_string=f"Your Bmi is {round(bmi,2)}.You are "
    if bmi<16:
        result_string +="severely thin"
    elif bmi >16 and bmi<=17:
        result_string +="moderately thin"
    elif bmi>17 and bmi<=18.5:
        result_string +="mild thin"
    elif bmi>18.5 and bmi<=25:
        result_string +="normal"
    elif bmi>25 and bmi<=30:
        result_string +="overweight"
    elif bmi>30 and bmi<=35:
        result_string +="obese class 1"
    elif bmi>35 and bmi<=40:
        result_string +="obese class 2"
    else:
        result_string +="obese class 3"
    return result_string



window.mainloop()