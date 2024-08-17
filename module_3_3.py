def print_params(a=1, b='строка', c=True):
    """Функция для вывода параметров."""
    print(a, b, c)

# 1. Вызовы функции с разным количеством аргументов
print_params()  # Вывод: 1 строка True
print_params(10)  # Вывод: 10 строка True
print_params(10, 25)  # Вывод: 10 25 True
print_params(b=25)  # Вывод: 1 25 True
print_params(c=[1, 2, 3])  # Вывод: 1 строка [1, 2, 3]

# 2. Распаковка параметров из списка и словаря
values_list = [42, 'текст', False]
values_dict = {'a': 3.14, 'b': 'новая строка', 'c': None}

# Вызов функции с распаковкой параметров
print_params(*values_list)  # Вывод: 42 текст False
print_params(**values_dict)  # Вывод: 3.14 новая строка None

# 3. Распаковка + отдельные параметры
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)  # Вывод: 54.32 Строка 42