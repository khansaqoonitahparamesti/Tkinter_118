import  tkinter as tk
from tkinter import messagebox

def prediksi ():
    try:
        for entry in entries: # loop untuk memeriksa setiap entry
            nilai = int (entry.get())#mengambil nilai dari masing masing inputdan dikonversi ke integer
            if not (0<=nilai<=100):# mengecek nilai apakah dalam range0-100
                raise ValueError ("nilai harus antara 0 dan 100")# jika tidak,raise error
        hasil_label.config(text="prediksi prodi: Teknologi Informasi")# menampilkan hasil presiksi sesuai dengan yang diminta
    except ValueError as ve: # Jika ada error ValueError (misal input tidak valid)
        messagebox.showerror("input error","pastikan semua input adalah angka antara 0 dan 100.") # Menampilkan Pesan Error

root = tk.Tk()#Membuat jendela utama
root.title("Aplikasi Prediksi Prodi Pilihan")# memeberikan judul di jendal utama
root.geometry("500x600")#untuk mengatur ukuran jendelanya
root.configure (bg="#87CEEB") # menubah warna latar belakang menggunakan kode tertentu

judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("times", 16,"bold roman"))# membuat elemen tampilan  labelapakah gambar text
judul_label.pack(pady=20)# untuk mengatur tataletak dan menempatkan label jendela

frame_input = tk.Frame(root, bg="#f0f0f0")# mengubah warna latar belakang menggunakan kode tertentu
frame_input.pack(pady=10)# untuk mengatur tataletak dan menempatkan label jendela
 # unutk mengatur tampilan isi jendelnya
entries = []
for i in range(10):
    label = tk.Label(frame_input, text=f"Nilai Mata Pelajaran{i+1}:", font=("times",12))
    label.grid(row=i, column=0, padx=10, pady=5, sticky="e")
    entry = tk.Entry(frame_input, width=10, font=("times", 12))
    entry.grid(row=i, column=1,padx=10, pady=5)
    entries.append(entry)
#
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=prediksi, font = ("times",12)) # membuat tombol prediksi untuk menjalan kan prediksi
prediksi_button.pack(pady=30)#mengatur jarak label

hasil_label = tk.Label(root, text="", font=("Arial", 12), fg = "blue")# menatur tampilan hasil prediksi
hasil_label.pack(pady=10)#mengatur jarak label
 #untuk memanggil loop tkinter
root.mainloop()