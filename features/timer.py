import tkinter as tk
import time
from utils import clear_frame 

remaining_time = 0  # Dalam detik
is_paused = False
is_running = False  # Menambahkan status timer

def update_timer(label, root):
    """Memperbarui tampilan timer setiap detik"""
    global remaining_time, is_paused, is_running
    while remaining_time > 0 and is_running:
        mins, secs = divmod(remaining_time, 60)
        label.config(text=f"{mins:02}:{secs:02}")
        root.update()  # Memperbarui window
        time.sleep(1)
        if is_paused:
            break  # Hentikan pembaruan jika timer dijeda
        remaining_time -= 1

    if remaining_time <= 0:
        label.config(text="Waktu Habis!")
        root.update()
        is_running = False  # Stop timer setelah selesai

def start_timer(entry_hours, entry_minutes, entry_seconds, label, root):
    """Memulai timer berdasarkan input jam, menit, detik"""
    global remaining_time, is_paused, is_running
    try:
        hours = int(entry_hours.get())
        minutes = int(entry_minutes.get())
        seconds = int(entry_seconds.get())
        remaining_time = (hours * 3600) + (minutes * 60) + seconds  # Total detik
        is_paused = False
        is_running = True  # Menandakan timer sedang berjalan
        update_timer(label, root)  # Mulai menghitung mundur
    except ValueError:
        label.config(text="Masukkan durasi yang valid")

def pause_timer():
    """Menjeda timer"""
    global is_paused
    is_paused = True

def resume_timer(label, root):
    """Melanjutkan timer yang dijeda"""
    global is_paused, is_running
    is_paused = False
    is_running = True
    update_timer(label, root)  # Melanjutkan timer yang sudah dijeda

def reset_timer(label):
    """Mengatur ulang timer ke kondisi awal"""
    global remaining_time, is_paused, is_running
    remaining_time = 0
    is_paused = False
    is_running = False
    label.config(text="00:00")  # Reset label timer ke 00:00

def show_timer(root, frame):
    """Menampilkan fitur Timer Belajar"""
    clear_frame(frame)  
    label = tk.Label(frame, text="Timer Belajar", font=("Arial", 20))
    label.pack(pady=20)

    global timer_label
    timer_label = tk.Label(frame, text="00:00", font=("Arial", 50), fg="red")
    timer_label.pack(pady=10)

    # Input untuk jam, menit, dan detik
    entry_hours = tk.Entry(frame, font=("Arial", 14), width=5)
    entry_hours.insert(0, "0")
    entry_hours.pack(side=tk.LEFT, padx=5)

    entry_minutes = tk.Entry(frame, font=("Arial", 14), width=5)
    entry_minutes.insert(0, "0")
    entry_minutes.pack(side=tk.LEFT, padx=5)

    entry_seconds = tk.Entry(frame, font=("Arial", 14), width=5)
    entry_seconds.insert(0, "0")
    entry_seconds.pack(side=tk.LEFT, padx=5)

    # Tombol untuk mulai, pause, resume, dan reset
    start_button = tk.Button(frame, text="Mulai", font=("Arial", 14), command=lambda: start_timer(entry_hours, entry_minutes, entry_seconds, timer_label, root))
    start_button.pack(side=tk.LEFT, padx=5, pady=10)

    pause_button = tk.Button(frame, text="Pause", font=("Arial", 14), command=pause_timer)
    pause_button.pack(side=tk.LEFT, padx=5, pady=10)

    resume_button = tk.Button(frame, text="Resume", font=("Arial", 14), command=lambda: resume_timer(timer_label, root))
    resume_button.pack(side=tk.LEFT, padx=5, pady=10)

    reset_button = tk.Button(frame, text="Reset", font=("Arial", 14), command=lambda: reset_timer(timer_label))
    reset_button.pack(side=tk.LEFT, padx=5, pady=10)
