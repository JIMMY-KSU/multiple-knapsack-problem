class Knapsack(object):

  def __init__(self, capacity):
    self.capacity = capacity

   def __str__(self):
    return 'c = {0}'.format(self.capacity)

class KnapsackList(object):

  def __init__(self, knapsacks):
    self.knapsacks = knapsacks

