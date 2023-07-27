# Напишите функцию принимающую на вход только ключевые параметры
# и возвращающую словарь, где ключ — значение переданного аргумента,
# а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление.
# Пример: rev_kwargs(res=1, reverse=[1, 2, 3]) -> {1: 'res', '[1, 2, 3]': 'reverse'}

def key_args_dict(**kwags) -> dict:
    result_dict = {}
    for key, value in kwags.items():
        if isinstance(value, (list, set, dict)):
            value_str = str(value)
            result_dict[value_str] = key
        else:
            result_dict[value] = key

    return result_dict


my_dict = key_args_dict(res=1, reverse=[1, 2, 3])
print(my_dict)