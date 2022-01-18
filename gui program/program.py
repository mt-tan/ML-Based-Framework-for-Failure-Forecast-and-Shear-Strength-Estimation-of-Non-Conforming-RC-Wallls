from tkinter import *
import pickle
from PIL import ImageTk, Image
import numpy as np

window = Tk(screenName="Failure mode and Shear Strength Estimation of RC Shear Walls")
window.title("Failure mode and Shear Strength Estimation of RC Shear Walls")


window.geometry("650x710")
window.resizable(False, False)
t1 = Label(window, text=f"Wall Length - l\N{LATIN SUBSCRIPT W}", font='SegoeUI 10 bold', anchor="w", justify="left", width=52)
t1.grid(row=0, column=0)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value, width=15, borderwidth=2, font='SegoeUI 10 bold', selectbackground="yellow", selectforeground="black")
e1.insert(0, "1000")
e1.grid(row=0, column=1)

t2 = Label(window, text="Wall Web Thickness - tw (mm):", font='SegoeUI 10 bold', anchor="w", justify="left", width=52)
t2.grid(row=1, column=0)

e2_value = StringVar()
e2 = Entry(window, textvariable=e2_value, width=15, borderwidth=2, font='SegoeUI 10 bold', selectbackground="yellow", selectforeground="black")
e2.insert(0, "100")
e2.grid(row=1, column=1)

t3 = Label(window, text="Wall Height - hw (mm):", font='SegoeUI 10 bold', anchor="w", justify="left", width=52)
t3.grid(row=2, column=0)

e3_value = StringVar()
e3 = Entry(window, textvariable=e3_value, width=15, borderwidth=2, font='SegoeUI 10 bold', selectbackground="yellow", selectforeground="black")
e3.insert(0, "1000")
e3.grid(row=2, column=1)

t4 = Label(window, text="Total Boundary Area - Agb (mm\u00b2):", font='SegoeUI 10 bold', anchor="w", justify="left", width=52)
t4.grid(row=3, column=0)

e4_value = StringVar()
e4 = Entry(window, textvariable=e4_value, width=15, borderwidth=2, font='SegoeUI 10 bold', selectbackground="yellow", selectforeground="black")
e4.insert(0, "10322.56")
e4.grid(row=3, column=1)

t6 = Label(window, text="Concrete Compressive Strength - fc (MPa):", font='SegoeUI 10 bold', anchor="w", justify="left", width=52)
t6.grid(row=4, column=0)

e6_value = StringVar()
e6 = Entry(window, textvariable=e6_value, width=15, borderwidth=2, font='SegoeUI 10 bold', selectbackground="yellow", selectforeground="black")
e6.insert(0, "46.2")
e6.grid(row=4, column=1)

t7 = Label(window, text="Axial Load Ratio - P/Agfc:", font='SegoeUI 10 bold', anchor="w", justify="left", width=52)
t7.grid(row=5, column=0)

e7_value = StringVar()
e7 = Entry(window, textvariable=e7_value, width=15, borderwidth=2, font='SegoeUI 10 bold', selectbackground="yellow", selectforeground="black")
e7.insert(0, "0")
e7.grid(row=5, column=1)

t8 = Label(window, text="Shear Span Ratio - M/Vlw:", font='SegoeUI 10 bold', anchor="w", justify="left", width=52)
t8.grid(row=6, column=0)

e8_value = StringVar()
e8 = Entry(window, textvariable=e8_value, width=15, borderwidth=2, font='SegoeUI 10 bold', selectbackground="yellow", selectforeground="black")
e8.insert(0, "1.2")
e8.grid(row=6, column=1)

t9 = Label(window, text="Web Longitudinal Reinforcement Ratio - ρl:", font='SegoeUI 10 bold', anchor="w", justify="left", width=52)
t9.grid(row=7, column=0)

e9_value = StringVar()
e9 = Entry(window, textvariable=e9_value, width=15, borderwidth=2, font='SegoeUI 10 bold', selectbackground="yellow", selectforeground="black")
e9.insert(0, "0.0125")
e9.grid(row=7, column=1)

t10 = Label(window, text="Web Longitudinal Reinforcement Yield Strength - fyl (MPa):", font='SegoeUI 10 bold', anchor="w", justify="left", width=52)
t10.grid(row=8, column=0)

e10_value = StringVar()
e10 = Entry(window, textvariable=e10_value, width=15, borderwidth=2, font='SegoeUI 10 bold', selectbackground="yellow", selectforeground="black")
e10.insert(0, "420")
e10.grid(row=8, column=1)

t11 = Label(window, text="Web Transverse Reinforcement Ratio - ρt:", font='SegoeUI 10 bold', anchor="w", justify="left", width=52)
t11.grid(row=9, column=0)

e11_value = StringVar()
e11 = Entry(window, textvariable=e11_value, width=15, borderwidth=2, font='SegoeUI 10 bold', selectbackground="yellow", selectforeground="black")
e11.insert(0, "0.0125")
e11.grid(row=9, column=1)

