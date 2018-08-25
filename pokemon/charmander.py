from random import randint

class Charmander():
  def __init__(self):
    self.name = "Charmander"
    self.life = 20

  def call(self, move, pokemon):
    moves = {
      'arranhar': self.slash
    }

    result = moves.get(move, 'nao_existe')

    if result == 'nao_existe':
      return result
    else:
      result(pokemon)

  def slash(self, pokemon):
    damage = randint(1, 5)
    pokemon.life -= damage
    print(self.name + " deu dano de " + str(damage) + " em " + pokemon.name)
