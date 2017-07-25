wrd = input("Введите слово: ")

rewrd = wrd[::-1]

if rewrd == wrd:
    print(wrd, "- это палиндром")
else:
    print(wrd, "- это не палиндром")
