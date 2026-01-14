# class Cat:
#     def __init__(self,name):
#         self.name=name
#     def speak(self):
#         return f'{self.name}'
# my_cat=Cat('myrchik')
# print(my_cat.speak())
# my_cat.name='Барсик'
# print(my_cat.name)
#
#
#
#
# class Zombie:
#     def __init__(self,name):
#         self.name=name
#         self.heath=50
# z1=Zombie('dibil')
# print(z1.name)
# print(z1.heath)
#
#
#
# print('Битва до смерти')
# class Character:
#     def __init__(self, name, heath=50, max_heath=None, damage=1):
#         self.name=name
#         self.heath=heath
#         self.max_heath=max_heath or heath
#         self.damage=damage
# def status(self):
#     percent=(self.heath/self.max_heath)*100
#     return f'{self.name}: {self.heath}/{self.max_heath} HP ({percent:.0f}%) | Урон: {self.damage}'
# def attack(self, target):
#     return f'{self.name} бьёт {target.name} на {self.damage}!'
# def take_damage(self, damage):
#     self.heath-=damage
#     if self.heath<0:
#         self.heath=0
#     return f'{self.name} получил {damage} урона! Осталось: {self.heath} HP'
# def is_alive(self):
#     return self.heath>0
# class Enemy:
#     def __init__(self, name, heath=60, damage=15):
#         self.name=name
#         self.heath=heath
#         self.damage=damage
#         self.max_heath=heath
# def status(self):
#     percent = (self.heath / self.max_heath) * 100
#     return f'{self.name}: {self.heath}/{self.max_heath} HP ({percent:.0f}%) | Урон: {self.damage}'
# def attack(self, target):
#     return f'{self.name} бьёт {target.name} на {self.damage}!'
# def take_damage(self, damage):
#     self.heath-=damage
#     if self.heath<0:
#         self.heath=0
#     return f'{self.name} получил {damage} урона! Осталось: {self.heath} HP'
# def is_alive(self):
#     return self.heath > 0
# print('Собираем армию по чертежам...\n')
# hero=Character('Артур',120, damage=25)
# goblin=Enemy('Гоблин',50, 12)
# boss=Enemy('Дракон',200, 30)
# army=[hero, goblin, boss]
# print('Состав армии:')
# for unit in army:
#     print(unit.status())
#     print('\n'+'='*50+'\n')
# def battle_round(attacker, defender):
#     print(f'\n РАУНД БОЯЖ')
#     print(attacker.status())
#     print(defender.status())
#     print(attacker.attack(defender))
#     print(defender.take_damage(attacker.damage))
#     print(defender.status())
#     print('-'*30)
# print('Начинаеться битва!\n')
# battle_round(goblin, hero)
# battle_round(hero, goblin)
# battle_round(boss, hero)
# battle_round(hero, boss)
# print('\n'+'='*50+'\n')
# print('Итог битвы:')
# for unit in army:
#     status=unit.status()
#     if not unit.is_alive():
#         status+='Мертв'
#     print(status)
# print('\n===конец демонстрации ооп===\n')
# print('классы=чертежи')
# print('объекты=фигурки')
# print('методы=умения')
# print('атрибуты=характеристики(урон, здоровье)')
# print('готово к уроку-тестировано')





print('одинокий воин')
class Character:
    def __init__(self, name, heath=100, max_heath=None, damage=10):
        self.name=name
        self.heath=heath
        self.max_heath=max_heath or heath
        self.damage=damage
def status(self):
    percent=(self.heath/self.max_heath)*100
    return f'{self.name}: {self.heath}/{self.max_heath} HP ({percent:.0f}%) | Урон: {self.damage}'
def attack(self, target):
    return f'{self.name} бьёт {target.name} на {self.damage}!'
def take_damage(self, damage):
    self.heath-=damage
    if self.heath<0:
        self.heath=0
    return f'{self.name} получил {damage} урона! Осталось: {self.heath} HP'
def is_alive(self):
    return self.heath>0
class Enemy:
    def __init__(self, name, heath=60, damage=15):
        self.name=name
        self.heath=heath
        self.damage=damage
        self.max_heath=heath
def status(self):
    percent = (self.heath / self.max_heath) * 100
    return f'{self.name}: {self.heath}/{self.max_heath} HP ({percent:.0f}%) | Урон: {self.damage}'
def attack(self, target):
    return f'{self.name} бьёт {target.name} на {self.damage}!'
def take_damage(self, damage):
    self.heath-=damage
    if self.heath<0:
        self.heath=0
    return f'{self.name} получил {damage} урона! Осталось: {self.heath} HP'
def is_alive(self):
    return self.heath > 0
print('Собираем армию по чертежам...\n')
hero=Character('герой',100, damage=10)
goblin=Enemy('Гоблин',50, 5)
boss=Enemy('Босс',200, 20)
pomochnik=Character('помошник',70, 15)
army=[hero, goblin, boss]
print('Состав армии:')
for unit in army:
    print(unit.status())
    print('\n'+'='*50+'\n')
def battle_round(attacker, defender):
    print(f'\n РАУНД БОЯЖ')
    print(attacker.status())
    print(defender.status())
    print(attacker.attack(defender))
    print(defender.take_damage(attacker.damage))
    print(defender.status())
    print('-'*30)
print('Начинаеться битва!\n')
battle_round(goblin, hero)
battle_round(hero, goblin)
battle_round(boss, hero)
battle_round(hero, boss)
print('\n'+'='*50+'\n')
print('Итог битвы:')
for unit in army:
    status=unit.status()
    if not unit.is_alive():
        status+='Мертв'
    print(status)
print('\n===конец демонстрации ооп===\n')
print('классы=чертежи')
print('объекты=фигурки')
print('методы=умения')
print('атрибуты=характеристики(урон, здоровье)')
print('готово к уроку-тестировано')