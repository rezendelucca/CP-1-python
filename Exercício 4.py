dias = int(input("Digite o total de dias que você viveu: "))


anos = dias // 365
dias_restantes = dias % 365
meses = dias_restantes // 30
dias_finais = dias_restantes % 30

print("Você viveu", "\n Anos", anos, "\n Meses", meses, "\n Dias", dias_finais)
