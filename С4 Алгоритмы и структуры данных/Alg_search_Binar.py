def binary_search(array, element, left, right):
    if left > right: #Если левая граница превысила правую, то
        return False # эл-т отсутствует
    middle = (left + right) // 2 #находим индекс середины массива

    if array[middle] == element: #Если эл-т находися по середине
        return middle #то возвращаем индекс середины
    elif element < array[middle]: #Если элемент меньше элемент по середине
        return binary_search(array, element, left, middle + 1) #то рекурсивно вызываем поиск в первой(левой)
        # половине массива
    else: # Иначе вызываем поиск в правой половине
        return binary_search(array, element, middle + 1, right) #

element = int(input()) # Вызываем ввод искомого эл-та
array = [i for i in range(1,100)] #Генерируем список

print(binary_search(array,element,0,99))