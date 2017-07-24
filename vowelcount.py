vow = "aeiouAEIOU"
fo = input("Введите фразу латиницей: ")
A = 0
E = 0
I = 0
O = 0
U = 0

def vowch(x):
    global A, E, I, O, U
    for n in range(0, len(x)):
        if x[n] in vow:
            if x[n] == "a" or x[n] == "A":
                A = A + 1
            elif x[n] == "e" or x[n] == "E":
                E = E + 1
            elif x[n] == "i" or x[n] == "I":
                I = I + 1
            elif x[n] == "o" or x[n] == "O":
                O = O + 1
            elif x[n] == "u" or x[n] == "U":
                U = U + 1


vowch(fo)

print("Общее количество гласных: ", A + E + I + O + U, "\nA: ", A, "\nE: ", E, "\nI: ", I, "\nO: ", O, "\nU: ", U)
