class Ghost:
    def __init__(self):
        import random
        colors = ["white", "yellow", "purple", "red"]
        color = colors[random.randint(0, 3)]
        self.color = color

#Create a class Ghost
#Ghost objects are instantiated without any arguments.
#Ghost objects are given a random color attribute of "white" 
#or "yellow" or "purple" or "red" when instantiated