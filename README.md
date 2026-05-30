# membuat-lampu-sirine

# Dual-LED Smart Siren System with ESP32

Proyek ini adalah simulasi sistem sirine pintar berbasis IoT menggunakan **ESP32** dan **MicroPython**
## Fitur Utama
- **Sinkronisasi Dinamis:** Tingkat kecerahan kedua LED berkedip seirama (fading) dengan frekuensi ketukan (*bip*) buzzer.
- **Penskalaan Otomatis (Auto-Scaling):** Menggunakan rumus matematika untuk mengonversi nilai kecerahan LED ($0$ s.d $1023$) menjadi jeda waktu suara secara *real-time*.
- **Clean & Efficient Code:** Struktur kode menerapkan prinsip **DRY (Don't Repeat Yourself)** dengan mereduksi fungsionalitas ke dalam fungsi tunggal guna menghemat memori RAM pada mikrokontroler.

## Komponen Sirkuit (Hardware)
Sistem ini menggunakan komponen-komponen berikut yang dikonfigurasi pada platform simulasi Wokwi:
- **ESP32 DevKit V1** (Mikrokontroler Utama)
- ** Terhubung ke **GPIO 13** dan **GPIO 14**
- ** Terhubung ke **GPIO 12**

## Alur Logika Sistem
1. **Loop Naik :** LED secara bertahap berubah dari redup ke sangat terang. Seiring lampu menguat, ketukan buzzer otomatis berbunyi semakin cepat (efek alarm mendekat).
2. **Loop Turun :** LED secara bertahap meredup kembali ke posisi mati. Seiring lampu melemah, ketukan buzzer melambat secara konstan.
