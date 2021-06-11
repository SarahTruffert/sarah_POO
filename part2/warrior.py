
class Warrior:
  """Warrior is first fighter you can create."""

  def __init__(self, strength=5, life_point=50):
    """
    :param strenght: damage that will inflict the warrior
    :param life_point: Maximum life point that warrior can hold
    """
    self.strength = strength
    self._alive = life_point > 0
    self._maxpts = life_point
    self._life = life_point

  @property
  def health(self):
    """
    Health property. update _alive state.
    """
    if self._life > self._maxpts:
      self._life = self._maxpts

    return self._life

  @health.setter
# proprieté vampirism du vampire :
  def health(self, value):

    self._life = value
    if self._life > self._maxpts:
      self._life = self._maxpts

# Le + 2 heal du healer :
  def heal(self):
    """
        :param heal: add 2 points of life
    """
    self.health += 2


  def presentation(self):
    """
    String representing the Warrior
    """
    msg = "{} {} life and {} strength"
    return msg.format("Warrior", self.health, self.strength)

  def damaged(self, dmg):
    """
    methods called when warrior receive damaged. Update _alive and _life..

    :param dmg: damage received.
    """
    self._life -= dmg
    if self._life <= 0:
      self._alive= False
      self._life=0

  def isalive(self):
    """:return bool: is Warrior Alive"""
    return self._alive
