class Animal(object):
    def __init__(self ,name,weight):
        self.name = name
        self.weight = weight
        self.size = None 
        self.species = None
        self.food_type = None
        self.nocturnal = False
    def sleep(self):
        if self.nocturnal:
            print(f"{self.name} , sleeps during the day")
        else:
            print(f"{self.name} , sleeps during the night")
    def eat(self,food):
        if self.food_type == 'omnivore':
            print(f"{self.name,self.species},thinks its yummy")
        elif(food == 'meat' and self.food_type =='carnivore')or (food == 'plants'and self.food_type =='herbivore'):
            print(f"{self.name,self.food_type,food} thinks the food is tasty")
        else:
            print('i dont eat these')
class Elephant(Animal): 
    def __init__(self,name,weight):
        super().___init__(name,weight)
        self.size = "huge"
        self.species = "elephant" 
        self.food_type = "herbivore" 
        self.nocturnal = False
class Tiger(Animal): 
    def __init__(self,name,weight):
        super().___init__(name,weight)
        self.size = "huge"
        self.species = "Tiger" 
        self.food_type = "carnivore" 
        self.nocturnal = False
class Monkey(Animal): 
    def __init__(self,name,weight):
        super().___init__(name,weight)
        self.size = "medium"
        self.species = "Monkey" 
        self.food_type = "omnivore" 
        self.nocturnal = True
def add_animal_to_zoo(zoo, animal_type, name, weight):
        animal = None
        if animal_type == 'Monkey':
            animal = Monkey(name,weight)
        elif animal_type == 'Tiger':
            animal = Tiger(name,weight)
        else:
            animal = Elephant(name,weight) 
        zoo.append(animal)
        return zoo
    
to_create = ['Elephant','Tiger','Monkey']
zoo = []
for i in to_create: 
    zoo = add_animal_to_zoo(zoo,i,'name',100)
zoo
def feed_animals(zoo,  time ='Day'):
    for animal in zoo:
        if ((time == 'Day'and not animal.nocturnal) or (time == 'Night' and animal.nocturnal)):
            if animal.nocturnal == False:
                if animal.food_type == 'carnivore':
                    animal.eat('meat')
                else:
                    animal.eat('plants')
            else:
                if animal.nocturnal == True:
                    if animal.food_type == 'carnivore':
                        animal.eat('meat')
                    else:
                        animal.eat('plants')
feed_animals(zoo)
feed_animals(zoo,'Night')
        