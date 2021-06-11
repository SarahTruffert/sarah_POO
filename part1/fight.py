
def fight(unit_1, unit_2):
  """
  Simple Fight function

  :param unit_1: First unit to fight
  :param unit_2: Second unit to fight
  :return bool: True if unit_1 won the fight False otherwise"""
# counter = 10000

  while unit_1.isalive():
    unit_2.damaged(unit_1.strength)
# counter -= 1
    if not unit_2.isalive():
      return True
    unit_1.damaged(unit_2.strength)
  return False
