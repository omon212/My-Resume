# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
#
# from_email = 'omonnuloraimkulov@gmail.com'
# email_password = 'bpwr bjap qyvw chnm'
# to_email = 'mominovsharif12@gmail.com'
# subject = 'sharifjon'
# message = 'mominov'
# msg = MIMEMultipart()
# msg['From'] = from_email
# msg['To'] = to_email
# msg['Subject'] = subject
#
# msg.attach(MIMEText(message, 'plain'))
#
# smtp_server = 'smtp.gmail.com'
# smtp_port = 587
# try:
#     server = smtplib.SMTP(smtp_server, smtp_port)
#
#     server.starttls()
#
#     server.login(from_email, email_password)
#
#     server.sendmail(from_email, to_email, msg.as_string())
#     print('Email sent successfully!')
#
# except Exception as e:
#     print('Email could not be sent. Error:', str(e))
#
# finally:
#     server.quit()


# Morse kodlari lug'atini aniqlash
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
    ' ': ' ',  # Bo'sh joy (probel)
}

# Matnni Morse tiliga o'giruvchi funksiya
def text_to_morse(text):
    morse_code = []
    for char in text.upper():
        if char in morse_code_dict:
            morse_code.append(morse_code_dict[char])
        else:
            morse_code.append('?')  # Agar belgi lug'atta mavjud bo'lmasa, '?' qo'shamiz
    return ' '.join(morse_code)

# Morse kodni matnga o'giruvchi funksiya
def morse_to_text(morse_code):
    text = []
    morse_code = morse_code.split(' ')
    for code in morse_code:
        for key, value in morse_code_dict.items():
            if code == value:
                text.append(key)
                break
        else:
            text.append('?')  # Agar Morse kodi belgi bilan mos kelmasa, '?' qo'shamiz
    return ''.join(text)

# Matn -> Morse
text = input('Soz yozing: ')
morse = text_to_morse(text)
print(f"Matn: {text}")
print(f"Morse: {morse}")

# Morse -> Matn
# morse_code = "... .- .-.. --- --, -.. ..- -. -.-- --- -!"
# text = morse_to_text(morse_code)
# print(f"Morse: {morse_code}")
# print(f"Matn: {text}")
