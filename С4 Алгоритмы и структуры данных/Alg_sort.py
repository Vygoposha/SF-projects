# Сортировка выбором
array = [2, 3, 1, 4, 6, 5, 9, 8, 7] #Создаем массив

# count = 0
# for i in range(len(array)): #В цикле проходим весь массив
#     index_min = i # выбираем предположительно минимальный элемент
#     for j in range(i,len(array)): # в цикле проходим массив от мин эл-та до конца массива
#         if array[j] < array[index_min]: # если эл-т из массива меньше минимального эл-та
#             index_min = j # то присваиваем новый индекс мин эл-та
#         count += 1
#     if i != index_min: # если индекс не совпадает с теущим, то меняем значение
#         array[i], array[index_min] = array[index_min], array[i] #
#
# print(count)
# print(array)
#
# #По убыванию
# count = 0
# for i in range(len(array)): #В цикле проходим весь массив
#     index_max = i # выбираем предположительно максимальный элемент
#     for j in range(i,len(array)): # в цикле проходим массив от максимального эл-та до конца массива
#         if array[j] > array[index_max]: # если эл-т из массива боьше макс эл-та
#             index_max = j # то присваиваем новый индекс макс эл-та
#         count += 1
#     if i != index_max: # если индекс не совпадает с теущим, то меняем значение
#         array[i], array[index_max] = array[index_max], array[i] #
#
# print(count)
# print(array)
#
#Сортировка пузырьком
# for i in range(len(array)): #внешний цикл прохоходит по всем эл-м массива
#     for j in range(len(array)-i-1): #внутренний цикл без учета первого элемента
#         if array[j] > array[j+1]: #сравнивает два соседних элемента
#             array[j], array[j+1] = array[j+1], array[j] # Если тру, то меняет их местами
# print(array)

# #Сортировка вставками
# for i in range(1, len(array)): #итерируем в диапазоне от 1 до конца массива
#     current = array[i] #в переменную сохраняем ведущий элемент(по умолчанию первый в массиве)
#     id_current = i #индекс ведущего эл-та
#     while array[id_current - 1] > current and id_current > 0: #пока вед эл-т меньше эл-та слева
#     и индекс внутри диапазона
#         array[id_current] = array[id_current - 1]
#         id_current -= 1 #шаг цикла, сдвиг эл-та вправо
#     array[id_current] = current #сохраняем значение для слеющей итерации и

#Сортировка слиянием
# def merge_sort(L): #функция разделения массива
#     if len(L) < 2: # Если размер массива меньше 2
#         return L[:] # то возвращаем массив и выходим из рекурсии
#     else:
#         middle = len(L)//2 # Делим массив на 2 части, находим середину массив
#         left = merge_sort(L[:middle])  # Рекурсивно вызываем функцию разделения для левой части массива
#         right = merge_sort(L[middle:])  # Рекурсивно вызываем функцию разделения для правой части массива
#         return merge(left, right)  # возвращаем фукцию слияния
#
# def merge(left,right):
#     result = []  # Создаем пустой массив, куда будут записаны сортированный эл-ты
#     i,j = 0,0  # начальные индексы для сортировки, указатели
#     while i < len(left) and j < len(right):  # условие, что индексы не выйдут за границы левого и правого массивов
#         if left[i] < right[j]:  # если элемент в левом массиве < чем в правом,
#             result.append(left[i])  # то он записывается в рзультирующий массив
#             i += 1  # индекс сдвигается на следющий эл-т
#         else:
#             result.append(right[j])  # иначе в резльтирующий массив записывает правый эл-т
#             j += 1  # индекс сдвигается на следющий эл-т
#
#     while i < len(left):
#         result.append(left[i])
#         i += 1
#
#     while j < len(right):
#         result.append(right[j])
#         j += 1
#
#     return result
#
# print(merge_sort(array))

#Быстрая сортировка
import random

def qsort(array, left, right):
    #middle = (left + right) // 2  # Находим середину массива
    #p = array[middle]  #
    p = random.choice(array[left:right + 1])
    i,j = left, right  #
    while i <= j:  #
        while array[i] < p:  #
            i += 1  #
        while array[j] > p:  #
            j -= 1  #
        if i < j: #
            array[i], array[j] = array[j], array[i]  #
            i += 1  #
            j -= 1  #
    if j > left:
        qsort(array, left, j)
    if right > i:
        qsort(array, i, right)

print(qsort(array, 1, 8))