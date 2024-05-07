import tkinter as tk
import math
from math import sqrt

class AdvancedCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Advanced Calculator")

        self.display = tk.Entry(master, width=30, font=("Arial", 14))
        self.display.grid(row=0, column=0, columnspan=5)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('C', 1, 4),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('(', 2, 4),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), (')', 3, 4),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3), ('√', 4, 4),
            ('^', 5, 0), ('π', 5, 1), ('sin', 5, 2), ('cos', 5, 3), ('tan', 5, 4)
        ]

        for (text, row, col) in buttons:
            btn = tk.Button(master, text=text, width=5, height=2, command=lambda t=text: self.on_button_click(t))
            btn.grid(row=row, column=col)

    def on_button_click(self, value):
        if value == '=':
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")

        elif value == 'C':
            self.display.delete(0, tk.END)

        elif value == '√':
            try:
                result = math.sqrt(eval(self.display.get()))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")

        elif value == '^':
            self.display.insert(tk.END, '**')

        elif value == 'π':
            self.display.insert(tk.END, math.pi)

        elif value == 'sin':
            try:
                result = math.sin(math.radians(eval(self.display.get())))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")

        elif value == 'cos':
            try:
                result = math.cos(math.radians(eval(self.display.get())))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")

        elif value == 'tan':
            try:
                result = math.tan(math.radians(eval(self.display.get())))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")

        else:
            self.display.insert(tk.END, value)

def main():
    root = tk.Tk()
    app = AdvancedCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
