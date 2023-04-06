class SuperHero:
    people = 'people'
    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def name(self):
        return self.name
    def health_points(self):
        return self.health_points*2
    def __str__(self):
        return f'меня зовут {self.name}\n'\
               f'мой ник {self.nickname}\n' \
               f'моя суперсила {self.superpower}\n' \
               f'мой удвоенный уровень здоровья {self.health_points*2}\n' \
               f'моя коронная фразочка {self.catchphrase} и длина {len(self.catchphrase)} символов'
    def __len__(self):
        return len(self.catchphrase)

class Hero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        super(Hero, self).__init__(name, nickname, superpower, health_points, catchphrase)
pers1 = Hero("Violet", "RIDE", "Boosthand", 1800, "GET OUT HERE!")
print(pers1.__str__())
