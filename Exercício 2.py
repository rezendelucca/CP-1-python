num1 = int(input("Insira o número escolhido: "))

Centena  = (num1 // 100) *100
Dezena = (num1 % 10) *10
Unidade = num1 % 10

print("Seu número em centena é: ", Centena, "\nSeu Número em dezena é: ",  Dezena, "\nSeu número em unidade é: ", Unidade)