print("Cadastro de usuario ")
nome = str(input("Digite seu Usuario : "))
senha = str(input("Cadatre um senha : "))

while nome == senha : 
  print("Usuario e senha não podem ser iguais !! ")
  nome = input("Digite seu Usuario : ")
  senha = (input("Cadatre um senha : "))
if nome != senha:
 print ("CADASTRO EFETUADO COM SUCESSO ")