# a.append(x) : thêm x vào list a

a = [1,2,3]
a.append(5)
# in ra phần tử thứ 0 của list a
g = a[0]
print(g) 
print('List sau khi them phan tu 5 : ',a)

# b.insert(x,y) : tại vị trí x thêm phần tử y vào list b

b = [1,2,4,5,4]
b.insert(0,10)
print('List sau khi them phan tu 10 vao vi tri 0 :',b)

# b.pop(x) : lấy phần tử thứ x trong list

c = b.pop(0)
print("List ban dau : ", b)
print('Phan tu lay ra la : ',c)

# b.remove(x) : xoá phần tử x đầu tiên có trong list b

b.remove(4)
print('List sau khi xoa phan tu 4 dau tien trong list : ',b)

# d.reverse() : đảo ngược list d
d = [1,9,3,4,5]
d.reverse()
print(d)

# d.sort(reverse=False) : sắp xếp từ nhỏ đến lớn
# d.sort(reverse=True) : sắp xếp từ lớn đến nhỏ
d.sort(reverse=False)
print(d)

# a.extend(b) : nối list a với list b