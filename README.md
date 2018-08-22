
# Python

## Sobre a linguagem

Python é uma linguagem interpretada, de tipagem forte. Ela é multi paradigma, suportando o paradigma da Orientação a objetos, paradigma funcional, etc. É muito usada para aplicações web, com frameworks como Django, Flask ou Pyramid. Também é usada muito na área de inteligência artificial e análise de dados.

## Dinâmico

```
x = 5;
print(x)
# 5

x = "John"
print(x)
# "John"
```

## Tipagem forte

```
x = 99

x = x + "not a number"
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

## Operadores

```
- Soma
- Subtração
- Multiplicação
- Divisão

x = 5
y = 6
print(x + y)
print(x - y)
print(x * y)
print(x / y)
```

## Comparadores

- Maior / maior que
- Menor / menor que
- Identidade
- Equalidade

```
5 > 3
6 < 10
5 == 5 # True
5 == "5" # False
```

## Condicionais

If / Else

```
if idade > 18:
  print("Maior de idade")
else:
  print("Menor de idade")
```

```
if idade > 18:
  print("Maior de idade")
elif idade == 18:
  print("Você tem exatamente 18!")
else:
  print("Menor de idade")
```

Desafio: Criar condicionais usando alguns comparativos

## Funções

- Um bloco de código designado para realizar um conjunto de comandos.
- Pode retornar algum valor, ou não retornar nada.
- Uma função é executada quando ela é Invocada (chamada)

```
def hello_world():
  print("Hello world")

def soma(a, b):
  return a + b

print(soma(4, 8))
print(soma(5, 20))
print(soma(3, 7))

// Escopo
x = 10

def a():
  print(x)

print(a())

x = 10
def b():
  x = 20;
  print(x)

print(b())
print(x)

```

* Desafio: Calculador de IMC

## Vetores

Vetores, ou Arrays são uma forma de estrutura de dados, onde é possível armazenar uma lista de elementos.

```
arr = []

# inserindo elementos ao array
arr.append('Abacate');
arr.append('Melancia');

print(arr)

# retirando elementos pelo inicio
fruit = arr.pop();

print(fruit)
print(arr)
```

## Dicionario

```
hugo = {
  'first_name': 'Hugo',
  'last_name': 'Tamaki',
  'books': ['O pequeno principe', 'Lerinho', 'bafafa']
}

print(hugo['first_name'])
print(hugo['last_name'])
print(hugo['books'])


```

Desafio: Como implementar uma função que dado um número (ex: 1, 2, 3...) retorna o mês correspondente? (ex: Janeiro, Fevereiro...)

### Objeto

```
class Person():
  def say_hello():
    print("Hello world!")

person = Person()

person.say_hello()
# Hello world!
```

## Loops

### For

```
# repete 10 vezes hello world
for x in range(5):
  print("hello world")

# printa números de 0 a 5
for x in range(5):
  print(x)

# printa conteúdo de arrays
fruits = ['Apple', 'Banana', 'Melon']

for fruit in fruits:
  print(fruit)

evens = []

for num in range(5):
  if num % 2 == 0:
    evens.append(num)

print(evens)
```
### While

```
i = 0;

while i < 10:
  print('ahsuahsuahs')
  i += 1
```


