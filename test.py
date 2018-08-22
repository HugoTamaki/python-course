quantidade = int(input())
soma = 0
maior = -999999
menor = 999999

for n in range(quantidade):
  num = float(input())
  soma += num
  if num > maior:
    maior = num

  if num < menor:
    menor = num

media = soma / quantidade

print(media)
print(maior)
print(menor)
