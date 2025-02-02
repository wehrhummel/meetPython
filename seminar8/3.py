# Вводится список целых чисел в одну строчку через пробел.
# Необходимо оставить в нем только двузначные числа. Реализовать программу
# с использованием функции filter. Результат отобразить на экране в виде
# последовательности оставшихся чисел в одну строчку через пробел.
#
#
# пример:
# - 8 11 0 -23 140 1 => 11 -23
# import math
num_list = "8 11 0 -23 140"
print(*filter(lambda x: 0 < (abs(int(x)) // 10) < 10, num_list.split()))
print(*filter(lambda x: len(str(abs(int(x)))) == 2, num_list.split())) # вариант от Сердюка С.С.