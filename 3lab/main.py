"""
Вариант 3(так как 8 нет).
"""
class Student:
    students_quantity = 0

    def __init__(self, name: str, course: int, grades: dict):
        self.name = name
        self.course = course
        self.grades = grades  # Формат: {'Математика': [5, 4, 5], ...}
        
        Student.students_quantity += 1

    def is_honors_student(self) -> bool:
        """
        Проверяет, является ли студент отличником (средний балл > 8.5).
        """
        total_sum = 0
        total_count = 0
        
        for subject_grades in self.grades.values():
            if subject_grades:
                total_sum += sum(subject_grades)
                total_count += len(subject_grades)
        
        if total_count == 0:
            return False
            
        overall_avg = total_sum / total_count
        print(f"\n📊 Общий средний балл по всем предметам: {overall_avg:.2f}")
        return overall_avg > 8.5

    def avg_score_by_subject(self, subject: str):
        """
        Возвращает средний балл по конкретному предмету.
        """
        # Ищем предмет, игнорируя регистр (математика == Математика)
        found_key = None
        for key in self.grades.keys():
            if key.lower() == subject.lower():
                found_key = key
                break
        
        if found_key:
            scores = self.grades[found_key]
            return sum(scores) / len(scores)
        else:
            return None


def get_valid_number(prompt, error_msg="Введите число!"):
    """Вспомогательная функция для безопасного ввода чисел."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(error_msg)

def create_student_from_input():
    """Функция для ручного ввода данных о студенте."""
    print("\n--- СОЗДАНИЕ НОВОГО СТУДЕНТА ---")
    name = input("Введите имя студента: ").strip()
    course = get_valid_number("Введите номер курса: ")
    
    grades_dict = {}
    print("Далее вводите предметы и оценки. Напишите 'стоп' вместо названия предмета для завершения.")
    
    while True:
        subject = input("\nВведите название предмета (или 'стоп'): ").strip()
        if subject.lower() == 'стоп':
            break
        if not subject:
            print("Название предмета не может быть пустым.")
            continue
            
        # Ввод оценок строкой
        while True:
            grades_str = input(f"Введите оценки по предмету '{subject}' через пробел (например: 9 8 10): ")
            try:
                # Превращаем строку "5 4 5" в список чисел [5, 4, 5]
                grades_list = [int(x) for x in grades_str.split()]
                if not grades_list:
                    print("Список оценок пуст. Введите хотя бы одну оценку.")
                    continue
                grades_dict[subject] = grades_list
                break
            except ValueError:
                print("Ошибка! Вводите только целые числа через пробел.")
    
    return Student(name, course, grades_dict)


# --- ГЛАВНЫЙ БЛОК ВЫПОЛНЕНИЯ ---
if __name__ == "__main__":
    current_student = None

    while True:
        print("\n=== ГЛАВНОЕ МЕНЮ ===")
        print("1. Создать/Перезаписать студента")
        print("2. Показать информацию о текущем студенте")
        print("3. Проверить, отличник ли студент (Avg > 8.5)")
        print("4. Узнать средний балл по конкретному предмету")
        print("5. Выход")
        
        choice = input("Выберите действие (1-5): ")

        if choice == "1":
            current_student = create_student_from_input()
            print("✅ Студент успешно создан!")

        elif choice == "2":
            if current_student:
                print(f"\n📁 ДОСЬЕ:")
                print(f"Имя: {current_student.name}")
                print(f"Курс: {current_student.course}")
                print("Оценки:")
                for subj, grades in current_student.grades.items():
                    print(f" - {subj}: {grades}")
                print(f"Всего студентов создано за сеанс: {Student.students_quantity}")
            else:
                print("⚠️ Сначала создайте студента (пункт 1).")

        elif choice == "3":
            if current_student:
                is_honors = current_student.is_honors_student()
                if is_honors:
                    print("🏆 РЕЗУЛЬТАТ: Студент попадает в список лучших!")
                else:
                    print("📉 РЕЗУЛЬТАТ: Студент не дотягивает до списка лучших.")
            else:
                print("⚠️ Сначала создайте студента (пункт 1).")

        elif choice == "4":
            if current_student:
                if not current_student.grades:
                    print("У студента нет предметов.")
                else:
                    print(f"Доступные предметы: {', '.join(current_student.grades.keys())}")
                    subj_query = input("Введите название предмета: ")
                    avg = current_student.avg_score_by_subject(subj_query)
                    if avg is not None:
                        print(f"Средний балл по '{subj_query}': {avg:.2f}")
                    else:
                        print(f"❌ Предмет '{subj_query}' не найден.")
            else:
                print("⚠️ Сначала создайте студента (пункт 1).")

        elif choice == "5":
            print("Программа завершена.")
            break
        else:
            print("Неверный выбор, попробуйте снова.")