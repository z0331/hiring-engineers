import random

from checks import AgentCheck

class RandomCheck(AgentCheck):
   def check(self, instance):
      # check random
      r = random.random()

      self.gauge('test.support.random', r, tags=['random_check'])
