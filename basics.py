age=18 #integer
name="ankit" #string
weight=20.5 #float
print(age)
print(name)
print(weight)
x=50+60
print(x)
y="good"+"5"
print(y)
is_valid=True
print(is_valid)
x=10
y=20
x,y=y,x
print(x,y)
x=10
print(id(10))
print(id(20))
a=10
b=a
b=20
print(b is a)
x={1,2,3}
print(type(x))
p=[1,2,3]
p[0]=2
print(p)

p.append(4)
print(p)
p.insert(1,4)
print(p)
p.count(1)
print(p)
p.remove(4)
print(p)
p.pop()
print(p)
p.pop(1)
print(p)
del p[1]
print(p)
p.reverse()
print(p)
p.sort()
print(p)

i=(1,3,3)
print(set(i))

s={1,2,3,4,5,6,7,8}
s.add(5)
print(s)
s.update([5,6])
print(s)
s.discard(5)
print(s)
s.remove(4)
print(s)
s.clear()
print(s)