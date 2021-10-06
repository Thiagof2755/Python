numero = 1
x= -1 
while numero<6 : 
    y = int(input(f"Digite o primeiro numero {numero} ª : "))
    numero+= 1
    if x<y:
       x = y 
       y=0
print("sua maior numero foi ",x)