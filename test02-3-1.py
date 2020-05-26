odd = [1, 3, 5, 7, 9]
a = []
b = [1,2,3]
c = ['Life', 'is', 'too', 'short']
d = [1,2,'Life', 'is']
e = [1,2,['Life', 'is']]
a = [1,2,3]
print(a)
print(a[0] + a[2])
print(a[-1])
a = [1,2,3,['a', 'b', 'c']]
print(a[3][0]) 
a = [1, 2, ['a', 'b', ['Life', 'is']]]
print(a[2][2][1])
a = [1, 2, 3, 4, 5]
b = "12345"
print(a[0:2])
print(b[0:2])
a = [1,2,3]
b = [4,5,6]
print(a + b)
a * 3
print(len(a * 3))
a = [1,2,3]
a[2] = 4
print(a)
#append -> 리스트에 요소 추가
a.append(600)
print(a)
a.append([5,9])
print(a)
print(a[4][1])
