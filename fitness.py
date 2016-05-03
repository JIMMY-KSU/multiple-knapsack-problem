

class FitnessFunction(object):

  def __init__(self, chromosome, knapsack_items_map):
    self.chromosome = chromosome
    self.knapsack_items_map = knapsack_items_map

  def sum_item_attribute(self, m, attribute):
    '''returns the sum of specified attribute of items in knapsacks m'''
    return sum([item.profit if attribute == 'profit' else item.weight for item in self.knapsack_items_map[m]])

  def get_knapsack_capacity(self, m):
    '''returns capacity of knapsack m'''
    return RcParser().get_rc_knapsacks()[m]

  def sum_single_fitness(self, m):
    '''returns fitness of chromosomes in knapsack m'''
    if self.sum_item_attribute(m, 'weight') > self.get_knapsack_capacity(m - 1):
       self.random_repair(choice(range(1, len(self.chromosome), 2)), m)
    return self.sum_item_attribute(m, 'profit')

  def sum_all_fitness(self):
    '''returns total fitness of this chromosome'''
    fsum = 0
    for knapsack in range(1, RcParser().get_m() + 1):
      fsum = fsum + self.sum_single_fitness(knapsack)
    return fsum
 
