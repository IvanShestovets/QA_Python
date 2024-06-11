class Person:
    def __init__(self,name,age):
        self.name = name #self.name - атрибут name
        self.age = age #self.age - атрибут age


    def greet(self):
        
        

        print(f'Привет, я {self.name} и мне {self.age} лет.')

person1 = Person('Ivan', 38)
person1.greet()