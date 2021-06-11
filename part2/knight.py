
from .warrior import Warrior
class Knight(Warrior):
  """Trainned from Warrior."""

  def __init__(self, strength=6, life_point=50):
    """
    :param strenght: damage that will inflict the Knight
    :param life_point: Maximum life point that Knight can hold
    :param claquette: when he hits the other unit, he also deals
     50% of the deal damage to the next enemy unit in line
    """

    # definit pts de vie
    self._alive = life_point > 0
    super().__init__(strength=strength, life_point=50)
