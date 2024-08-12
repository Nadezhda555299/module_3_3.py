# 1. Функция с параметрами по умолчанию:
def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(303, 'apple', False)
print_params(101, 'banana')
print_params(b='peach')
print_params(b=25)
print_params(c=[1, 2, 3])

# 2. Распаковка параметров:
values_list = [100, 'first', False]
values_dict = {'a': 200, 'b': 'стол', 'c': True}
print_params(*values_list)
print_params(**values_dict)

# 3. Распаковка + отдельные параметры:
values_list_2 = [54.34, 'chars']
print_params(*values_list_2, 42)
