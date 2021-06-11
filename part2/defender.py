
from part2.warrior import Warrior

class Defender(Warrior):
  """Trainned from Warrior."""

  def __init__(self, strength=3, life_point=55, defense=2):
    """
    :param strength: strength of defender
    :param life_point: Maximum Life Point
    :param defense: Defense to reduce damage taken
    """
    self.defense = defense
    super().__init__(strength=strength, life_point=life_point)

  def damaged(self, dmg):
    """
    reduce damage from self.defense call Warrior.damaged
    :param dmg: damage to be reduced
    """
    dmg -= self.defense
    dmg= max(dmg, 0)
    super().damaged(dmg)
