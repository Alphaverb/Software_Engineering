class NoDogsAllowedException(Exception):
    pass

def checking(*items):
    forbidden_word = 'собака'

    for item in items:
        if forbidden_word in item.lower():
            raise NoDogsAllowedException('Никаких собак!')

    print('Можете проходить..')

if __name__ == '__main__':
    group1 = ('Кот', 'Черепаха', 'Попугай')
    group2 = ('Собака в шляпе', 'Кот', 'Мышь')

    try:
        checking(*group1)
    except NoDogsAllowedException as e:
        print(e)

    try:
        checking(*group2)
    except NoDogsAllowedException as e:
        print(e)