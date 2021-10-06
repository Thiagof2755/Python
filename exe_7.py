populacao_1 = float (1)
populacao_2 = float (0)
while populacao_1>populacao_2:
    populacao_1= float(input("Digite a População a alcançar :   "))
    populacao_2= float(input("Digite a População a ser alcançada:   "))
taxa_1 = float (0)
taxa_2 = float (1)
while taxa_1<taxa_2:
    taxa_1=float(input("Digite a porcentagem de crescimento ano da População 1 :   "))
    taxa_2=float(input("Digite a porcentagem de crescimento ano da População 2 :   "))
anos = int (0)
while (populacao_1<populacao_2):
    populacao_2 = populacao_2 +(populacao_2*taxa_2)
    populacao_1 = populacao_1 +(populacao_1*taxa_1)
    anos = anos +  1
print("foram necessarios %i anos Para o Pais A ultrapassar o B "% anos)
print("O Pais A com %.0f de Habitantes "% populacao_1)
print("O Pais B com %.0f de Habitantes "% populacao_2)
