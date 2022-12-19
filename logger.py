# Модуль для записи резуьтатов вычислений

file_name = 'log.txt'

def log_exec(expr: str, result: str) -> str:
    
    """Записывает в файл результат вычислений в виде |задача -> ответ|."""
    
    log = ('[' + str(expr) + ' -> ' + str(result).replace('[]', '') + ']\n')

    with open('log.txt', 'a', encoding = 'utf-8') as f:
        f.writelines(log)


def get_history() -> str:
    
    """"Возвращает содержимое файла с результатами вычислений."""
    
    with open('log.txt', 'r', encoding='utf-8') as f:
        file_contents = f.read()

        if len(file_contents) == 0:
            
            print('Список операций пуст!')
        
        else:
            
            return file_contents