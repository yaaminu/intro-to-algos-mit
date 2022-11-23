import random
import sorting as sort


arr= [1, 12, 15, 3, -1, 18, 10, 2, 20]

print(arr)
sort.insertion_sort(arr)
print(arr)

arr2 = []

for i in range(1, 30):
    arr2.append(random.randint(-2934, 23483))

print(arr2)
sort.insertion_sort(arr2)
print(arr2)
