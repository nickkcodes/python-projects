import tkinter as tk

window = tk.Tk()
window.title('Calculator ni Nick')
window.geometry('600x700')
window.configure(bg='black')

for i in range(4):
    window.columnconfigure(i, weight=1)
for i in range(6):
    window.rowconfigure(i, weight=1)

display = tk.Entry(window, width=20, font=('Arial', 28), bg='black', fg='white', insertbackground='white', bd=0)
display.grid(row=0, column=0, columnspan=4, pady=10, padx=10, sticky='nsew')

def click(value):
    if value == '=':
        try:
            result = eval(display.get())
            display.delete(0, tk.END)
            display.insert(0, str(result)) 
        except:
            display.delete(0, tk.END)
            display.insert(0, 'Error')
    elif value == 'AC':
        display.delete(0, tk.END)
    elif value == 'D':
        current = display.get()
        display.delete(0, tk.END)
        display.insert(0, current[:-1])
    else:
        display.insert(tk.END, value)

buttons = [
    'AC', 'D', '%', '/',
    '7', '8', '9', '*',
    '4', '5', '6', '-',
    '1', '2', '3', '+',
    'e', '0', '.', '='
]

operators = ['/', '*', '-', '+', '=', '%', 'AC', 'D']

row = 1
col = 0
for btn in buttons:
    if btn in operators:
        bg_color = 'orange'
        fg_color = 'black'
    else:
        bg_color = '#222222'
        fg_color = 'white'

    tk.Button(window, text=btn, font=('Arial', 18),
              bg=bg_color, fg=fg_color,
              activebackground='orange', activeforeground='black',
              bd=0, command=lambda b=btn: click(b)).grid(row=row, column=col, sticky='nsew', padx=2, pady=2)
    col += 1
    if col > 3:
        col = 0
        row += 1

window.mainloop()