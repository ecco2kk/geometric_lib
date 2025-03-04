# **** Лабораторная работа по GIT №2 ****
## Общее описание решения
> В репозитории находятся файлы расширения .py , в каждом ищз который описаны функции нахождения площади и периметра каждой из 4 фигур: треугольника, прямоугольника, квадрата и круга.
## Описание каждой функции с примерами вызова
### triangle.py
- def area(a, h)
```
принимает сторону а и высоту h, возвращает площадь треугольника 
```
> def area(16, 10)
```
output 80
```
- def perimetr(a, b, c)
```
принимает стороны а, b, c , возвращает периметр треугольника 
```
> def perimetr(3, 4, 5)
```
output 12
```
### rectangle.py
-def area(a, b)
```
принимает стороны а и b, возвращает площадь прямоугольника 
```
> def area(5, 10)
```
output 50
```
-def perimetr(a, b)
```
принимает стороны а и b, возвращает периметр прямоугольника 
```
> def perimetr(5, 10)
```
output 30
```
### square.py
-def area(a)
```
принимает сторону а, возвращает площадь квадрата 
```
> def area(4)
```
output 16
```
-def perimetr(a)
```
принимает сторону а, возвращает периметр квадрата 
```
> def perimetr(3)
```
output 12
```
### circle.py
-def area(r)
```
принимает радиус r, возвращает площадь круга 
```
> def area(1)
```
output ~3.14
```
-def perimetr(r)
```
принимает радиус r, возвращает периметр круга 
```
> def area(2)
```
output ~12.57
```
## История изменения проекта с хешами комитов

<img width="510" alt="Снимок экрана 2023-09-27 в 2 20 10 PM" src="https://github.com/ecco2kk/geometric_lib/assets/114879885/ac1e5749-0fab-47b9-a0e7-c72206333bb5">

# **** Лабораторная работа №4. Написание Unit тестов ****
# Описание работы unit-тестов для файла circle.py:
## Тесты для файла circle.py хранятся в файле test_circle.py:
### - Функция `test_area_1()` проверяет корректность работы программы, вычисляющей площадь круга, при вводе валидного значения радиуса круга.
### - Функция `test_area_2()` проверяет корректность работы программы, вычисляющей площадь круга, при вводе нулевого значения радиуса круга.
### - Функция `test_area_3()` проверяет корректность работы программы, вычисляющей площадь круга, при вводе отрицательного значения радиуса круга.
### - Функция `test_area_4()` проверяет корректность работы программы, вычисляющей площадь круга, при вводе строкового значения радиуса круга.
### - Функция `test_area_5()` проверяет корректность работы программы, вычисляющей площадь круга, при вводе булевого значения радиуса круга.
### - Функция `test_perimeter_1()` проверяет корректность работы программы, вычисляющей длину окружности, при вводе валидного значения радиуса круга.
### - Функция `test_perimeter_2()` проверяет корректность работы программы, вычисляющей длину окружности, при вводе нулевого значения радиуса круга.
### - Функция `test_perimeter_3()` проверяет корректность работы программы, вычисляющей длину окружности, при вводе отрицательного значения радиуса круга.
### - Функция `test_perimeter_4()` проверяет корректность работы программы, вычисляющей длину окружности, при вводе строкового значения радиуса круга.
### - Функция `test_perimeter_5()` проверяет корректность работы программы, вычисляющей длину окружности, при вводе булевого значения радиуса круга.


