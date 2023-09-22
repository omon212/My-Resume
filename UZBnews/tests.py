from django.test import TestCase
#
# # Create your tests here.


# Define the Morse code dictionary
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
