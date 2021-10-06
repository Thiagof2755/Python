valores=list(range(1,21))
x = 1 

operacao = int(input ("Digite 1 para Lista em ordem horizontal e 2 Para vertical  :  \n"))
if operacao == 1 :
    print(valores)
elif operacao == 2:
   while x <21 :
       print(x)
       x +=1
else: 
    print("Opção invalida ")