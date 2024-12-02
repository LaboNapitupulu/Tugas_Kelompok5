import tkinter as tk
import requests
import random

def show_random_quote(frame, label=None):
    """Menampilkan kutipan acak dari GitHub"""
    url = "https://raw.githubusercontent.com/LaboNapitupulu/File/main/quotes.txt"  # Ganti dengan URL raw file yang benar
    try:
        # Mengambil file dari GitHub
        response = requests.get(url)
        response.raise_for_status()  # Memastikan file berhasil diambil

        quotes = response.text.splitlines()  # Membaca semua baris
        random_quote = random.choice(quotes).strip()  # Memilih kutipan acak
    except requests.exceptions.RequestException as e:
        random_quote = f"Terjadi kesalahan saat mengambil file: {e}"

    # Jika label sudah ada, hanya update teks
    if label:
        label.config(text=random_quote)
    else:
        # Jika label belum ada, buat label baru dan tampilkan
        label = tk.Label(frame, text=random_quote, font=("Arial", 18), wraplength=500)
        label.pack(pady=50)

    # Tombol untuk menampilkan kutipan selanjutnya hanya dibuat sekali
    if not hasattr(show_random_quote, 'next_button'):  # Cek apakah tombol sudah ada
        show_random_quote.next_button = tk.Button(frame, text="Kutipan Selanjutnya", font=("Arial", 14),
                                                   command=lambda: show_random_quote(frame, label))  # Menampilkan kutipan baru
        show_random_quote.next_button.pack(pady=10)


def create_window():
    window = tk.Tk()
    window.title("Toolkit Produktivitas")
    window.geometry("600x600")

    frame = tk.Frame(window)
    frame.pack(fill="both", expand=True)

    show_random_quote(frame)  # Tampilkan kutipan pertama

    window.mainloop()

if __name__ == "__main__":
    create_window()
