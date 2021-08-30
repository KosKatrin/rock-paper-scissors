import random
import enum

# Привязываем каждое действие пользователя к числу
class Action(enum.IntEnum):
    камень = 0  # камень
    ножницы = 1  # ножницы
    бумага = 2  # бумага

# Функция не принимает никаких аргументов и возвращает выбор пользователя
def get_user_choice():
    while True:  # проверка "на дурака"
        try:
            user_input = input( '\n''Выбери камень [0], ножницы [1] или бумага [2]: ')
            user_choice = int(user_input)
            action = Action(user_choice)
            return action
        except ValueError:
            range_string = f'[0, {len(Action)} -1]'
            print('Некорректный ввод.')
            continue

# Функция возвращает действие, связанное со случайным числом
def get_computer_choice():
    computer_choice = random.randint(0, len(Action) - 1)  # Значения Action начинаются с 0, а счет len() с 1, вычитаем единицу из len(Action)  
    action = Action(computer_choice)
    return action

# Выводим на экран выбор пользователя и компьютера
def print_choices(user_choice, computer_choice):
    print(f'Вы выбрали {user_choice.name}')
    print(f'Компьютер выбрал {computer_choice.name}')

# Определяем победителя
def who_win(user_choice, computer_choice):
    if user_choice == computer_choice:
        print('Ничья!')
    elif user_choice == 0 and computer_choice == 1 or  user_choice == 1 and computer_choice == 2 or user_choice == 2 and computer_choice == 0 :  # камень
        print('Вы победили.')
    else:
        print('Вы проиграли.')

# Играем снова
def play_again():
    while True:
        question = input('\n''Сыграем еще раз? - Да / Нет: ')
        if not question or question.lower() in ('да', 'lf', 'yes'):
            return True
        elif question.lower() in ('нет', 'ytn', 'no'):
            return False
        else:
            print("Пожалуйста, введите 'да' или 'нет'")

# Вызов функций
print('Привет! Ты попал в игру "Камень-ножницы-бумага". Давай начем!')

user_choice = get_user_choice()
computer_choice = get_computer_choice()
print_choices(user_choice, computer_choice)
who_win(user_choice, computer_choice)

while play_again():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print_choices(user_choice, computer_choice)
    who_win(user_choice, computer_choice)



