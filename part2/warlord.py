from part2.warrior import Warrior

class Warlord(Warrior):
  """Trainned from Warrior."""

  def __init__(self, strength=4, life_point=100, defense=2):
    """
    :param strength: strength of defender live
    :param life_point: Maximum Life Point live
    :param defense: Defense to reduce damage taken live
    """
    self.defense = defense
    super().__init__(strength=strength, life_point=life_point)

  def damaged(self, dmg):
    """
    reduce damage from self.defense call Warrior.damaged live
    :param dmg: damage to be reduced live
    """
    dmg -= self.defense
    dmg= max(dmg, 0)
    super().damaged(dmg)
