import tkinter as tk

def clear_frame(frame):
    """Menghapus semua widget dari frame"""
    for widget in frame.winfo_children():
        widget.destroy()
