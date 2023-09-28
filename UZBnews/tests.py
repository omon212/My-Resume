# from django.test import TestCase
# morse_code_dict = {
#     'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
#     'J': '.---',
#     'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...',
#     'T': '-',
#     'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
#     '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
#     '8': '---..', '9': '----.',
#     '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.',
#     ')': '-.--.-', '&': '.-...',
#     ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
#     '$': '...-..-', '@': '.--.-.'
# }
#
#
# def text_to_morse(text):
#     morse_code = []
#     for char in text.upper():
#         if char == ' ':
#             morse_code.append(' ')
#         else:
#             morse_code.append(morse_code_dict.get(char, ''))
#
#     return ' '.join(morse_code)
#
#
# def morse_to_text(morse_code):
#     morse_code = morse_code.split(' ')
#     text = []
#     for code in morse_code:
#         if code == '':
#             text.append(' ')
#         else:
#             text.append(next((char for char, morse in morse_code_dict.items() if morse == code), ''))
#
#     return ''.join(text)
#
#
# # Example usage:
# input_text = "Sharifjon"
# encoded_text = text_to_morse(input_text)
# decoded_text = morse_to_text(encoded_text)
# print("Input Text:", input_text)
# print("Encoded Text:", encoded_text)
# print("Decoded Text:", decoded_text)



import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from_email = 'raimkulovomon@gmail.com'
email_password = 'yfkf zvzh lfzg kklw'
to_email = 'omonnuloraimkulov@gmail.com'
subject = 'Qanday garang opcham'
message = 'siz kop gapirovirmang dovdirginam'

msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = subject

msg.attach(MIMEText(message, 'plain'))

smtp_server = 'smtp.gmail.com'
smtp_port = 587
try:
    server = smtplib.SMTP(smtp_server, smtp_port)

    server.starttls()

    server.login(from_email, email_password)

    server.sendmail(from_email, to_email, msg.as_string())
    print('Email sent successfully!')

except Exception as e:
    print('Email could not be sent. Error:', str(e))

finally:
    server.quit()
