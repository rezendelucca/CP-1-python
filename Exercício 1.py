Real = float(input("Insira um valor em reais"))
Dolar = round(Real / 5.68, 2)

print(Real, "Em reais equivale a: ", Dolar, "Dolar")

Euro = round(Real / 6.17, 2)
print(Real, "Em reais equivale a: ", Euro, "Euro")

LibraEsterlina = round(Real / 7.4, 2)
print(Real, "Em reais equivale a: ", LibraEsterlina, "Libra Esterlina")

PesoArgentino = round(Real * 188.72, 2)
print(Real, "Em reais equivale a: ", PesoArgentino, "Peso Argentino")

Iene = round(Real * 26, 2)
print(Real, "Em reais equivale a: ", Iene, "Iene")