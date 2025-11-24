import sys

# --- РЕШЕНИЕ ВАРИАНТА 8 ---

def task_1_palindrome():
    """1. Проверка, является ли строка палиндромом."""
    print("\n--- Задание 1: Палиндром ---")
    text = "Топот"  # Пример строки
    # Приводим к нижнему регистру и сравниваем с перевернутой строкой
    is_pal = text.lower() == text[::-1].lower()
    
    print(f"Строка: '{text}'")
    if is_pal:
        print("Результат: Это палиндром")
    else:
        print("Результат: Не палиндром")

def task_2_starts_with_a():
    """2. Вывод строк, начинающихся с буквы 'А'."""
    print("\n--- Задание 2: Слова на букву 'А' ---")
    words = ["Арбуз", "Банан", "Акула", "Груша", "Ананас", "Киви"]
    
    # Используем списковое включение и метод startswith
    result = [word for word in words if word.startswith("А")]
    
    print(f"Исходный список: {words}")
    print(f"Результат: {result}")

def task_3_divisors_dict():
    """3. Словарь: число -> количество делителей."""
    print("\n--- Задание 3: Словарь делителей ---")
    N = 10
    divisors = {}
    
    for num in range(1, N + 1):
        count = 0
        # Вложенный цикл для подсчета делителей
        for i in range(1, num + 1):
            if num % i == 0:
                count += 1
        divisors[num] = count
        
    print(f"Число N = {N}")
    print(f"Словарь (число: кол-во делителей): {divisors}")

def task_4_odd_numbers():
    """4. Вывод всех нечётных чисел от 1 до N."""
    print("\n--- Задание 4: Нечётные числа ---")
    N = 15
    # range(start, stop, step) - шаг 2 позволяет брать нечетные
    odd_nums = list(range(1, N + 1, 2))
    
    print(f"N = {N}")
    print(f"Нечётные числа: {odd_nums}")

def task_5_min_element():
    """5. Минимальный элемент списка и его индекс."""
    print("\n--- Задание 5: Минимум и индекс ---")
    numbers = [45, 12, 88, 3, 19, 100]
    
    min_val = min(numbers)
    min_idx = numbers.index(min_val)
    
    print(f"Список: {numbers}")
    print(f"Минимальный элемент: {min_val}")
    print(f"Его индекс: {min_idx}")

def task_6_sort_tuple():
    """6. Сортировка кортежа строк по убыванию длины."""
    print("\n--- Задание 6: Сортировка кортежа ---")
    data = ("кот", "электростанция", "дом", "программирование")
    
    # sorted возвращает список, преобразуем обратно в tuple
    # key=len (по длине), reverse=True (по убыванию)
    sorted_data = tuple(sorted(data, key=len, reverse=True))
    
    print(f"Исходный кортеж: {data}")
    print(f"Отсортированный: {sorted_data}")

def task_7_count_a():
    """7. Количество символов 'а' в строке."""
    print("\n--- Задание 7: Подсчет буквы 'а' ---")
    text = "Мама мыла раму, а папа читал газету"
    char = "а"
    
    count = text.count(char)
    
    print(f"Строка: '{text}'")
    print(f"Количество букв '{char}': {count}")

def task_8_remove_duplicates():
    """8. Удалить числа, встречающиеся более одного раза (оставить уникальные)."""
    print("\n--- Задание 8: Удаление повторяющихся чисел ---")
    numbers = [1, 2, 3, 2, 4, 5, 1, 6]
    
    # Оставляем только те, count которых равен 1
    unique_only = [x for x in numbers if numbers.count(x) == 1]
    
    print(f"Исходный список: {numbers}")
    print(f"Уникальные числа: {unique_only}")

def task_9_set_intersection():
    """9. Пересечение двух множеств."""
    print("\n--- Задание 9: Пересечение множеств ---")
    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7, 8}
    
    # Метод intersection или оператор &
    intersect = set_a.intersection(set_b)
    
    print(f"Множество A: {set_a}")
    print(f"Множество B: {set_b}")
    print(f"Пересечение: {intersect}")

def task_10_sum_squares():
    """10. Сумма квадратов чисел от 1 до N."""
    print("\n--- Задание 10: Сумма квадратов ---")
    N = 5
    
    total_sum = 0
    for i in range(1, N + 1):
        total_sum += i ** 2
        
    print(f"N = {N}")
    print(f"Сумма квадратов (1^2 + ... + {N}^2): {total_sum}")

# --- ГЛАВНЫЙ БЛОК ЗАПУСКА ---
if __name__ == "__main__":
    print("ЗАПУСК ЛАБОРАТОРНОЙ РАБОТЫ №2 (ВАРИАНТ 8)")
    
    task_1_palindrome()
    task_2_starts_with_a()
    task_3_divisors_dict()
    task_4_odd_numbers()
    task_5_min_element()
    task_6_sort_tuple()
    task_7_count_a()
    task_8_remove_duplicates()
    task_9_set_intersection()
    task_10_sum_squares()
    
    print("\n--- Все задачи выполнены ---")