# Запрос ввода трех целых чисел
first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
third = int(input("Введите третье число: "))

# Как работает программа:
# Ввод данных: Программа запрашивает у пользователя ввод трех целых чисел и сохраняет их в переменные first, second и third.

# Условная конструкция для проверки количества одинаковых чисел
if first == second == third:  # Все числа равны
    print(3)
elif first == second or first == third or second == third:  # Хотя бы два числа равны
    print(2)
else:  # Все числа разные
    print(0)

# Как работает программа:
# Условия: 
# Первое условие (if): Проверяет, равны ли все три числа. Если это так, выводится 3.
# Второе условие (elif): Проверяет, равны ли хотя бы два числа. Это делается с помощью логического оператора or. Если одно из условий истинно, выводится 2.
# Третье условие (else): Если ни одно из предыдущих условий не выполняется, значит все числа разные, и выводится 0.
