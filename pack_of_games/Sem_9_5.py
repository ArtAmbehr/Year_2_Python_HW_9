# Объедините функции из прошлых задач.
# Функцию угадайку задекорируйте:
# ○ декораторами для сохранения параметров,
# ○ декоратором контроля значений и
# ○ декоратором для многократного запуска.
# Выберите верный порядок декораторов.


from Sem_9_2 import guess_number as function_, control_game as control
from Sem_9_3 import decor as save_param
from Sem_9_4 import count as counter

NUM = 101
TRY_NUM = 11
COUNT = 3


@counter(COUNT)
@save_param
@control
def decorate_game(num, attempts):
    return function_(num, attempts)


if __name__ == "__main__":
    decorate_game(NUM, TRY_NUM)
    