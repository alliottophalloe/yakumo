# yakumo
Proyek ini secara otomatis memperbarui daftar proxy setiap 10 menit. Proxy yang diperiksa meliputi HTTP(S), SOCKS4, dan SOCKS5 dengan hasil global maupun spesifik negara.

## Fitur
- **Pembaharuan Otomatis**: Daftar proxy diperbarui setiap 10 menit.
- **Pengecekan Validitas Proxy**: Hanya proxy yang valid dan aktif yang disimpan.
- **Pengambilan Proxy dari Berbagai Sumber**: Mengambil proxy dari beberapa situs terpercaya.
- **Penyimpanan Hasil dalam JSON**: Proxy yang valid disimpan dalam format JSON.

## Instalasi
1. Pastikan Python 3.x terpasang di sistem Anda.
2. Install dependencies dengan `pip install -r requirements.txt`.
3. Jalankan program dengan `python src/main.py`.

## Penggunaan
Proxy akan diperbarui dan disimpan dalam file `data/proxies.json` setiap 10 menit.
