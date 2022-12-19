# Модуль для выполнения операций

import sympy

x = sympy.Symbol('x')

def execute_expr(expr: str) -> str:
    
    """Принимает на вход строку-пример. Возвращает результат примера."""

    result = sympy.nsimplify(expr)

    return result

def solve_eq(expr: str) -> str:
 
    """Принимает на вход уравнение в виде строки. Возвращает список корней уравнения в строку с разделителем."""
    
    try:
        
        result = sympy.solve(expr, x)

        return result
    
    except ValueError:

        print('Неправильные вводные данные.')

def simpify_pol(expr: str) -> str:

    """"Упрощает введенный многочлен."""

    result = sympy.simplify(expr)

    return result