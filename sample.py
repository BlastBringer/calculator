import tkinter as tk

def parse_and_calculate(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"Error: {e}"

def on_calculate():
    expression = entry1.get()
    result = parse_and_calculate(expression)
    result_label.config(text=f"Result: {result}")

def on_number_click(number):
    current_text = entry1.get()
    entry1.delete(0, tk.END)
    entry1.insert(0, current_text + str(number))

def on_operator_click(operator):
    current_text = entry1.get()
    entry1.delete(0, tk.END)
    entry1.insert(0, current_text + operator)

r = tk.Tk()
r.title('Calculator App!')

entry1 = tk.Entry(r, font=("Helvetica", 16))
entry1.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
    ('0', 4, 1)
]

for (text, row, col) in buttons:
    button = tk.Button(r, text=text, width=10, height=3, command=lambda t=text: on_number_click(t), font=("Helvetica", 16))
    button.grid(row=row, column=col)

operators = [
    ('+', 1, 3), ('-', 2, 3), ('*', 3, 3), ('/', 4, 3)
]

for (text, row, col) in operators:
    button = tk.Button(r, text=text, width=10, height=3, command=lambda t=text: on_operator_click(t), font=("Helvetica", 16))
    button.grid(row=row, column=col)

button_calculate = tk.Button(r, text="=", width=10, height=3, command=on_calculate, font=("Helvetica", 16))
button_calculate.grid(row=4, column=2)

result_label = tk.Label(r, text="Result: ", font=("Helvetica", 16))
result_label.grid(row=5, column=0, columnspan=4)

r.mainloop()
