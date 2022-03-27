class Translation(object):
    START_TEXT = """Selamat Datang di Api Scrapping Bot!
Terima Kasih Telah Menggunakan Saya
Masukkan Nomor Telepon Telegram Anda, untuk mendapatkan APP ID Dan API HASH dari my.telegram.org

/start pada tahap apa pun untuk memasukkan kembali detail Anda""""""
    AFTER_RECVD_CODE_TEXT = """I see!
sekarang silakan kirim kode Telegram yang Anda terima dari Telegram!
kode ini hanya digunakan untuk tujuan mendapatkan API ID Dan API HASH dari my.telegram.org
jika Anda tidak mempercayai pengembang bot ini, bisa isi sendiri di my.telegram.org

/start pada tahap apa pun untuk memasukkan kembali detail Anda"""

    BEFORE_SUCC_LOGIN = "recieved code. Scarpping web page ..."

    ERRED_PAGE = "Gagal mendapatkan id aplikasi. \n\n@GojoProject"

    CANCELLED_MESG = "Selamat tinggal! Silahkan ulang /start percakapan baru"

    IN_VALID_CODE_PVDED = "Maaf, kode Telegram Web-Login yang valid"
    IN_VALID_PHNO_PVDED = "Maaf, sepertinya bukan telepon yang valid"
