# Модуль для выполнения операций

import sympy

x = sympy.Symbol('x')

def execute_expr(expr: str) -> str:         # (5+3)*10 -> 80
    
    """Принимает на вход строку-пример. Возвращает результат примера."""

    answer = sympy.solve(expr)

    return answer

def solve_eq(expr: str) -> str:              # x**3 - 8 = 0 -> "2"
                                             # x**2 - 1 = 0 -> "1,-1"
    """Принимает на вход уравнение в виде строки. Возвращает список корней уравнения в строку с разделителем."""
    
    try:
        
        answer = sympy.solve(expr, x)

        return answer
    
    except ValueError:

        print('Неправильные вводные данные')

def simpify_pol(expr: str) -> str:           # x**2 + 3*x**2 + 4 -> 4*x**2 + 4
    """"Упрощает введенный многочлен"""
    pass
