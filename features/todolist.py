import tkinter as tk
from utils import clear_frame 

def add_task(task_listbox, entry):
    """Menambahkan tugas ke daftar"""
    task = entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
    entry.delete(0, tk.END)

def mark_task_done(task_listbox):
    """Menandai tugas sebagai selesai (garis tengah)"""
    selected = task_listbox.curselection()
    if selected:
        task = task_listbox.get(selected)
        task_listbox.delete(selected)
        task_listbox.insert(tk.END, f"✔ {task}")

def delete_all_tasks(task_listbox):
    """Menghapus semua tugas dari daftar"""
    task_listbox.delete(0, tk.END)

def show_todolist(window, frame):
    """Menampilkan fitur Daftar Tugas"""
    clear_frame(frame)  # Memanggil fungsi clear_frame
    label = tk.Label(frame, text="Daftar Tugas", font=("Arial", 20))
    label.pack(pady=20)

    task_listbox = tk.Listbox(frame, height=10, width=50, font=("Arial", 14))
    task_listbox.pack(pady=10)

    entry = tk.Entry(frame, font=("Arial", 14))
    entry.pack(pady=5)

    add_button = tk.Button(frame, text="Tambah Tugas", font=("Arial", 14), command=lambda: add_task(task_listbox, entry))
    add_button.pack(pady=5)

    done_button = tk.Button(frame, text="Tandai Selesai", font=("Arial", 14), command=lambda: mark_task_done(task_listbox))
    done_button.pack(pady=5)

    delete_all_button = tk.Button(frame, text="Hapus Semua", font=("Arial", 14), command=lambda: delete_all_tasks(task_listbox))
    delete_all_button.pack(pady=5)
