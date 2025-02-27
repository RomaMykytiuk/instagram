# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#     def show_info(self):
#         print(f"{self.name}: {self.price} грн")
#
# class ShoppingCart:
#     def __init__(self):
#         self.items = []
#
#     def add_item(self, product):
#         self.items.append(product)
#
#     def total_price(self):
#         return sum(item.price for item in self.items)
#
#     def show_cart(self):
#         for item in self.items:
#             item.show_info()
#         print(f"Total Price: {self.total_price()} грн")
#
# milk = Product("Молоко", 25)
# bread = Product("Хліб", 15)
#
# cart = ShoppingCart()
# cart.add_item(milk)
# cart.add_item(bread)
#
# cart.show_cart()
#
# name = (input())
# text = "Привіт "
# print(text + name)
#
# spicok = [1, 7, 9, 12]
# num = int(input("Введіть число"))
# if num in spicok:
#     print('ти вгадав')
# else:
#     print('ти не вгадав')
#
# magic_word = 'будь ласка'
# num = (input("яке чарівне слово"))
# if num == magic_word:
#     print('ласкаво просимо!')
# else:
#     print('у доступі відмовлено!')
#
# def brew_potion(ingredient):
#     potion.append(ingredient)
#
# potion = []
#
# brew_potion('вода')
# brew_potion('вода2')
#
# print('інградієнти')
# for ingredient in potion:
#     print(f'{ingredient}')
#
# a = int(input('введіть глибину'))
# if a <= 5:
#     print('все ок')
# else:
#     print('глибоко')
#
# a = {
#     'fireball': 'запуск вогняної кулі',
#     'heal': 'зцілення рани'
# }
#
# a_name = input('введіть назву закляття')
#
# if a_name in a:
#     print(f'опис закляття: {a[a_name]}')
# else:
#     print('такого закляття немає')
#
# crystals = 5
#
# for i in range(1, crystals + 1):
#     print(f"Кристал №{i} зібрано!")
#
# print(f"Загальна кількість зібраних кристалів: {crystals}")
#
# class Hero:
#     def __init__(self, hp):
#         self.hp = hp
#
#     def take_damage(self, amount):
#         self.hp -= amount
#         if self.hp <= 0:
#             print("ти програв!")
#
# hero = Hero(100)
# hero.take_damage(30)
# hero.take_damage(80)
#
# num = int(input("Скільки істот буде у списку? "))
#
# creature_list = {}
#
# for _ in range(num):
#     code = input("Введи код істоти: ")
#     creature = input("Введи назву істоти: ")
#     creature_list[code] = creature
#
# print("Список істот:")
# for code, creature in creature_list.items():
#     print(f"{code}: {creature}")
#
# creature = input("Яку істоту ти зустрів? (wolf, bear, wizard): ")
#
# if creature == "wolf":
#     print("Ти борешся з вовком!")
# elif creature == "bear":
#     print("Ти біжиш від ведмедя!")
# elif creature == "wizard":
#     print("Ти ведеш розмову з чарівником!")
# else:
#     print("Нічого цікавого не відбулося.")

#
# s = ['хліб','Молоко','яйця']
# s.remove('яйця')
# print(s)
#
# p = {'Ігорь':'+38004043413','Роман':'+380965499432'}
# a = input()
# print(p[a])

#
# class Dog:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def bark(self):
#         print(f'Гав! я - {self.name}')
#
# dog = Dog('шарік', 3)
# dog.bark()
#
#
#


# with open("YT.txt")as a :
#     print(a.read())


#
# with open('product.txt', 'w',encoding='utf-8')as f:
#     f.write("Apples\nBread\nMilk\nEggs")
#
# with open('product.txt', 'a',encoding='utf-8')as e:
#     e.write('\nappalesss')




#
# with open('story.txt', 'r', encoding='utf-8') as f:
#     content = f.read()
# content = content.replace('.', '').replace(',', '').replace('!', '').replace('?', '')
# words = content.split()
# word_count = len(words)
# print(f"Кількість слів у тексті: {word_count}")
#_________________________________________________
# n = int(input())
# result  = 1
# for i in range(1,n+1):
#     result *= i
# print(result)
#
#
# text = input()
# reversed_str = ""
# for i in range(len(text) - 1, -1, -1):
#     reversed_str += text[i]
# print (reversed_str)
#
# text = 'venom'
# print(text[::-1])
# n = int(input())
# fib = [0,1]
# x = 0
# for i in range(2,n+1):
#      next_number = fib[x] + fib[x+1]
#      fib.append(next_number)
#      x+=1
# print(fib)

#
# numbers = input().split()
# if numbers:
#     numbers = list(map(int, numbers))
#     min_num = min(numbers)
#     max_num = max(numbers)
#     print(f"Найменше : {min_num}")
#     print(f"Найбільше : {max_num}")
# else:
#     print("")


#
# def max_of_three(a,b,c):
#     if a > b and a > c:
#         max_num = a
#     elif b > a and b > c:
#         max_num = b
#     elif c > a and c > b:
#         max_num = c
#     return max_num
#
# max_num = (max_of_three(2,4,7))
# print(max_num)

# def factorial(n):
#     x = 1
#     for i in range(1,n+1):
#         x*=i
#     return x
# x = factorial(5)
# print(x)

#
# def greet(name):
#     print(f'Привіт, {name}!')
#
# greet('Роман')
#

# def add_nembers(a,b):
#
#     return a + b
# print(add_nembers(1,5))
#
#
# def is_even(n):
#     return n % 2 == 0
# print(is_even(4))


#
# grades = {"Anna": 85, "Boris": 90, "Viktor": 78}
# name = input("Введіть ім'я учня: ")
# score = int(input("Введіть нову оцінку: "))
# grades[name] = score
# print("Оновлений список оцінок:", grades)
#
#
# key = {"apple": "red", "banana": "yellow", "grape": "purple"}
# name = input("Введіть назву фрукта: ").lower()
# if name in key:
#     print(f"Колір {name}: {key[name]}")
# else:
#     print("Фрукт не знайдено.")

class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        self.speed = 0

    def start(self):
        print("Машина поїхала!")

    def accelerate(self, value):
        self.speed += value

    def brake(self):
        self.speed = 0

my_car = Car("Tesla", "червона")
my_car.start()
my_car.accelerate(50)
print("Швидкість:", my_car.speed)
my_car.brake()
print("Швидкість після гальмування:", my_car.speed)


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grade = 0

    def study(self):
        print(f"Учень {self.name} вчиться!")

    def set_grade(self, grade):
        self.grade = grade

student1 = Student("Олег", 10)
student1.study()
student1.set_grade(12)
print("Оцінка:", student1.grade)

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hunger = 5
    def meow(self):
        print(f"Мяу! Мене звати {self.name}!")

    def eat(self):
        self.hunger = max(0, self.hunger - 2)

    def play(self):
        self.hunger += 3

my_cat = Cat("Барсик", 3)
my_cat.meow()
my_cat.play()
print("Рівень голоду:", my_cat.hunger)
my_cat.eat()
print("Рівень голоду після їжі:", my_cat.hunger)