t12 = Label(window, text="Web Transverse Reinforcement Yield Strength - fyt (MPa):", font='SegoeUI 10 bold', anchor="w", justify="left", width=52)
t12.grid(row=10, column=0)

e12_value = StringVar()
e12 = Entry(window, textvariable=e12_value, width=15, borderwidth=2, font='SegoeUI 10 bold', selectbackground="yellow", selectforeground="black")
e12.insert(0, "420")
e12.grid(row=10, column=1)

t13 = Label(window, text="Boundary Longitudinal Reinforcement Ratio - ρbl:", font='SegoeUI 10 bold', anchor="w", justify="left", width=52)
t13.grid(row=11, column=0)

e13_value = StringVar()
e13 = Entry(window, textvariable=e13_value, width=15, borderwidth=2, font='SegoeUI 10 bold', selectbackground="yellow", selectforeground="black")
e13.insert(0, "0.1")
e13.grid(row=11, column=1)

t14 = Label(window, text="Boundary Longitudinal Reinforcement Yield Strength - fybl (MPa):", font='SegoeUI 10 bold', anchor="w", justify="left", width=52)
t14.grid(row=12, column=0)

e14_value = StringVar()
e14 = Entry(window, textvariable=e14_value, width=15, borderwidth=2, font='SegoeUI 10 bold', selectbackground="yellow", selectforeground="black")
e14.insert(0, "420")
e14.grid(row=12, column=1)

t15 = Label(window, text="Boundary Transverse Reinforcement Ratio - ρsh:", font='SegoeUI 10 bold', anchor="w", justify="left", width=52)
t15.grid(row=13, column=0)

e15_value = StringVar()
e15 = Entry(window, textvariable=e15_value, width=15, borderwidth=2, font='SegoeUI 10 bold', selectbackground="yellow", selectforeground="black")
e15.insert(0, "0.01")
e15.grid(row=13, column=1)

t16 = Label(window, text="Boundary Transverse Reinforcement Yield Strength - fyt (MPa):", font='SegoeUI 10 bold', anchor="w", justify="left", width=52)
t16.grid(row=14, column=0)

e16_value = StringVar()
e16 = Entry(window, textvariable=e16_value, width=15, borderwidth=2, font='SegoeUI 10 bold', selectbackground="yellow", selectforeground="black")
e16.insert(0, "420")
e16.grid(row=14, column=1)

img = ImageTk.PhotoImage(Image.open('example_section.png'))
labelimage = Label(window, image=img)
labelimage.place(x=25, y=400)


text = Text(window, height=3, width=30, font='SegoeUI 10 bold', selectbackground="yellow", selectforeground="black")
text.grid(row=15, column=1, columnspan=4)


def prediction():
    try:
        classifier = pickle.load(open('catb_classifier.sav', 'rb'))
        regressor = pickle.load(open('catb_regressor.sav', 'rb'))
        lw = float(e1_value.get())
        tw = float(e2_value.get())
        hw = float(e3_value.get())
        Agb = float(e4_value.get())
        fc = float(e6_value.get())
        axial_load_ratio = float(e7_value.get())
        shear_span_ratio = float(e8_value.get())
        web_long_rebars = float(e9_value.get()) * float(e10_value.get())
        web_trans_rebars = float(e11_value.get()) * float(e12_value.get())
        boundary_long_rebars = float(e13_value.get()) * float(e14_value.get())
        boundary_trans_rebars = float(e15_value.get()) * float(e16_value.get())
        array1 = np.array([tw, lw, hw, shear_span_ratio, axial_load_ratio, fc, Agb, boundary_long_rebars, boundary_trans_rebars, web_long_rebars, web_trans_rebars])
        failure_mode = classifier.predict([array1])
        array2 = np.array([tw, lw, hw, shear_span_ratio, axial_load_ratio, fc, Agb, boundary_long_rebars, boundary_trans_rebars, web_long_rebars, web_trans_rebars, failure_mode[0][0]])
        shear_strength = regressor.predict([array2])
        if failure_mode == 1:
            text.delete(1.0, END)
            text.insert(END, f"Failure Mode: Shear Failure\nShear Strength: {np.round(shear_strength[0], 2)} kN")
        elif failure_mode == 2:
            text.delete(1.0, END)
            text.insert(END, f"Failure Mode: Transition Failure\nShear Strength: {np.round(shear_strength[0], 2)} kN")
        elif failure_mode == 3:
            text.delete(1.0, END)
            text.insert(END, f"Failure Mode: Flexure Failure\nShear Strength: {np.round(shear_strength[0], 2)} kN")

    except ValueError:
        text.delete(1.0, END)
        text.insert(END, "Be sure to enter a number. Also do not use comma for decimals, use period for decimals instead.")


b1 = Button(window, text="Predict", height=3, width=40, command=lambda: prediction(), font='SegoeUI 11 bold')
b1.grid(row=15, column=0)


window.mainloop()
