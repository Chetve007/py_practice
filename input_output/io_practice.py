import sys

_file_obj = None


def capture_output(file='capture_file.txt'):
    """
        capture_output - перенаправление стандартного
        вывода в файл указанаыый в аргументах функции
    """
    global _file_obj
    print(f'output will be sent to file: {_file_obj}')
    print("restore to normal by calling 'io.practice.restore_output()'")
    _file_obj = open(file, 'w')
    sys.stdout = _file_obj


def restore_output():
    """"
        Восстановление стандартного вывода
        по умолчанию (также закрывает файл сохранения)
    """
    global _file_obj
    sys.stdout = sys.__stdout__
    _file_obj.close()
    print('standard output has been restored back to normal')


def print_file(file='capture_file.txt'):
    """передача заданного файла (из аргументов ф-ии) в стандартный вывод"""
    f = open(file)
    print(f.read())
    f.close()


def clear_file(file='capture_file.txt'):
    """очистка содержимого заданного файла (из аргументов ф-ии)"""
    f = open(file, 'w')
    f.close()
