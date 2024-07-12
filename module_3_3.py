# Функция с параметром по умолчанию:

def print_params(a = 1, b = 'string', c = True):
    print (a, b, c)

print_params()
print_params(2)
print_params(3, 'calls')
print_params(5, 'phone', False)
print_params(b = 25)
print_params(c = [1,2,3])

# Распаковка параметров:

value_list = [15, 'StarWars', True]
value_dict = {'a': 23, 'b': "book", 'c': 5.2}

print_params(*value_list)
print_params(**value_dict)

# Распаковка + отдельные параметры:

values_list_2 = [3.7, 'Ship']

print_params(*values_list_2, 42)
