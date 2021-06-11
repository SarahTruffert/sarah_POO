from part2.healer import Healer
from part2.vampire import Vampire
from part2.knight import Knight
#from part2.warrior import Warrior


def mais_t_es_ou(unit, entity, unit_second=None):
  """
      : To invoque the entities :
  """
  if isinstance(unit,entity):
    if entity == Knight:
      unit_second.damaged(unit.strength //2)
    if entity == Vampire:
      unit.nosferatus()
    if entity == Healer:
      unit_second.heal()

class Battlefield():
  """Battlefield used to battle two army against each other"""

  def simpleFight(self, army, army2):
    """
    :param army: First army
    :param army2: Second army
    :return bool: Did the first army won ?
    """

    while army[0].isalive():
      army2[0].damaged(army[0].strength)

      mais_t_es_ou(army[0], Vampire)
      if len(army2)>1:
        mais_t_es_ou(army[0], Knight, army2[1])
      if len(army)>1:
        mais_t_es_ou(army[1], Healer, army[0])
      if not army2[0].isalive():
        army2.pop()
        if len(army2)<1:
          return True

      army[0].damaged(army2[0].strength)
      mais_t_es_ou(army2[0], Vampire)
      if len(army)>1:
        mais_t_es_ou(army2[0], Knight, army[1])
      if len(army2)>1:
        mais_t_es_ou(army2[1], Healer, army2[0])
      if not army[0].isalive():
        army.pop()
        if len(army)<1:
          return False
