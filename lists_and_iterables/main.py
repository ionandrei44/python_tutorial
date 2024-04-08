import functools

students = ["Jack", "Sandy", "Patrick", "David"]
students_tuple = ["Jack", "Sandy", "Patrick", "David"]


students.sort(reverse=True)
sorted_students = sorted(students_tuple)

# print(students)
# print(sorted_students)

students_info = [
    ("Jack", "F", 60),
    ("Sandy", "A", 33),
    ("Patrick", "D", 20),
    ("David", "C", 78),
]

grade = lambda grades: grades[1]

students_info.sort(key=grade)

# print(students_info)

store = [("shirt", 20.00), ("pants", 25.00), ("jacket", 50.00), ("socks", 10.00)]

to_euros = lambda data: (data[0], data[1] * 0.92)

store_euros = list(map(to_euros, store))

# print(store_euros)

friends = [("Rachel", 19), ("Monica", 22), ("Ross", 25), ("Chandler", 17), ("Joey", 14)]

age = lambda data: data[1] >= 18

adults = list(filter(age, friends))

# for i in adults:
#   print(i)

letters = ["H", "E", "L", "L", "O"]
word = functools.reduce(lambda x, y: x + y, letters)

# print(word)

factorial = [5, 4, 3, 2, 1]
result = functools.reduce(lambda x, y: x * y, factorial)

# print(result)

squares = [i * i for i in range(1, 11)]

# print(squares)

students_grades = [100, 90, 80, 70, 60, 50, 40, 30, 0]

passed_students = [i if i >= 60 else "failed" for i in students_grades]

print(passed_students)
