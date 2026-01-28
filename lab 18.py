class Resident:
    def __init__(self,name):
        self.name=name
        self.hunger=60
        self.energy=80
        self.is_alive=True
    def status(self):
        return f'{self.name}|голод:{self.hunger}|энергия:{self.energy}'
    def live_day(self):
        '''пасивное старение'''
        self.hunger-=15
        self.energy-=15
        if self.hunger <=0 or self.energy<=0:
            self.is_alive=False
        def react_to_mess(self):
            pass
class WorkerSim(Resident):
    def __init__(self,name,money):
        super().__init__(name)
        self.money=money
    def work(self):
        print(f'{self.name}пашет на двух работах!+150$')
        self.money+=150
        self.energy-=40
        self.hunger-=20
    def react_to_mess(self):
        print(f'{self.name}:опять этот мусор! Сил моих нет (Минус 20 настроения!)')
        self.energy-=10
class LazySim(Resident):
    def __init__(self, name):
        super().__init__(name)
        self.laziness=100
    def live_day(self):
        self.hunger-=5
        self.energy-=5
        if self.hunger<=0 or self.energy<=0:
            self.is_alive=False
    def sleep_on_trash(self):
        print(f'{self.name}прилёг на гору грязного бнлья. удобно')
        self.energy+=40
        self.hunger-=5
    def react_to_mess(self):
        print(f'{self.name}:какой мусор? это же элементы интерьера')
worker=WorkerSim('артур(работяга)', 100)
lazy_guy=LazySim('ларри(ленивец)')
rommates=[worker, lazy_guy]
day=1
is_messy=True
print('симулятор коммуналки запущен')
while True:
    print(f'\n===день{day}===')
    if not all(r.is_alive for r in rommates):
        dead=next(r for r in rommates if not r.is_alive)
        print(f'конец игры:{dead.name}откинулся')
        break
    print(f'общак артура:{worker.money}$|состояние:')
    for r in rommates:
        print(r.status())
        print('\n Ваш выбор')
        print('1.артур:пойти на работу (+150$)')
        print('2.артур:купить пиццу на всех(-50$)')
        print('3.ларри:поспать в куче хлама (+энергия)')
        print('4.ларри:попросить у артура денег на еду')
        print('5.убраться в комнате(артур тратит энергию)')
        print('0.выход')
        choice=input('действие:')
        if choice=='1':
            worker.work()
        elif choice=='2':
            if worker.money>=50:
                worker.money-=50
                for r in rommates:
                    r.hunger=min(100, r.hunger+40)
                print('пицца заказанаю все поеди')
            else:
                print('нет денег на пиццу!')
        elif choice=='3':
            if is_messy:
                lazy_guy.sleep_on_trash()
            else:
                print('хлама нет, пришлось спать на голом полу. Спина болит.')
                lazy_guy.energy+=10
        elif choice=='4':
            print(f'ларри клянчит деньги.Артур в ярости!')
            worker.energy-=5
        elif choice=='5':
            print(f'артур вынес 40 мешков мусора.')
            is_messy=False
            worker.energy-=30
        elif choice=='0':
            break
        print('\n ночь в коммуналке')
        time.sleep(1)
        for r in rommates:
            r.live_day()
            if is_messy:
                r.react_to_mess()

        day+=1
print('игра завершена')