class Cat():

    species = 'Feline'


    def __init__(self, breed):
        self.breed = breed

    def meow(self, number):
        print(f'MEOW! My breed is {self.breed} and the number is {number}')


my_cat = Cat(breed='shorthair')

type(my_cat)

my_cat.meow(23)