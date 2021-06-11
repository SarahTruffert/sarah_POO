from .warlord import Warlord
class Army():
  """Army hold all fighter ready to battle."""

  def __init__(self):
    """Create an Empty Army"""
    self._army = []

  def __getitem__(self, item):
    """
    :param item: index
    :return : the Instance of a fighter.
    :raise : IndexError
    """
    return self._army[item]

  def __len__(self):
    """Builtin len"""
    return len(self._army)

  def rangement(self, entity):
    """ Range chaque entité """
    liste_entity=[]
    #print(liste_entity)
    for i in self._army:
      if entity in str(i):
        liste_entity.append(i)
        print(i)
    return liste_entity


  def addUnits(self, cls, number=1):
    """
    Add to the army

    :param cls: Class to be instancied
    :param number: Number of instance to create
    """
    while number > 0:
    # Si la classe et un Warlord :
      if cls is Warlord:
      # N' inclus qu'un seul Warlord :
        if len(self.rangement("Warlord"))<1:
          self._army.append(cls())
          break
    # Doit ranger l'armée dans tous les cas :
      else:
        self._army.append(cls())
      number-= 1

  def moveUnits(self):
    """
        La job du Warlord : je bouge les personnages !
    """
    # liste_Knight = []
    # liste_Healer = []
    # liste_Warlord = []
    # liste_Warrior = []


    # for entity in self._army:
    #   if len(liste_Warlord)==0:
    #     return self._army

    #   if "Knight" in str(entity):
    #     liste_Knight.append(entity)

    #   if "Healer" in str(entity):
    #     liste_Healer.append(entity)

    #   if "Warlord" in str(entity):
    #     liste_Warlord.append(entity)

    #   if "Warrior" in  str(entity):
    #     liste_Warrior.append(entity)


    if "Warlord" in str(self._army):
      Knight=self.rangement("Knight")
      Healer=self.rangement("Healer")
      Warrior=self.rangement("Warrior")
      Warlord=self.rangement("Warlord")
      if len(Knight) == 1 :
        self._army = Knight + Healer + Warrior + Warlord
      else:
        liste_finale = []
        liste_finale.append(Warrior[0])
        liste_finale += Healer
        liste_finale += Warrior[1:]
        liste_finale += Warlord
        self._army = liste_finale

     #return self._army


  def pop(self):
    """return the first soldier of the army."""
    ret = self._army.pop(0)
    return ret