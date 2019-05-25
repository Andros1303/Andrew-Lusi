class Ball:
  def __init__(self, i=None):
      self.ball_type = "super"
      if i == None:
          self.ball_type = "regular"

#Create a class Ball.
#Ball objects should accept one argument for "ball type" when instantiated.
#If no arguments are given, ball objects should instantiate with a "ball type" of "regular."