# Описание работы unit-тестов для файла square.py:
## Тесты для файла square.py хранятся в файле test_square.py:
### - Функция `test_area_1()` проверяет корректность работы программы, вычисляющей площадь квадрата, при вводе валидного значения стороны квадрата.
### - Функция `test_area_2()` проверяет корректность работы программы, вычисляющей площадь квадрата, при вводе нулевого значения стороны квадрата.
### - Функция `test_area_3()` проверяет корректность работы программы, вычисляющей площадь квадрата, при вводе отрицательного значения стороны квадрата.
### - Функция `test_area_4()` проверяет корректность работы программы, вычисляющей площадь квадрата, при вводе строкового значения стороны квадрата.
### - Функция `test_area_5()` проверяет корректность работы программы, вычисляющей площадь квадрата, при вводе булевого значения стороны квадрата.
### - Функция `test_perimeter_1()` проверяет корректность работы программы, вычисляющей периметр квадрата, при вводе валидного значения стороны квадрата.
### - Функция `test_perimeter_2()` проверяет корректность работы программы, вычисляющей периметр квадрата, при вводе нулевого значения стороны квадрата.
### - Функция `test_perimeter_3()` проверяет корректность работы программы, вычисляющей периметр квадрата, при вводе отрицательного значения стороны квадрата.
### - Функция `test_perimeter_4()` проверяет корректность работы программы, вычисляющей периметр квадрата, при вводе строкового значения стороны квадрата.
### - Функция `test_perimeter_5()` проверяет корректность работы программы, вычисляющей периметр квадрата, при вводе булевого значения стороны квадрата.

# Описание работы unit-тестов для файла rectangle.py:
## Тесты для файла rectangle.py хранятся в файле test_rectangle.py:
### - Функция `test_area_1()` проверяет корректность работы программы, вычисляющей площадь прямоугольника, при вводе валидного значения сторон прямоугольника.
### - Функция `test_area_2()` проверяет корректность работы программы, вычисляющей площадь прямоугольника, при вводе нулевого значения хотя бы одной из сторон прямоугольника.
### - Функция `test_area_3()` проверяет корректность работы программы, вычисляющей площадь прямоугольника, при вводе отрицательного значения хотя бы одной из сторон прямоугольника.
### - Функция `test_area_4()` проверяет корректность работы программы, вычисляющей площадь прямоугольника, при вводе строкового значения хотя бы одной из сторон прямоугольника.
### - Функция `test_area_5()` проверяет корректность работы программы, вычисляющей площадь прямоугольника, при вводе булевого значения хотя бы одной из сторон прямоугольника.
### - Функция `test_perimeter_1()` проверяет корректность работы программы, вычисляющей периметр прямоугольника, при вводе валидного значения сторон прямоугольника.
### - Функция `test_perimeter_2()` проверяет корректность работы программы, вычисляющей периметр прямоугольника, при вводе нулевого значения хотя бы одной из сторон прямоугольника.
### - Функция `test_perimeter_3()` проверяет корректность работы программы, вычисляющей периметр прямоугольника, при вводе отрицательного значения хотя бы одной из сторон прямоугольника.
### - Функция `test_perimeter_4()` проверяет корректность работы программы, вычисляющей периметр прямоугольника, при вводе строкового значения хотя бы одной из сторон прямоугольника.
### - Функция `test_perimeter_5()` проверяет корректность работы программы, вычисляющей периметр прямоугольника, при вводе булевого значения хотя бы одной из сторон прямоугольника.

# Описание работы unit-тестов для файла triangle.py:
## Тесты для файла triangle.py хранятся в файле test_triangle.py:
### - Функция `test_area_1()` проверяет корректность работы программы, вычисляющей площадь треугольника, при вводе валидного значения сторон треугольника.
### - Функция `test_area_2()` проверяет корректность работы программы, вычисляющей площадь треугольника, при вводе нулевого значения хотя бы одной из сторон треугольника.
### - Функция `test_area_3()` проверяет корректность работы программы, вычисляющей площадь треугольника, при вводе отрицательного значения хотя бы одной из сторон треугольника.
### - Функция `test_area_4()` проверяет корректность работы программы, вычисляющей площадь треугольника, при вводе строкового значения хотя бы одной из сторон треугольника.
### - Функция `test_area_5()` проверяет корректность работы программы, вычисляющей площадь треугольника, при вводе булевого значения хотя бы одной из сторон треугольника.
### - Функция `test_perimeter_1()` проверяет корректность работы программы, вычисляющей периметр треугольника, при вводе валидного значения сторон треугольника.
### - Функция `test_perimeter_2()` проверяет корректность работы программы, вычисляющей периметр треугольника, при вводе нулевого значения хотя бы одной из сторон треугольника.
### - Функция `test_perimeter_3()` проверяет корректность работы программы, вычисляющей периметр треугольника, при вводе отрицательного значения хотя бы одной из сторон треугольника.
### - Функция `test_perimeter_4()` проверяет корректность работы программы, вычисляющей периметр треугольника, при вводе строкового значения хотя бы одной из сторон треугольника.
### - Функция `test_perimeter_5()` проверяет корректность работы программы, вычисляющей периметр треугольника, при вводе значений сторон, не удовлетворяющих неравенству треугольника.
### - Функция `test_perimeter_6()` проверяет корректность работы программы, вычисляющей периметр треугольника, при вводе булевого значения хотя бы одной из сторон треугольника.

