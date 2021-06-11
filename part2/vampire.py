from .warrior import Warrior
class Vampire(Warrior):
  """Warrior is first fighter you can create."""

  def __init__(self, strength=4, life_point=40, vampirism=50):
    """
    :param strenght: damage that will inflict the warrior
    :param life_point: Maximum life point that warrior can hold
    :param vampirisme: Helps him to heal himself (50% attack)
    """

    # definit pts de vie

    self._alive = life_point > 0
    self.vampirism = vampirism

    super().__init__(strength=strength, life_point=40)


  def nosferatus(self):
    """
        :param nosferatus: exact blood calcul
    """
    jeboistonsang =int((self.strength * self.vampirism)/100)
    self.health += jeboistonsang
