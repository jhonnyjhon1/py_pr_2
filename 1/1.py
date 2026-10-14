# Пузырьковая сортировка

# Исходный список расположен в файле input.txt 
fileArray = open("input.txt", "r")

arr = []

for lineArray in fileArray :
    arr.append(int(lineArray))

count = len(arr)
order = False
while not order :
    order = True
    for i in range(count - 1) : 
        if arr[i] > arr[i+1] :
            # print(arr[i], arr[i+1])
            arr[i],arr[i+1] = arr[i+1],arr[i]
            order = False
            # print(arr[i], arr[i+1])
        # print(arr)
    count -=1 

# Вывод отсортированный список в файл output.txt
fileArray = open("output.txt", "w")
for i in range(count) :
    fileArray.write(str(arr[i]) + '\n')

fileArray.close()