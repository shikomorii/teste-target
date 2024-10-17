string = input("Digite uma string para inverter: ")

invertida = ""

indice = len(string) - 1 

while indice >= 0:
    invertida += string[indice]  
    indice -= 1  

print("String invertida:", invertida)
