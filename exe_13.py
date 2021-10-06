x = int(input("Digite um priemiro algarismo "))
y = int(input("Digite um segundo algarismo "))
meio = float
meio_2 = int
while x > y :
    print("Valores mencionados invalidos ")
    x = int(input("Digite um priemiro algarismo "))
    y = int(input("Digite um segundo algarismo "))
meio = y-x
if (meio%2) == 0:
    meio = meio/2
    meio = meio + x 
    meio_int =int (meio)
    print("",meio_int) 
else:
   meio = meio/2
   meio = meio + x 
   type(meio)
   meio_int = int (meio)
   meio_2=meio_int + 1 
   print(meio_int,"",meio_2)
   total_final= meio_int+meio_2
   print("A soma é ",total_final)