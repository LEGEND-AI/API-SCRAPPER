class Translation(object):
    START_TEXT = """Salam, Ledy AP Scrapper Bot'a xoş gəldin!
my.telegram.org saytından APP-ID əldə etmək üçün Telegram Telefon Nömrənizi daxil edin.


/start yenidən başlamaq üçün basın"""
    AFTER_RECVD_CODE_TEXT = """yaxsı!
indi Telegramdan aldığınız Telegram kodunu göndərin!
**bu kod yalnız my.telegram.org saytından APP ID əldə etmək üçün istifadə olunur!**

/start yenidən başlatmaq üçün basın"""

    BEFORE_SUCC_LOGIN = "kod alındı. web səhifə silinir ..."

    ERRED_PAGE = "bir şey səhvdir. Sahiblə əlaqə saxlayın. \n\n@SOQrup"

    CANCELLED_MESG = " /start yenidən başlatmaq..."

    IN_VALID_CODE_PVDED = "üzr istəyirik, daxil etdiyiniz kod düzgün deyil!"

    IN_VALID_PHNO_PVDED = "üzr istəyirik, daxil etdiyiniz nömr| düzgün deyil xaiş edirəm düzgün yazın!"
