def sort_grades(list):
    list.sort()
    return list[::-1]

print(sort_grades(["A", "B", "C", "C", "F", 'A']))


s1 = 'hello'
s2 = 'hello'

t1 = (1, 2, 'a')
t2 = (1, 2, 'a')
print(id(s1) == id(s2))
print(id(t1) == id(t2))