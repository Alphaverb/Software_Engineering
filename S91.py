class Tomato:
    states = {'Отсутствует': 0, 'Цветение': 1, 'Зеленый': 2, 'Красный': 3}

    def __init__(self, index):
        self._index = index
        self._state = self.states['Отсутствует']

    def grow(self):
        if self._state < 3:
            self._state += 1

    def is_ripe(self):
        return True if self._state == 3 else False

class TomatoBush:
    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(1, num + 1)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):
        self.tomatoes = []

class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            print('Урожай собран!')
            self._plant.give_away_all()
        else:
            print('Подождите, томаты еще не дозрели')

    @staticmethod
    def knowledge_base():
        print('Справка по садоводству:\n'
              '1. Выбирайте сорта томатов, подходящие для вашего региона и климата\n'
              '2. Заготовьте плодородную почву с хорошим дренажем. Томаты любят рыхлую почву\n'
              '3. Сажайте рассаду томатов после последнего заморозка\n'
              '4. Регулярно поливайте томаты, особенно в период созревания плодов\n'
              '5. Применяйте удобрения с учетом потребностей томатов в питательных веществах\n'
              '6. Используйте опоры, чтобы поддерживать растения, особенно если у вас высокие сорта томатов\n'
              '7. Проводите обрезку, чтобы удалить лишние листья и побеги\n'
              '8. Регулярно осматривайте растения на наличие вредителей и признаков болезней\n')

Gardener.knowledge_base()

tomato_bush = TomatoBush(5)
gardener = Gardener('Брэд', tomato_bush)
# print(f"Садовник {gardener.name} выращивает {len(tomato_bush.tomatoes)} томат(а/ов)")

gardener.work()
# print(f"Томаты находятся в состоянии: '{list(Tomato.states.keys())[tomato_bush.tomatoes[0]._state]}'")

gardener.work()
gardener.harvest()

gardener.work()
gardener.work()
gardener.work()
gardener.harvest()