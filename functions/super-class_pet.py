class Pet:
    def __init__ (self, name):
        self.name = name; # this.name = name;
    def feed (self, food):
        print (self.name + " was fed with " + food)
    def makeSound (self):
        print ("Ouh")

class Dog (Pet): # class Dog extends Pet
    def __init__ (self, name):
        super().__init__ (name)
        self.favoriteFood = 'bone'
    def makeSound (self):
        print ('Bark')
    def feed (self):
        super().feed (self.favoriteFood) # super.feed(...);

class Cat (Pet): # class Cat extends Pet
    def __init__ (self, name):
        super().__init__ (name)
        self.favoriteFood = 'meat'
    def makeSound (self):
        print ('Meow')
    def feed (self):
        super().feed (self.favoriteFood) # super.feed(...);
