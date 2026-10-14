# Подключение библиотеки для генерации случайных чисел
import random

# Пользовательский выбор - решение какой задачи необходимо проверить
choice = int(input("Выберите, какой результат будем проверять (1 задача, 2 задача или 3 задача)"))

# Функция, которая определяет тип сортировки через сравнение 2 элементов массива - первый и последний
def typeSort(arr) : 
    if arr[0] > arr[len(arr) - 1] : 
        print("Массив " + str(arr) +  " отcортирован по-убыванию")
    else :
        print("Массив " + str(arr) +  " отcортирован по-возрастанию")

# Функция, которая преобразует строки файла в числовой массив
def fileAppendArray(path) :
    arr = []
    for lineArray in path :
        arr.append(int(lineArray))
    print(arr)
    typeSort(arr) # Вызов функции - тип сортировки

# Функция для вызова сортировки методом пузырька
def bubbleSort() :
    # Открываем файл с отсортированными элементами из первой задач
    fileArray = open("../1/output.txt", "r")
    fileAppendArray(fileArray)

# Функция для вызова сортировки методом подсчета
def countSort() :
    # Открываем файл с отсортированными элементами из второй задач
    fileArray = open("../2/output.txt", "r")
    fileAppendArray(fileArray)

# Функция для вызова сортировки встроенными методами
def standartSort() : 
    # Генерация массива случайным образом
    arr = [random.randint(1, 10) for randomEl in range(7)]
    # Обратная сортировка  
    arr.sort(reverse=True)
    typeSort(arr)

# Проверка на корректный ответ пользователя
order = False
while not order: 
    if choice == 1 :
        print("Вы выбрали сортировку методом пузырьки")
        bubbleSort()
        order = True
    elif choice == 2 :
        print("Вы выбрали сортировку методом подсчета")
        countSort()
        order = True
    elif choice == 3 :
        print("Вы выбрали сортировку методом sort")
        standartSort()
        order = True
    else :
        choice = int(input("Выберите, существующую задачу"))
        order = False
    
    