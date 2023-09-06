t = (1,2,3,4,1,5,6,1)
print(t)
print(type(t))
print(len(t))
b = t.index(1)
print(b)

# id(c) là địa chỉ của c
c = ('Cong')
print(id(c))


# SET
# {x,y} - {x} = {y} : toán tử trừ
# {x,y} & {x} = {x} : toán tử và : in ra phần tử có cả ở 2 set
# {x,y} | {z} = {x,y,z} : toán tử hoặc : lấy hết phần tử có ở 2 set
# {x,y} ^ {x,z} = {y,z} : toán tử shaw : lấy tất cả phần tử của 2 set trừ những phần tử giống nhau
a = ({1,2,3,4} - {1})
print(a)
# clear(): xoá tất cả phần tử trong set
# pop() : xoá phần tử đầu tiên trong set
# remove(x),discard(x) : xoá phần tử x có trong set
# copy() : sao chép set
# add(x) : thêm x vào set ,nếu set đã có x thì bỏ qua
a.discard(3)
print(a)
a.add(9)
print(a)
