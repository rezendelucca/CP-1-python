ano = int(input("Digite quantos anos voce tem: "))
mes = int(input("Digite quantos meses voce tem: "))
dia = int(input("Digite quantos dias voce tem: "))

print("Digite o seu dia de nascimento")

Dias_somados = (ano * 365) + (mes * 30 ) + dia

print(f"Você viveu {Dias_somados} dias")
