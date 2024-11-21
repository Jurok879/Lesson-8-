# объявляем функцию
def personal_sum(numbers):
# присваеваем переменным значение "0"
    result = 0
    incorrect_data = 0
# перебераем значения "numbers"
    for i in numbers:
# блок проверки на ошибки
        try:
# вычисляем сумму чисел в "numbers"
            result += i
# подсчитываем количество выявленых ошибок "TypeError"
        except TypeError:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы - {i}')
# возвращаем полученный результат в виде кортежа
    return (result, incorrect_data)

# объявляем функцию
def calculate_average(numbers):
# блок проверки на ошибки вычислений
    try:
# обращение за данными к функции "personal_sum()"
        per_sum = personal_sum(numbers)
# подсчитываем среднее арифметическое через индексы кортежа "per_sum"
        avg = per_sum[0] / (len(numbers) - per_sum[1])
# возврат "avg"
        return avg
# обработка ошиибки деления на "0"
    except ZeroDivisionError:
        return 0
# обработка ошибки типа данных
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать