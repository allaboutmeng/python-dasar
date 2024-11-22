import tkinter as tk  # Import Tkinter module tkinter
from tkinter import ttk  # Import ttk() widget
from tkinter.messagebox import showinfo

# Init
window = tk.Tk()  # Membuat object window berisi window Tk()
window.configure(bg="white")  # Mengubah background window menjadi putih
window.geometry("300x200")  # Mengubah size window dalam satuan pixel
window.resizable(False, False)  # Window x,y tidak bisa diresize
window.title("Sapa")  # Mengubah title window

# Variable
NAMA_DEPAN = tk.StringVar()  # Membuat constant
NAMA_BELAKANG = tk.StringVar()  # Membuat constant

# Fungsi
def tombol_click():
    pesan = f"Hello {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}, Have nice day"
    showinfo(title="Hi", message=pesan)

# Frame input
input_frame = ttk.Frame(window)  # Menggunakan widget ttk untuk memakai frame yang akan berisi window
input_frame.pack(padx=10, pady=10, fill="x", expand=True)  # Membuat layout dengan pack

# Komponen
# 1. Label nama depan
nama_depan_label = ttk.Label(input_frame, text="Nama Depan:")  # Label text Aisha pada frame input
nama_depan_label.pack(padx=10, fill="x", expand=True)  # Membuat pack layout untuk label

# 2. Entry nama depan
nama_depan_entry = ttk.Entry(input_frame, textvariable=NAMA_DEPAN)  # Entry akan masuk ke constant NAMA_DEPAN
nama_depan_entry.pack(padx=10, fill="x", expand=True)

# 3. Label nama belakang
nama_belakang_label = ttk.Label(input_frame, text="Nama Belakang:")  # Label text Aisha pada frame input
nama_belakang_label.pack(padx=10, fill="x", expand=True)  # Membuat pack Layout untuk Label

# 4. Entry nama belakang
nama_belakang_entry = ttk.Entry(input_frame, textvariable=NAMA_BELAKANG)  # Entry akan masuk ke constant NAMA_BELAKANG
nama_belakang_entry.pack(padx=10, fill="x", expand=True)

# 5. Tombol
tombol = ttk.Button(input_frame, text="Sapa!", command=tombol_click)  # Tombol untuk memanggil fungsi tombol_click
tombol.pack(fill='x', expand=True, padx=10, pady=10)

# Mainloop
window.mainloop()  # Menjalankan program hingga aplikasi close