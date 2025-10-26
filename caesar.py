'''
Функция для переданного символа возвращает полный алфавит того языка, к которому он принадлежит
(рассматриваются только английский и русский алфавиты)
'''
def get_alphabet(char: str) -> str:
    # для поиска по алфавитам используем тесно связанную с unicode-таблицами функцию ord
    if 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122:
        return "abcdefghijklmnopqrstuvwxyz"
    elif 1072 <= ord(char) <= 1103 or ord(char) == 1105 or 1040 <= ord(char) <= 1071 or ord(char) == 1025:
        return "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    # если символ не принадлежит ни к русскому, ни к английскому алфавиту, возвращаем пустую строку
    # (это нужно для функции shift_char)
    return ""


'''
Следующая функция для переданного символа возвращает символ, соответствующий сдвигу от исходного символа на
n-позиций в алфавите (число n указано параметром shift), как в шифре Цезаря. Алфавит символа передаётся отдельным
параметром.
'''
def shift_char(char: str, shift: int, alphabet: str) -> str:
    n = alphabet.find(char.lower()) # ищем версию символа в нижнем регистре
    if n == -1:
        return char
    if char.isupper(): # случай для символа, введённого в верхнем регистре
        return (alphabet[(n + shift) % len(alphabet)].upper())
    return (alphabet[(n + shift) % len(alphabet)]) # случай для символа, введённого в нижнем регистре


'''
Функция шифрования по Цезарю переданного текста (с указанным сдвигом)
'''
def encrypt(text: str, shift: int) -> str:
    encrypted = ""
    for t in text: # посимвольное шифрование с применением ранее введённых функций
        encrypted += shift_char(t, shift, get_alphabet(t))
    return encrypted


'''
Функция расшифровки переданного текста по известному сдвигу шифрования
'''
def decrypt(text: str, shift: int) -> str:
    decrypted = ""
    for t in text: # посимвольная расшифровка
        decrypted += shift_char(t, -shift, get_alphabet(t))
    return decrypted


'''
Функция запуска программы
'''
def run_caesar_cipher():
    text = input() # сначала в консоль вводится текст
    shift = int(input()) # затем сдвиг
    mode = int(input()) # после чего вводится число, соответствующее режиму работы программы
    if mode == 1: # 1 - шифрование
        print(encrypt(text, shift))
    elif mode == 2: # 2 - расшифровка
        print(decrypt(text, shift))


run_caesar_cipher()