x = 1
total = 0 
while x<6 :
    soma= float(input(f"Digite sua {x} nota "))
    x+=1
    total=(total+soma)
    media=total/5
print ("A soma é %.0f"%total)
print ("A media é %.0f "%media )