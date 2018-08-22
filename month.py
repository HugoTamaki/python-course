def tradutor_meses(mes):
  meses = {
    '1': 'Janeiro',
    '2': 'Fevereiro',
    '3': 'Marco',
    '4': 'Abril'
  }

  return meses.get(mes, "Mes invalido")

mes = input("Digite um numero: ")
print(tradutor_meses(mes))