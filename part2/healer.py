from .warrior import Warrior
# heal the ally standing right in front of him
# by +2 health points with the heal() method.
# ally's health after healing can't be greater
# than the maximum health of the unit.
class Healer(Warrior):
  """Trainned from Warrior."""

  def __init__(self, strength=0, life_point=60):
    """
    :param strength: strength of defender
    :param life_point: Maximum Life Point
    """

    super().__init__(strength=strength, life_point=life_point)