# Тест-кейсы unittest для файла circle.py
| Номер теста      | Входные данные |    Ожидаемый результат     |   Фактический результат    | Статус  |
|------------------|:--------------:|:--------------------------:|:--------------------------:|---------|        
| 1) area(r)       |     r = 3      |     28.274333882308138     |     28.274333882308138     | Успешно | 
| 2) area(r)       |     r = 0      | "The figure doesn't exist" | "The figure doesn't exist" | Успешно |
| 3) area(r)       |     r = -2     |      'Invalid input'       |      'Invalid input'       | Успешно |
| 4) area(r)       |    r = 'qw'    |      'Invalid input'       |      'Invalid input'       | Успешно |
| 5) area(r)       |    r = True    |      'Invalid input'       |      'Invalid input'       | Успешно |
| 6) perimeter(r)  |     r = 3      |     18.84955592153876      |     18.84955592153876      | Успешно |
| 7) perimeter(r)  |     r = 0      | "The figure doesn't exist" | "The figure doesn't exist" | Успешно |
| 8) perimeter(r)  |     r = -2     |      "Invalid input"       |      "Invalid input"       | Успешно |
| 9) perimeter(r)  |    r = 'qw'    |      "Invalid input"       |      "Invalid input"       | Успешно |
| 10) perimeter(r) |    r = True    |      "Invalid input"       |      "Invalid input"       | Успешно |


# Тест-кейсы unittest для файла square.py
| Номер теста      | Входные данные |    Ожидаемый результат     |   Фактический результат    | Статус  |
|------------------|:--------------:|:--------------------------:|:--------------------------:|---------|        
| 1) area(a)       |     a = 2      |             4              |             4             | Успешно | 
| 2) area(a)       |     r = 0      | "The figure doesn't exist" | "The figure doesn't exist" | Успешно |
| 3) area(a)       |     r = -1     |      'Invalid input'       |      'Invalid input'       | Успешно |
| 4) area(a)       |    r = 'a'     |      'Invalid input'       |      'Invalid input'       | Успешно |
| 5) area(a)       |    r = True    |      'Invalid input'       |      'Invalid input'       | Успешно |
| 6) perimeter(a)  |     r = 4      |             16             |             16            | Успешно |
| 7) perimeter(a)  |     r = 0      |      'Invalid input'       |      'Invalid input'       | Успешно |
| 8) perimeter(a)  |     r = -1    |      'Invalid input'       |      'Invalid input'       | Успешно |
| 9) perimeter(a)  |    r = 'a'     |      'Invalid input'       |      'Invalid input'       | Успешно |
| 10) perimeter(a) |    r = True    |      'Invalid input'       |      'Invalid input'       | Успешно |

