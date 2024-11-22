import PySimpleGUI as sg
from datetime import datetime

# Layout Program Kasir
def program_kasir():
    layout = [
        [sg.Text("Harga:"), sg.Input(key='-HARGA-', size=(20, 1))],
        [sg.Text("Kuantitas:"), sg.Input(key='-KUANTITAS-', size=(20, 1))],
        [sg.Button("Hitung Total"), sg.Button("Kembali")],
        [sg.Text("Total: "), sg.Text("Rp.0.00", key='-TOTAL-', size=(15, 1))]
    ]
    return sg.Window("Program Kasir", layout)

# Layout Program Parkir
def program_parkir():
    layout = [
        [sg.Text("No Plat Polisi:"), sg.Input(key='-NOPOL-', size=(20, 1)), sg.Button("Cari")],
        [sg.Text("Waktu Masuk (HH:MM):"), sg.Input(key='-MASUK-', size=(20, 1))],
        [sg.Text("Waktu Keluar (HH:MM):"), sg.Input(key='-KELUAR-', size=(20, 1))],
        [sg.Text("Biaya Per Jam: Rp. 2,000")],
        [sg.Button("Hitung"), sg.Button("Kembali"), sg.Text("Biaya: Rp.0", key='-BIAYA-', size=(15, 1))],
    ]
    return sg.Window("Aplikasi Parkir", layout)

# Layout Program Data Siswa
def program_data_siswa():
    layout = [
        [sg.Text("Nama Lengkap:"), sg.Input(key='-NAMA-', size=(30, 1))],
        [sg.Text("Tanggal Lahir:"), sg.Input(key='-TGL_LAHIR-', size=(30, 1))],
        [sg.Text("Asal Sekolah:"), sg.Input(key='-SEKOLAH-', size=(30, 1))],
        [sg.Text("NISN:"), sg.Input(key='-NISN-', size=(30, 1))],
        [sg.Text("Nama Ayah:"), sg.Input(key='-AYAH-', size=(30, 1))],
        [sg.Text("Nama Ibu:"), sg.Input(key='-IBU-', size=(30, 1))],
        [sg.Text("Nomor Telepon/HP:"), sg.Input(key='-HP-', size=(30, 1))],
        [sg.Text("Alamat:"), sg.Multiline(size=(40, 5), key='-ALAMAT-')],
        [sg.Button("Simpan"), sg.Button("Kembali")]
    ]
    return sg.Window("Data Siswa Baru", layout)

# Menu Utama
def menu_utama():
    layout = [
        [sg.Text("Pilih Program:", font=("Helvetica", 16))],
        [sg.Button("Program Kasir"), sg.Button("Program Parkir"), sg.Button("Program Data Siswa")],
        [sg.Button("Keluar")]
    ]
    return sg.Window("Menu Utama", layout)

# Logika Utama
window = menu_utama()

while True:
    event, values = window.read()

    if event in (sg.WINDOW_CLOSED, "Keluar"):
        break

    if event == "Program Kasir":
        window.close()
        window = program_kasir()
        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "Kembali"):
                break
            if event == "Hitung Total":
                try:
                    harga = float(values['-HARGA-'])
                    kuantitas = int(values['-KUANTITAS-'])
                    total = harga * kuantitas
                    window['-TOTAL-'].update(f"Rp.{total:,.2f}")
                except ValueError:
                    sg.popup("Masukkan angka yang valid!")
        window.close()
        window = menu_utama()

    elif event == "Program Parkir":
        window.close()
        window = program_parkir()
        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "Kembali"):
                break
            if event == "Hitung":
                try:
                    waktu_masuk = datetime.strptime(values['-MASUK-'], '%H:%M')
                    waktu_keluar = datetime.strptime(values['-KELUAR-'], '%H:%M')
                    durasi = (waktu_keluar - waktu_masuk).seconds // 3600
                    biaya = durasi * 2000
                    window['-BIAYA-'].update(f"Rp.{biaya}")
                except ValueError:
                    sg.popup("Masukkan waktu dalam format HH:MM!")
        window.close()
        window = menu_utama()

    elif event == "Program Data Siswa":
        window.close()
        window = program_data_siswa()
        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "Kembali"):
                break
            if event == "Simpan":
                data_siswa = "\n".join([f"{key}: {values[key]}" for key in values])
                sg.popup("Data Tersimpan!", data_siswa)
        window.close()
        window = menu_utama()

window.close()