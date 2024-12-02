import tkinter as tk
from utils import clear_frame  # Mengimpor clear_frame dari utils.py

def press(button_text, entry):
    """Menambahkan teks tombol ke entry"""
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + str(button_text))

def calculate(entry):
    """Menghitung ekspresi matematika"""
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear(entry):
    """Menghapus semua input"""
    entry.delete(0, tk.END)

def show_calculator(window, frame):
    """Menampilkan fitur Kalkulator Sederhana"""
    clear_frame(frame)  # Memanggil fungsi clear_frame
    label = tk.Label(frame, text="Kalkulator Sederhana", font=("Arial", 20))
    label.pack(pady=20)

    entry = tk.Entry(frame, font=("Arial", 18), justify="right", bd=10)
    entry.pack(pady=10, fill="both", expand=True)

    button_frame = tk.Frame(frame)
    button_frame.pack()

    buttons = [
        ("7", 7), ("8", 8), ("9", 9), ("/", "/"),
        ("4", 4), ("5", 5), ("6", 6), ("", ""),
        ("1", 1), ("2", 2), ("3", 3), ("-", "-"),
        ("0", 0), ("C", "C"), ("=", "="), ("+", "+")
    ]

    for row in range(4):
        for col in range(4):
            button_text, value = buttons[row * 4 + col]
            if button_text == "C":
                button = tk.Button(button_frame, text=button_text, font=("Arial", 14), command=lambda: clear(entry))
            elif button_text == "=":
                button = tk.Button(button_frame, text=button_text, font=("Arial", 14), command=lambda: calculate(entry))
            else:
                button = tk.Button(button_frame, text=button_text, font=("Arial", 14), command=lambda v=value: press(v, entry))
            button.grid(row=row, column=col, ipadx=20, ipady=20, padx=5, pady=5, sticky="nsew")

     # Membuat tombol untuk menyesuaikan ukuran kolom dan baris
    for i in range(4):
        button_frame.grid_columnconfigure(i, weight=1)
        button_frame.grid_rowconfigure(i,weight=1)
