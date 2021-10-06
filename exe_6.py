populacao_1 = float (8000)
populacao_2 = float (20000)
taxa_1 = float (0.03)
taxa_2 = float (0.015)
anos = int (0)
while (populacao_1<populacao_2):
 populacao_2 = populacao_2 +(populacao_2*taxa_2)
 populacao_1 = populacao_1 +(populacao_1*taxa_1)
 anos = anos +  1

print("foram necessarios %i anos Para o Pais A ultrapassar o B "% anos)
print("O Pais A com %.0f de Habitantes "% populacao_1)
print("O Pais B com %.0f de Habitantes "% populacao_2)
