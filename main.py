import tkinter as tk

def evaluate_expression():
    try:
        expression = entry.get()
        result = str(eval(expression))
        result_label.config(text="Result: " + result)
    except Exception as e:
        result_label.config(text="Error")

# Creat a tkinter window
window = tk.Tk()
window.title("Simple Calculator")

entry = tk.Entry(window, width=20)
entry.grid(row=0, column=0, columnspan=4)


buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == '=':
        tk.Button(window, text=button, padx=20, pady=20, command=evaluate_expression).grid(row=row_val, column=col_val)
    elif button == 'C':
        tk.Button(window, text=button, padx=20, pady=20, command=lambda b=button: entry.delete(0, tk.END)).grid(row=row_val, column=col_val)
    else:
        tk.Button(window, text=button, padx=20, pady=20, command=lambda b=button: entry.insert(tk.END, b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1


result_label = tk.Label(window, text="")
result_label.grid(row=row_val, column=0, columnspan=4)


window.mainloop()
