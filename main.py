import tkinter as tk

from features.calculator import show_calculator
from features.todolist import show_todolist


def main():
    window = tk.Tk()
    window.title("Toolkit Produktivitas")
    window.geometry("600x600")  # Menyesuaikan ukuran jendela aplikasi

    frame = tk.Frame(window)
    frame.pack(fill="both", expand=True)

    # Membuat tombol navigasi yang lebih besar
    menu = tk.Menu(window)
    window.config(menu=menu)

    app_menu = tk.Menu(menu, tearoff=0)
    menu.add_cascade(label="Fitur", menu=app_menu)

    app_menu.add_command(label="Kalkulator", command=lambda: show_calculator(window, frame))
    app_menu.add_command(label="Daftar Tugas", command=lambda: show_todolist(window, frame))  # Perbaikan di sini, hanya frame

    window.mainloop()

if __name__ == "__main__":
    main()
