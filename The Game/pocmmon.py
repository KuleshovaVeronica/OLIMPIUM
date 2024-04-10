import random
s=0
FAN=0
f=0
class MONSTER:
    def __init__(self,NAME,LV,HP,EXP):
        self.NAME=NAME
        self.LV=LV
        self.HP=HP
        self.EXP=EXP
    def MOVE(self,z):
        print(f'*{self.NAME} двигается в напралении {z}')
        print(f'*Может здесь кто-нибудь затаился...?')
        s=random.randint(1,8)
    def ATTACK(self,MON2):
        print(f'*{self.NAME} встречает в зарослях {MON2}!')
        print(f'*{self.NAME} атакует {MON2}!')
    def EXPUP(self,EXP):
        self.EXP+=EXP
        print(f'*{self.NAME} получил {EXP} опыта!')
    def LVUP(self):
        self.LV+=1
        self.HP+=10
        print(f'*{self.NAME} получил новый уровень! Его здоровье было увеличенно до {self.HP}!')

print('*Добро пожаловать в игру PocketMonster!')
print('*Введите имя вашего отважного монстра: ')
n=input('# ')
MN=MONSTER(n, 1, 100, 0)
MONSTERS=['Змея','Волк','Тигр','Рыжая Треска!','Скелет','Великан','Ловец','Крокодил','Мышь']

while True:
    print('*Введите команду (move/attack/exit): ')
    x=input('# ')
    if x=='move':
        f=0
        FAN=random.randint(1,5)
        print('*Введите направление (up/down/left/right): ')
        z=input('# ')
        MN.MOVE(z)
    elif x=="attack":
     if f<2:
        if FAN>3:
         s=random.randint(1,8)
         f+=1
         MON2=MONSTERS[s]
         MN.ATTACK(MON2)
         if MON2=='Великан':
          MN.EXPUP(60)
         elif MON2=='Мышь':
          MN.EXPUP(10)
         elif MON2=='Ловец':
          MN.EXPUP(100)
         elif MON2=='Рыжая Треска!':
          MN.EXPUP(1)
         else:
          MN.EXPUP(30)
         if MN.EXP >= 100:
            MN.LVUP()
        else:
           print('*Здесь никого... может двинемся далее?')
     else:
           print('*Здесь никого... может двинемся далее?')
    elif x=="exit":
        print('*Вы вышли из игры!')
        print('*Спасибо за игру!')
        break
    else:
        print('*Ошибка в команде!')