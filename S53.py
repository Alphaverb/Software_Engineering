from math import sqrt

one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

def min_triangle(list):
    min_element = min(list)
    return min_element

def max_triangle(list):
    max_element = max(list)
    return max_element

def triangle_area(a, b, c):
    s = (a + b + c) / 2
    area = sqrt(s * (s - a) * (s - b) * (s - c))
    return area

area_min = triangle_area(min_triangle(one), min_triangle(two), min_triangle(three))
area_max = triangle_area(max_triangle(one), max_triangle(two), max_triangle(three))
print("Площадь треугольника из минимальных значений:", area_min, "\nMin:", min_triangle(one), min_triangle(two), min_triangle(three),
      "\nПлощадь треугольника из максимальных значений:", area_max, "\nMax:", max_triangle(one), max_triangle(two), max_triangle(three))
