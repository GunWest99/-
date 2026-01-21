import time
import random
#1 базовый класс
class sim:
    def __nit__(self, name):
        self.name=name
        self.hunger=50
        self.energy=100
        self.is_alive=True
    def eat(self):
        if self.hunger>=100:
            print(f'{self.name}не хочет есть.')
        else:
            self.hunger+=20
            self.energy-=5
            print(f'{self.energy}поел(а).Голод:{self.hunger}')
def live_day(self):
    '''Этот метод вызывается каждый ход. Жизнь идётб ресурсы тратятся.'''
    self.hunger-=10
    self.energy -=10
    if self.hunger<=0 or self.energy<=0:
        self.is_alive=False
        print(f'{self.name} не выдержал суровой жизни и покинул чат.')
def status(self):
    return f'{self.name}|Голод:{self.hunger}|Энергия:{self.energy}'
#2 класс наследники
class Human(sim):
    def __init__(self, name, job):
        super().__init__(name)
        self.job=job
        self.money=50
    def work(self):
        self.energy-=30
        self.hunger-=20
        self.money+=100
        print(f'{self.name}сходил на работу({self.job}).+100$. Энергия: {self.energy}')
#взаимодействие: Человек кормит кого-то (Связь объектов!)
    def feed_pet(self, pet):
        if self.money >=20:
            print(f'{self.name} покупает корм и кормит {pet.name}...')
            self.money-=20
            pet.eat()
        else:
            print(f'y {self.name} ет денег на корм! Иди работай!')
    def repair_robot(self, robot):
        print(f'{self.name}чинит{robot.name}...')
        self.energy-=20
        robot.energy=100
        print(f'{robot.name}полностью заряжен!')
class dog(sim):
    def eat(self):
        self.hunger+=30
        print(f'{self.name}жадно грызёт кость! гав!')
        def play(self, human):
            print('f{self.name}приносит мячик{human.name}.')
            self.energy-=20
            human.energy+=10
            print(f'{human.name}повеселел!')
class robot(sim):
    def __init__(self, name):
        super().__init__(name)
        self.battery=100
    def live_day(self):
        self.energy-=5
    def eat(self):
        print(f'{self.name}подключается к розетке. Зарядка...')
        self.energy=100
    def  cook_dinner(self, human):
        if self.energy>20:
            print(f'{self.name}готовит ужин для {human.name}.')
            self.energy-=20
            human.eat()
        else:
            print(f'{self.name}:Батарея разряжена. Не могу готовить.')
# 3 игровой мир
player=Human('Алекс', 'Программист')
doggo=dog('бобик')
robo=robot('Вертер-3000')
household=[player, doggo, robo]
day=1
print('добро пожаловать в симс: YTHON EDITION')
#4 игровой цикл
while True:
    print(f'\n===день{day}===')
    game_over=False
    for sim in household:
        if not sim.is_alive:
            print(f'GAME OVER: {sim.name}погиб')
            game_over = True
    if game_over:
        break
    print(f'деньги:{player.money}$')
    for sim in household:
        print(sim.status())
        print('\n что будет делать алекс?')
        print('1. пойти на работу')
        print('2. поесть самому (-20$ еда)')
        print('3. покормить бобика (-20$ корм)')
        print('4.поиграть с бобиком')
        print('5. попросить робота приготовить ужин (бесплатно)')
        print('6.починить робота')
        print('0.выход')
        choice=input('твой выбор:')
        if choice =='1':
            player.work()
        elif choice =='2':
            if player.money>=20:
                player.money-=20
                player.eat()
            else:
                print('нет денег!')
        elif choice =='3':
            player.feed_pet(doggo)
        elif choice =='4':
            doggo.play(player)
        elif choice =='5':
            robo.cook_dinner(player)
        elif choice=='6':
            player.repair_robot(robo)
        elif choice =='0':
            print('пока!')
            break
        else:
            print('неверная команда, день прошёл впустую...')
            print('\n наступает ночь...Вск показатели падают.')
            time.sleep(1)
            for sim in household:
                sim.live_day()
            day+=1