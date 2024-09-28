
def main(input_text):
    # Допустимые числа
    valid_numbers = range(1, 11)

    # Разбор строки на составляющие
    parts = input_text.split()

    try:
        a, operator, b = parts
    except:
        raise Exception('throws Exception //т.к. строка не является математической операцией')

    if len(parts) > 3:
        raise Exception('throws Exception //т.к. формат математической операции не удовлетворяет заданию - два операнда и один оператор (+, -, /, *)')


    try:
        a = int(a)
        b = int(b)
    except ValueError:
        raise ValueError("Введены некорректные числа. Ожидаются целые числа от 1 до 10 включительно.")

    if a not in valid_numbers or b not in valid_numbers:
        raise ValueError("Числа должны быть в диапазоне от 1 до 10 включительно.")

    # Выполнение операции
    if operator == '+':
        result = a + b
    elif operator == '-':
        result = a - b
    elif operator == '*':
        result = a * b
    elif operator == '/':
        result = a // b  # Целочисленное деление
    else:
        raise ValueError("throws Exception //т.к. строка не является математической операцией")

    return result


# Примеры использования
try:
    expression = input("Введите выражение (например, '2 + 3'): ")
    print("Результат:", main(expression))
except ValueError as e:
    print("throws Exception :", e)
