class Translation(object):
    START_TEXT = """Salam, Ledy APİ'ə xoş gəldin!
Ledy APİ: Məni istifadə etdiyin üçün təşəkkürlər ❣️
my.telegram.org saytından APP-ID əldə etmək üçün Telegram Telefon Nömrənizi daxil edin.
nümünə: `+99450*******`
/start yenidən daxil etmək üçün istənilən mərhələdə başlayın""""
    AFTER_RECVD_CODE_TEXT = """I see!
now please send the Telegram code that you received from Telegram!
this code is only used for the purpose of getting the APP ID from my.telegram.org
if you do not trust this bot dev, please host this bot yourself
by opening https://github.com/LEGEND-AI/API-SCRAPPER and clicking on the Pink Button

/start yenidən daxil etmək üçün istənilən mərhələdə başlayın""""

    BEFORE_SUCC_LOGIN = "recieved code. Scarpping web page ..."

    ERRED_PAGE = "bir şey səhv oldu. proqram identifikatorunu əldə etmək alınmadı. \n\n@tenha055"

    CANCELLED_MESG = "Bye! Please re /start the bot conversation"

    IN_VALID_CODE_PVDED = "sorry, but the input does not seem to be a valid Telegram Web-Login code"

    IN_VALID_PHNO_PVDED = "sorry, but the input does not seem to be a valid phone number"
