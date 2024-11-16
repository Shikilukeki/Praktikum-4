# Praktikum-4

Nama : Rifqi Maulana

NIM : 312410529

Kelas : TI.24.A.5

# Penjelasan program sederhana tabel data mahasiswa

## FLowchart program :

![Image](https://github.com/Shikilukeki/Foto/blob/main/Flowchart%20Tabel%20data%20mahasiswa.png?raw=true)

## Penjelasan :

```python
def hitung_nilai_akhir(nilai_tugas, nilai_uts, nilai_uas):
    return (0.3 * nilai_tugas) + (0.35 * nilai_uts) + (0.35 * nilai_uas)
```
Fungsi ```hitung_nilai_akhir``` pada program untuk menghitung nilai akhir berdasarkan nilai tugas, uts, dan uas. Dengan masing-masing persentase 30% untuk tugas, dan masing-masing 35% untuk nilai UTS dan UAS

```python
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
```

Sebuah perulangan untuk memasukan data mahasiswa mulai dari nama, nim, nilai tugas, nilai UTS, dan nilai UAS. akan terus melakukan loop / memasukan data mahasiswa, hingga pengguna memilih t (tidak) untuk berhenti memasukan data

```python
print("\nDaftar Data Mahasiswa:")
print("==========================================================================================")
print("| No | Nama                      | NIM       | Tugas | UTS   | UAS   | Akhir             |")
print("==========================================================================================")

for i, mahasiswa in enumerate(data_mahasiswa, start=1):
    print(f"| {i:>2} | {mahasiswa['nama']:<25} | {mahasiswa['nim']:<9} | {mahasiswa['nilai_tugas']:<5} | {mahasiswa['nilai_uts']:<5} | {mahasiswa['nilai_uas']:<5} | {mahasiswa['nilai_akhir']:<17.2f} |")
    print("==========================================================================================")
```

Mencetak data dari mahasiswa yang tadi diinputkan kedalam sebuah tabel yang berisikan data nama, nim, dan nilai dari mahasiswa

## Contoh hasil eksekusi program :

![Image](https://github.com/Shikilukeki/Foto/blob/main/Tabel%20data%20nilai%20mahasiswa.png?raw=true)
