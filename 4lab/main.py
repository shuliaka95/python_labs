import numpy as np
import matplotlib.pyplot as plt

# 1. ГЕНЕРАЦИЯ ДАННЫХ
# Используем интервал X от 0 до 5π (около 15.7)
x = np.linspace(0, 5 * np.pi, 200)

# Функция 1 (Ваша функция из Лабы №1, Вариант 8, при y=x)
# Z1 = cos²x + sin²y + sin²2x - 1  => Z1(x) = sin²2x (Диапазон [0, 1])
def function_lab1_z1(x):
    return np.sin(2 * x) ** 2

# Функция 2 (Контрастная функция для демонстрации twinx)
# Используем Z2'(x) = 5 * x * cos(x) (Диапазон [-78, 78])
def function_contrast_z2(x):
    return 5 * x * np.cos(x) 

y1 = function_lab1_z1(x)
y2 = function_contrast_z2(x)

# 2. СОЗДАНИЕ ГРАФИКА
# Создаем Figure и первую ось (ax1)
fig, ax1 = plt.subplots(figsize=(12, 6))

# Устанавливаем заголовок
fig.suptitle('Вариант 8 (Лаба №1): Функции на двух осях Y', fontsize=16)

# --- Настройка Основной Оси Y (ax1) для Функции 1 (Синус) ---
color_1 = '#0070A8' # Синий
ax1.set_xlabel('X (Радианы)', fontsize=12)
ax1.set_ylabel(r'$\mathcal{Z}_1 = \sin^2(2x)$ (Диапазон [0, 1])', color=color_1, fontsize=12)
line1, = ax1.plot(x, y1, color=color_1, linestyle='-', label=r'$\mathcal{Z}_1$ (Синус)')
ax1.tick_params(axis='y', labelcolor=color_1)
ax1.set_ylim(-0.1, 1.1) 
ax1.grid(True, linestyle=':', alpha=0.6, axis='y') # Сетка только по Y1

# --- Создание Вторичной Оси Y (ax2) с использованием twinx() ---
ax2 = ax1.twinx() 

# --- Настройка Вторичной Оси Y (ax2) для Функции 2 (x*cos(x)) ---
color_2 = '#CC0000' # Красный
ax2.set_ylabel(r'$\mathcal{Z}_2\' = 5x \cos(x)$ (Широкий диапазон)', color=color_2, fontsize=12) 
line2, = ax2.plot(x, y2, color=color_2, linestyle='--', label=r'$\mathcal{Z}_2\'$ (Контрастная)')
ax2.tick_params(axis='y', labelcolor=color_2)
ax2.spines['right'].set_color(color_2)
ax2.spines['left'].set_color(color_1)


# 3. ДОБАВЛЕНИЕ ЛЕГЕНДЫ И АННОТАЦИЙ
# Объединяем легенды с обеих осей
ax1.legend([line1, line2], [r'$\mathcal{Z}_1 = \sin^2(2x)$', r'$\mathcal{Z}_2\' = 5x \cos(x)$'], 
           loc='upper center', bbox_to_anchor=(0.5, 1.15))

# Аннотация для Функция 1 (ax1) - Показываем точку на Z1
ax1.annotate(
    'Периодическая $\mathcal{Z}_1$',
    xy=(np.pi, function_lab1_z1(np.pi)), 
    xytext=(5, 0.7),  
    arrowprops=dict(facecolor=color_1, shrink=0.05, width=1, headwidth=6),
    fontsize=9,
    color='black'
)

# Аннотация для Функция 2 (ax2) - Показываем нарастающую амплитуду
max_index = np.argmax(y2)
ax2.annotate(
    'Нарастание амплитуды $\mathcal{Z}_2\'$',
    xy=(x[max_index], y2[max_index]), 
    xytext=(10, 50), 
    arrowprops=dict(facecolor=color_2, shrink=0.05, width=1, headwidth=6),
    fontsize=9,
    color='black'
)

# Выравнивание макета
fig.tight_layout(rect=[0, 0, 1, 0.95]) # Учитываем суженный макет из-за bbox_to_anchor

# 4. СОХРАНЕНИЕ И ОТОБРАЖЕНИЕ
plt.savefig('twinx_lab3_var8_final.png', dpi=300)
plt.show()