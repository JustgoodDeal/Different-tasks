# Написать программу, запрашивающую у пользователя строку с текстом и разделитель.
# Необходимо вывести список слов с их длиной в начале слова, например, 5hello.
# # Для каждой из пользовательских функций написать функцию-тест.

def len_word(spisok):
    spisok = spisok.replace(' ', '')       # чтобы из элемента списка получилось слитное слово, удаляем пробелы  
    return len(spisok), spisok

def Test_len_word():
    assert len_word('dsfsdf') == (6, 'dsfsdf'), 'Тест провален'
    assert len_word(' bel ka ') == (5, 'belka'), 'Тест провален'
text = input()
razdelitel = input()
text_words = text.split(razdelitel)
for i in text_words:
    if len(i):                            # "исключаем" (фильтруем) пустые строки из списка
        lens, word = len_word(i)
        print(str(lens)+word)
Test_len_word()
