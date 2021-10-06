x = int(input("Digite um número : "))
y = int(input("Digite um número : "))
aux = 0

if x > y:
    print("OPÇÃO INVALIDA ")
    x = int(input("Digite um número inteiro: "))
    y = int(input("Digite um outro número maior que o anterior: "))
else:
    while x <= y:
        aux = aux + x
        x += 1

print("O valor total da soma e:",aux)