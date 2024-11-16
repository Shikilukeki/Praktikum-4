# Fungsi untuk menghitung nilai akhir
def hitung_nilai_akhir(nilai_tugas, nilai_uts, nilai_uas):
    return (0.3 * nilai_tugas) + (0.35 * nilai_uts) + (0.35 * nilai_uas)

# List untuk menyimpan data mahasiswa
data_mahasiswa = []

# Loop untuk memasukan dan menambah data
while True:
    nama = input("Masukkan nama: ")
    nim = input("Masukkan NIM: ")
    nilai_tugas = float(input("Masukkan nilai tugas: "))
    nilai_uts = float(input("Masukkan nilai UTS: "))
    nilai_uas = float(input("Masukkan nilai UAS: "))
    
    nilai_akhir = hitung_nilai_akhir(nilai_tugas, nilai_uts, nilai_uas)
    data_mahasiswa.append({
        "nama": nama,
        "nim": nim,
        "nilai_tugas": nilai_tugas,
        "nilai_uts": nilai_uts,
        "nilai_uas": nilai_uas,
        "nilai_akhir": nilai_akhir
    })
    
    tambah_data = input("Tambah data lagi? (y/t): ")
    if tambah_data.lower() == 't':
        break

# Menampilkan daftar data mahasiswa dalam bentuk tabel 
print("\nDaftar Data Mahasiswa:")
print("==========================================================================================")
print("| No | Nama                      | NIM       | Tugas | UTS   | UAS   | Akhir             |")
print("==========================================================================================")

for i, mahasiswa in enumerate(data_mahasiswa, start=1):
    print(f"| {i:>2} | {mahasiswa['nama']:<25} | {mahasiswa['nim']:<9} | {mahasiswa['nilai_tugas']:<5} | {mahasiswa['nilai_uts']:<5} | {mahasiswa['nilai_uas']:<5} | {mahasiswa['nilai_akhir']:<17.2f} |")
    print("==========================================================================================")
