X = int(input())   /// Решение 3-х задач на переменные. Стандартный ввод/вывод
Y = int(input())
print(X*60 + Y) 

a=int(input())
b=int(a/60)
print(b)
print(a-b*60)

x,h,m=int(input()),int(input()),int(input())
X=int(x+(h*60)+m)
H=int(X/60)
M=int(X-(60*H))
print(H)
print(M)
