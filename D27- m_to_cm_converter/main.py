from tkinter import *


def m_to_cm():
    m = m_input.get()
    cm = float(m)*100
    cm_result_label["text"] = str(cm)


window = Tk()
window.title("meter_to_centimeter_Converter")
window.config(padx=20, pady=20)

m_input = Entry(width=5)
m_input.grid(column=1, row=0)

m_label = Label(text="meter")
m_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

cm_result_label = Label(text="0")
cm_result_label.grid(column=1, row=1)

cm_label = Label(text="cm")
cm_label.grid(column=2, row=1)

convert_button = Button(text="Convert", command=m_to_cm)
convert_button.grid(column=1, row=2)

window.mainloop()
