class Node: #класс элемента
    def __init__(self, value = None, next_ = None): #Инициализция
        self.value = value #значение
        self.next_ = next_ #ссылка на следующий элемент

    def __str__(self):
        return f"Node value = {str(self.value)}"

class LinkedList: #класс связанного списка
    def __init__(self): #инициализируем пустой список
        self.first = None
        self.last = None

    def clear(self): #очищает список
        self.__init__()

    def __str__(self): #функция печати
        R = ''

        pointer = self.first #Берем первый указатель
        while pointer is not None:
            R += str(pointer.value) #Добавляем занчение в строку
            pointer = pointer.next_ #Идем дальше по указателю
            if pointer is not None: #Если указатель существует, то добавляем пробел
                R += ' '
        return R

    def pushleft(self, value): #метод, к-ый вставляет эл-т в начало списка
        if self.first is None: # если первого элемента не существует, то
            self.first = Node(value) # присваиваем ему значение класса элемента
            self.last = self.first # т.к. элемент в списке один, то он становится первым и последним одновременно
        else:
            new_Node = Node(value, self.first) # Если эл-т сущетсвует, то создаем новый эл-т и
            self.first = new_Node # переопределяем занчение 1го эл-та

    def pushright(self, value):
        if self.first is None:
            self.first = Node(value)
            self.last = self.first
        else:
            new_Node = Node(value)
            self.last.next_ = new_Node
            self.last = new_Node

    def popleft(self):
        if self.first is None: # Если список пустой, то возвращаем None
            return None
        elif self.first == self.last: # Если в списке только один э-т, то
            node = self.first # сохраняем его
            self.__init__() # очищаем список
            return node # возвращаем сохраенынй эл-т
        else:
            node = self.first # сохраняем в переменную первый(левый) эл-т
            self.first = self.first.next_ # Меняем указатель первого эл-то на новый первый эл-т
            return node #возвращем сохраненный эл-т

    def popright(self):
        if self.first is None:  # Если список пустой, то возвращаем None
            return None
        elif self.first == self.last:  # Если в списке только один э-т, то
            node = self.first  # сохраняем его
            self.__init__()  # очищаем список
            return node  # возвращаем сохраенынй эл-т
        else:
            node = self.last #Сохраняем значение последнего(правого) эл-та
            pointer = self.first #Создаем указатель на первом эл-те
            while pointer.next_ is not node: #пока указатель не найдет значение предпоследний эл-та
                pointer = pointer.next_ # сохраянем указатель на предпоследний эл-т
            pointer.next_ = None
            self.last = pointer # Меняем указатель, чтобы предпоследний эл-т стал последним
            return node

    def __iter__(self): # объявляем класс как генератор
        self.current = self.first # Присваиваем текущему значению первый эл-т из списка
        return self # Возвращаем итератор

    def __next__(self): # Метод перехода
        if self.current is None: # Если текущий эл-т стал последним
            return StopIteration # То вызываем исключение
        else:
            node = self.current #сохраняем текущий эл-то
            self.current = self.current.next_ # переходим на следующий эл-т
            return node # врзвращаем сохраненый

    def __len__(self): # метод взвращающий длину/размер структуры данных
        count = 0 # создаем переменную для подсчета
        pointer = self.first # Ставим указатель на первый эл-т
        while pointer is not None: # пока указатель на существующем эл-те
            count +=1 # увеличиваем счетчик
            pointer = pointer.next_ # сдвигаем указатель на следующий эл-т
        return count #возвращаем значение

LL = LinkedList()

LL.pushright(1)
print(LL)
LL.pushleft(2)
print(LL)
LL.pushright(3)
print(LL)
LL.popright()
print(LL)
LL.pushleft(4)
print(LL)
LL.pushright(5)
print(LL)
LL.popleft()

print(LL)

print(len(LL))