# Тест-кейсы unittest для файла rectangle.py
| Номер теста         |   Входные данные    |    Ожидаемый результат     |   Фактический результат    | Статус  |
|---------------------|:-------------------:|:--------------------------:|:--------------------------:|---------|        
| 1) area(a, b)       |    a = 2, b = 0    | "The figure doesn't exist" | "The figure doesn't exist" | Успешно | 
| 2) area(a, b)       |   a = 2, b = 3   |            6            |            6            | Успешно |
| 3) area(a, b)       |   a = 5, b = -1    |      'Invalid input'       |      'Invalid input'       | Успешно |
| 4) area(a, b)       |  a = 'a', b = 10   |      'Invalid input'       |      'Invalid input'       | Успешно |
| 5) area(a, b)       | a = True, b = False |      'Invalid input'       |      'Invalid input'       | Успешно |
| 6) perimeter(a, b)  |    a = 2, b = 0    | "The figure doesn't exist" | "The figure doesn't exist" | Успешно | 
| 7) perimeter(a, b)  |   a = 2, b = 3   |            10             |            10             | Успешно |
| 8) perimeter(a, b)  |   a = 5, b = -1    |      'Invalid input'       |      'Invalid input'       | Успешно |
| 9) perimeter(a, b)  |  a = 'a', b = 10   |      'Invalid input'       |      'Invalid input'       | Успешно |
| 10) perimeter(a, b) | a = True, b = False |      'Invalid input'       |      'Invalid input'       | Успешно |

# Тест-кейсы unittest для файла triangle.py
| Номер теста            |     Входные данные      |    Ожидаемый результат     |   Фактический результат    | Статус  |
|------------------------|:-----------------------:|:--------------------------:|:--------------------------:|---------|        
| 1) area(a, h)          |      a = 2, h = 3       |             3              |             3              | Успешно | 
| 2) area(a, h)          |      a = 0, h = 4       | "The figure doesn't exist" | "The figure doesn't exist" | Успешно |
| 3) area(a, h)          |      a = -1, h = 3      |      'Invalid input'       |      'Invalid input'       | Успешно |
| 4) area(a, h)          |     a = 2, b = 'b'      |      'Invalid input'       |      'Invalid input'       | Успешно |
| 5) area(a, h)          |     a = 3, b = True     |      'Invalid input'       |      'Invalid input'       | Успешно |
| 6) perimeter(a, b, c)  |   a = 3, b = 4, c = 5   |             12             |             12             | Успешно |
| 7) perimeter(a, b, c)  |   a = 0, b = 2, c = 3   | "The figure doesn't exist" | "The figure doesn't exist" | Успешно |
| 8) perimeter(a, b, c)  |  a = -1, b = 2, c = 3   |      'Invalid input'       |      'Invalid input'       | Успешно |
| 9) perimeter(a, b, c)  |  a = -1, b = 'N', c = 3  |      'Invalid input'       |      'Invalid input'       | Успешно |
| 10) perimeter(a, b, c) |  a = 2, b = 13, c = 56  | "The figure doesn't exist" | "The figure doesn't exist" | Успешно |
| 11) perimeter(a, b, c) | a = False, b = 3, c = 5 |      'Invalid input'       |      'Invalid input'       | Успешно |

# Примеры прохождения тестов
## <img width="1326" alt="Снимок экрана 2023-11-13 в 10 21 20 PM" src="https://github.com/ecco2kk/geometric_lib/assets/114879885/a9eae47b-039b-4be9-8490-e8eb0f3cb4f7">
## <img width="1326" alt="Снимок экрана 2023-11-13 в 10 23 24 PM" src="https://github.com/ecco2kk/geometric_lib/assets/114879885/1cb3acf7-5474-4b82-8b90-49fce7c571f3">
## <img width="1326" alt="Снимок экрана 2023-11-13 в 10 26 17 PM" src="https://github.com/ecco2kk/geometric_lib/assets/114879885/770339a7-af36-4f0c-8429-8c1f8f863c0a">

# История изменений в проекте 
## <img width="563" alt="Снимок экрана 2023-11-13 в 7 53 02 PM" src="https://github.com/ecco2kk/geometric_lib/assets/114879885/5b71a097-868d-4dda-9b5a-1a18350bc97b">
## <img width="883" alt="Снимок экрана 2023-11-13 в 10 02 15 PM" src="https://github.com/ecco2kk/geometric_lib/assets/114879885/5ca9fcb4-d6af-49d7-a0f7-10d3c30bd111">


