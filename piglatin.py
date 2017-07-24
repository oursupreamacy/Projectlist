orig = input("Введите слово латиницей: ")
vow = "aeiou"

def plc(s):
    if s[0] in vow:
        s += "ay"
        return s
    else:
        f = s[0] + "ay"
        s = s[1::]
        wd = s + f
        return wd

print(plc(orig))