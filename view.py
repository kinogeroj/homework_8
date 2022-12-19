# Модуль для ввода/вывода информации

import os

def choose() -> str:

    """"Выбор режима работы приложения."""

    os.system('cls')

    print('\n              Меню калькулятора\n' +
          '-------------------------------------------------\n' +
          'Введите 1, 2, 3, 4 или 5:\n\n' +
          'Введите 1, чтобы решить арифметическое уравнение.\n' +
          'Введите 2, чтобы решить квадратное уравнение.\n' +
          'Введите 3, чтобы упростить многочлен.\n' +
          'Введите 4, чтобы отобразить историю операций.\n' +
          'Введите 5, чтобы выйти из калькулятора.\n' +
          '-------------------------------------------------')

    choice = input('Введите пункт меню: ')

    return choice

def get_expr() -> str:

    """"Запрашивает у пользователя задачу."""
    
    print()

    expr = input('Введите данные для вычисления: ')

    return expr

def show_res(result: str) -> str:

    """Выводит результат."""

    print()

    print(f'Результат вычислений равен: {result}')

    print()

def erorr_mode() -> str:

    """Выводит сообщение об ошибке выбора режима."""

    print()

    print('Что-то пошло не так...')

    print()

def show_history(history: str) -> str:
    
    """Выводит истроию оперций."""
    
    if history == None:
        
        print()
    
    else:
        print()
        
        print('История операций:')
        
        print(history)