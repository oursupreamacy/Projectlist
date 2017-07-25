st = input("Введите строку: ")
spc = 0

for x in range(1, len(st)):
    if st[x] == " " and st[x-1] != " " and st[x+1] != " ":
        spc += 1

print(spc+1)