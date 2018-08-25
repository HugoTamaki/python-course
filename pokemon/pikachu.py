from random import randint

class Pikachu():
  def __init__(self):
    self.name = "Pikachu"
    self.life = 20

  def call(self, move, pokemon):
    moves = {
      'choque do trovao': self.thundershock,
      'cauda de ferro': self.iron_tail
    }

    result = moves.get(move, 'nao_existe')

    if result == 'nao_existe':
      return result
    else:
      result(pokemon)

  def thundershock(self, pokemon):
    damage = randint(1, 5)
    pokemon.life -= damage
    print(self.name + " deu dano de " + str(damage) + " em " + pokemon.name)

  def iron_tail(self, pokemon):
    damage = randint(1, 7)
    pokemon.life -= damage
    print(self.name + " deu dano de " + str(damage) + " em " + pokemon.name)
