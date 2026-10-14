# Сортирвка методом подсчет

# Исходный список расположен в файле input.txt 
fileArray = open("input.txt", "r")

arr = []

for lineArray in fileArray :
    arr.append(int(lineArray))

print(arr, max(arr), min(arr))

countNewArray = [0] * (max(arr) - min(arr) + 2)

for elem in arr : 
    # (countNewArray[elem])
    countNewArray[elem] += 1

fileArray = open("output.txt", "w")

# Вывод отсортированный список в файл output.txt
for i in range(1, max(arr) - min(arr) + 2) : 
    for j in range(countNewArray[i]) :
        fileArray.write(str(i) + "\n")

fileArray.close()
