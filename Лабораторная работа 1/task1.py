numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
summ = sum(num for num in numbers if num is not None)
numofdig = len(numbers)
aver = summ/numofdig
numwithrep = [num if num is not None else aver for num in numbers]
print("Измененный список:", numwithrep)

