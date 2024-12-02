import tkinter as tk
from utils import clear_frame 

def save_note(entry, label):
    """Menyimpan catatan ke file lokal"""
    with open("notes.txt", "w") as f:
        f.write(entry.get("1.0", tk.END))  # Menyimpan semua teks dari widget Text
    label.config(text="Catatan berhasil disimpan!")

def read_note(entry):
    """Membaca catatan yang disimpan dari file lokal"""
    try:
        with open("notes.txt", "r") as f:
            note = f.read()
            entry.delete("1.0", tk.END)  # Menghapus teks lama
            entry.insert(tk.END, note)  # Memasukkan teks dari file
    except FileNotFoundError:
        entry.delete("1.0", tk.END)
        entry.insert(tk.END, "Tidak ada catatan yang disimpan.")

def show_notes(root, frame):
    """Menampilkan fitur Catatan Harian"""
    clear_frame(frame)  # Memanggil fungsi clear_frame untuk membersihkan frame
    label = tk.Label(frame, text="Catatan Harian", font=("Arial", 20))
    label.pack(pady=20)

    note_entry = tk.Text(frame, height=10, width=40, font=("Arial", 14))
    note_entry.pack(pady=10)

    save_button = tk.Button(frame, text="Simpan Catatan", font=("Arial", 14), command=lambda: save_note(note_entry, label))
    save_button.pack(pady=10)

    read_button = tk.Button(frame, text="Baca Catatan", font=("Arial", 14), command=lambda: read_note(note_entry))
    read_button.pack(pady=10)
