

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


search = int(input("Введите число для поиска: "))
arr = list(range(1, 101, 2)) # Список из нечетных чисел
result = linear_search(arr, search)


if result != -1:
    print(f"Элемент найден на позиции: {result}\n")
else:
    print("Нет такого элемента\n")




def bineary_search(arr, target):
    left = 0 
    right = len(arr) - 1 

    while left <= right:
        mid = (left + right) // 2
        print(f"Сравниваем со средним числом: [{mid} = {arr[mid]}]")

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return

arr = list(range(1, 101, 2))# Список из нечетных чисел
target = int(input("Введите число для поиска: "))
result = bineary_search(arr, target)

if result != -1:
    print(f"Элемент найден на позиции: {result}\n")
else:
    print("Элемент не найден\n")





class SearchEngine:
    def __init__(self, data):
        self.data = data

    def linear_search(self, target):
        for i in range(len(self.data)):
            if self.data[i] == target:
                return i
        
        return -1
    
    def bineary_search(self, target):
        left = 0
        right = len(self.data) - 1

        while left <= right:
            mid = (left + right) // 2
            print(f"Сравнение со средним числом: [{mid} = {self.data[mid]}]")

            if self.data[mid] == target:
                return mid
            elif self.data[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
    

arr = list(range(1, 101))
search_engine = SearchEngine(arr)
target = int(input("Введите число для поиска: "))

res1 = search_engine.linear_search(target)
print("Результат линейного поиска: ", res1 if res1 != -1 else 'Нет такого элемента')

res2 = search_engine.bineary_search(target)
print("Резултат бинарного поиска: ", res2 if res2 != -1 else "Нет такого элемента")

    




