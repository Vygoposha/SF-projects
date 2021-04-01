def find(array, element): #поиск индекса элемента в массиве
    for i, a in enumerate(array):
        if a == element:
            return i
    return False

# array = list(map(int, input().split()))
# element = int(input())

# print(find(array, element))

def count(array, element): #  подстчет колличества повторений эл-та в массиве
    count = 0
    for i in array:
        if i == element:
            count +=1
        continue
    if count != 0:
        return count
    else: return "Not found"


array = list(map(int, input().split()))
print(array)
element = int(input())

print(count(array, element))