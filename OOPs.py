#names and age
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def say_hello(self):
        print(f"Hello, my name is {self.name} and my age is {self.age}.")
#creating my object
person1=Person("Grace",18)
person1.say_hello()
person2=Person("Edward",14)
person2.say_hello()
person3=Person("Mark",6)
person3.say_hello()
person4=Person("Winnie",23)
person4.say_hello()
person5=Person("Emma",27)
person5.say_hello()
person6=Person("Ken",30)
person6.say_hello()
person7=Person("Jane",48)
person7.say_hello()
person8=Person("Stanley",54)
person8.say_hello()
print()
print()
    #create a class called cars with the following attributes/properties
    #make,model,year then create a function that prints make, model and year
    #then create three objects
class Cars:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def say_car(self):
        print(f"This is {self.make}. The model is {self.model}. Manufactured in the year {self.year}.")
car1=Cars("Mercedez-Benz","A-Class",2022)
car1.say_car()
car2=Cars("Audi","A3",2022)
car2.say_car()
car3=   Cars("Ford","Expedition MAX",2021)
car3.say_car()
car4=Cars("Toyota","Prius",2015)
car4.say_car()
car5=Cars("Toyota","Corona",1966)
car5.say_car()
car5=Cars("Honda","Accord sdn",2013)
car5.say_car()
car6=Cars("Ford","Deluxe",1958)
car6.say_car()
car7=Cars("Ford","F1",1948)
car7.say_car()
car8=Cars("Frazer","Manhattan",1948)
car8.say_car()
car9=Cars("Acura","MDX",2022)
car9.say_car()
car10=Cars("BMW","A5",2022)
car10.say_car()
print()
print()
    #countries and their capital cities
class Country:
    def __init__(self,country,capital):
        self.country=country
        self.capital=capital
    def say_country(self):
        print(f"This is {self.country}. The capital city is {self.capital}.")
country1=Country("Kenya","Nairobi")
country1.say_country()
country2=Country("Somalia","Mogadishu")
country2.say_country()
country3=Country("Uganda","Khartoum")
country3.say_country()
country4=Country("Egypt","Cairo")
country4.say_country()
country5=Country("Austrlia","Australia")
country5.say_country()
country6=Country("Afghanistan","Kabul")
country6.say_country()
country7=Country("Albania","Tirania")
country7.say_country()
country8=Country("Guatemala","Guatemala City")
country8.say_country()
country9=Country("India","New Delhi")
country9.say_country()
country10=Country("Spain","Madrid")
country10.say_country()


