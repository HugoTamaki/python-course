from pikachu import Pikachu
from charmander import Charmander

combat = True

pikachu = Pikachu()
charmander = Charmander()

while combat:
  move = input("Digite o movimento: ")

  result = pikachu.call(move, charmander)

  if result == 'nao_existe':
    continue

  charmander.call('arranhar', pikachu)

  if pikachu.life <= 0 or charmander.life <= 0:
    if pikachu.life > 0:
      print("Pikachu wins")
    else:
      print("Charmander wins")

    combat = False
