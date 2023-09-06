import sys

# Tesseract-OCR path
path_tesseract = '/usr/share/tesseract-ocr/tessdata'
# Configuración de Terreract-OCR, para más información consultar la documentación
custom_config = r"--oem 3 --psm 11 -c tessedit_char_whitelist= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '"




# Date format
date_format = "%d/%m/%Y, %H:%M:%S"

# Spanish phone regExp
reg_exp_phone_spain = r"(?:(?:\+(?:[0]{0,4})?)?34[. -]{0,3})?[6789][0-9]{2}[ ]{0,3}(?:[0-9][ ]?){5}[0-9]"
# International phone regExp
reg_exp_phone_international = r"\+(9[976]\d|8[987530]\d|6[987]\d|5[90]\d|42\d|3[875]\d|2[98654321]\d|9[8543210]|8[6421]|6[6543210]|5[87654321]|4[987654310]|3[9643210]|2[70]|7|1)\d{1,14}"
# web address regExp
reg_exp_web = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
# ip regExp
reg_exp_ip = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
# Garbage characters regExp
reg_exp_garbage_characters = r"([A-Z])\w+|([0-9])\w+/gi"
# Source regExp
reg_exp_instagram = r"/(Instagram)?(instagram)?/g"
reg_exp_reddit = r"/(Reddit)?(reddit)?/g"
reg_exp_twitter = r"/(Twitter)?(twitter)?/g"

