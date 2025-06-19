def tampilkan_header():
    print("=" * 50)
    print(" SISTEM DIAGNOSA PENYAKIT BALITA ".center(50))
    print("     Menggunakan Forward Chaining     ".center(50))
    print("=" * 50)
    print("Jawab pertanyaan berikut dengan: ya / tidak\n")

# Basis aturan (IF ... THEN ...)
rules = {
    "flu": {"demam", "batuk", "pilek"},
    "diare": {"muntah", "feses_cair", "lemas"},
    "campak": {"demam", "ruam", "mata_merah"},
    "radang_tenggorokan": {"sakit_tenggorokan", "demam", "tidak_nafsu_makan"},
    "infeksi_telinga": {"telinga_nyeri", "demam", "rewel"},
}

# Daftar semua gejala unik dari semua rule
gejala_semua = sorted({gejala for g_set in rules.values() for gejala in g_set})

# Simpan jawaban user
fakta_user = set()

def tanya_user():
    for gejala in gejala_semua:
        jawaban = input(f"Apakah balita mengalami {gejala.replace('_', ' ')}? ").strip().lower()
        if jawaban == "ya":
            fakta_user.add(gejala)

def diagnosa():
    hasil = []
    for penyakit, gejala_penyakit in rules.items():
        if gejala_penyakit.issubset(fakta_user):
            hasil.append(penyakit)
    return hasil

def tampilkan_hasil(hasil):
    print("\n" + "=" * 50)
    if hasil:
        print("Diagnosis berdasarkan gejala yang terdeteksi:\n")
        for penyakit in hasil:
            print(f"➡️  {penyakit.replace('_', ' ').title()}")
    else:
        print("❌ Maaf, tidak ada penyakit yang teridentifikasi dari gejala tersebut.")
    print("=" * 50)

def main():
    tampilkan_header()
    tanya_user()
    hasil = diagnosa()
    tampilkan_hasil(hasil)

if __name__ == "__main__":
    main()
