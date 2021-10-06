nota = int(1)
ordem = int (2)
print("Digite a sua 1º nota")
aux = float(input("Nota  : "))
while nota < 10:
    print("Digite a sua",ordem, "º nota")
    media = float(input("Nota  : "))
    aux = aux + media
    nota=nota+1
    ordem=ordem+1
aux= aux/10
print("Sua media é",aux)


