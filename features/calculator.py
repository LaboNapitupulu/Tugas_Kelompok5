import tkinter as tk

def press(value, entry):
    """Menambahkan angka atau operator ke dalam input kalkulator"""
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + str(value))

def clear(entry):
    """Menghapus input kalkulator"""
    entry.delete(0, tk.END)

def calculate(entry):
    """Menghitung hasil dari input"""
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def backspace(entry):
    """Menghapus karakter terakhir dari input kalkulator"""
    current_text = entry.get()
    entry.delete(len(current_text) - 1, tk.END)

def show_calculator(window, frame):
    """Menampilkan aplikasi kalkulator"""
    from utils import clear_frame 

    # Menghapus frame sebelumnya
    clear_frame(frame)

    # Menampilkan Kalkulator
    label = tk.Label(frame, text="Kalkulator", font=("Arial", 18))
    label.pack(pady=10)

    entry = tk.Entry(frame, font=("Arial", 18), width=20, borderwidth=2, relief="solid")
    entry.pack(pady=10)

    button_frame = tk.Frame(frame)
    button_frame.pack()

    buttons = [
        ('7', '8', '9', '/'),
        ('4', '5', '6', '*'),
        ('1', '2', '3', '-'),
        ('0', '.', '=', '+')
    ]

    for row in buttons:
        button_row = tk.Frame(button_frame)
        button_row.pack()

        for button_text in row:
            button = tk.Button(button_row, text=button_text, font=("Arial", 14),
                               command=lambda v=button_text: press(v, entry) if v != "=" else calculate(entry))
            button.pack(side="left", padx=5)

    # Tombol clear
    clear_button = tk.Button(frame, text="Clear", font=("Arial", 14), command=lambda: clear(entry))
    clear_button.pack(pady=5)

    # Tombol backspace
    backspace_button = tk.Button(frame, text="←", font=("Arial", 14), command=lambda: backspace(entry))
    backspace_button.pack(pady=5)


