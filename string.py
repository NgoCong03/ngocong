#import : truy xuất đến thư viện
a = 4

#type : in ra kiểu dữ liệu
print(type(a))

#decimal : chọn bao nhiêu số thập phân
from decimal import*
getcontext().prec = 5
b = Decimal(10)/3
print(b)
print(type(b))

#fractions : phân số
from fractions import*
c = Fraction(6,9)
print(c)
print(type(c))

#complex : số phức (thực + ảo*j)
d = complex(6,5)
print(d)
print(type(d))

#''' str ''' hoặc """ str """ : chuỗi nhiều dòng 
#Alert : \a : phát ra tiếng bíp
#Backspace : \b : đưa con trỏ về lại một khoảng trắng
#Newline : \n : xuống dòng
#Horizontal tab : \t : tạo ra một khoảng trống
#single quote : \' : in ra kí tự '
#double quote : \" : in ra kí tự "
#blackslas : \\ : in ra kí tự \

#có thể cộng chuỗi hoặc nhân chuỗi 

# hàm in : kiểu tra chuỗi B có trong chuỗi A không
A = "NhungyeuCong"
B = "Cong"
C = B in A 
print(C)

#in kí tự ở vị trí [n]
D = A[4]
print(D)

#hàm len() : tính độ dài của chuỗi
print(len(A))
E = A[len(A) - 1]
print(E)

#Cắt chuỗi : (None = 0) 
G = A[5:None:2] # 2 ở đây có nghĩa là bước nhảy
print(G)

#ép kiểu với số
H = float("6.9") + 5
print(H)

#ép kiểu với chuỗi
T = str(65) + "5"
print(T)

#Thay đổi giá trị bất kì của chuỗi
K = "Cong"
K = K[None:1] + "0" + K[2:None]
print(K)

#truyền giá trị vào chuỗi : 
# %s : string
# %r : 
# %d : giá trị của một số (nếu là số thực thì lấy phần nguyên)
# %.nf : phù hợp với số thực (n là bao nhiêu số bạn muốn lấy)
L = 'Cong %s Nhung %s'%('yeu','nhieu')
print(L)

U = '%d %.3f'%(3,8.6543253)
print(U)

#thay thế chuỗi 
p = 'Cong'
q = f'{p} yeu Nhung'
print(q)

k = '1:{},2:{}'.format(6,9)
print(k)
r = '1:{one}, 2:{two}'.format(one = 111, two = 222)
print(r)

#Căn lề : 
# căn giữa : ^n
# căn trái : <n
# căn phải : >n
# center(n,'x') : căn giữa; n là số ô, x là chuỗi cần chèn vào chỗ trống và chỉ được 1 kí tự
# rjust(n,'x') : căn phải
# ljust(n,'x') : căn trái
p = 'Ngo {:-^50} Cong'.format('Thanh')
print(p)
x = 'ngo thanh cong'
r = x.ljust(50,'-')
print(r.upper())

# capitalize : viết hoa chữ cái đầu tiên 
# upper : chuyển hết về chữ hoa
# lower : chuyển hết về viết thường
# swapcase : thường thành hoa, hoa thành thường
# title : viết hoa những chữ cái đầu tiên của từng từ
i = 'ngo thanh cong '
u = i.title()
print(u)

# join(['x']) : chèn vào chuỗi; x là 1 string
# encode() : mã hoá 
# replace('x','y',z) : thay thế chuỗi (x là chuỗi cần thay thế, y là chuỗi thay thế x, z là số lần)
# strip() : loại bỏ 2 đầu của chuỗi 
# rstrip() : cắt bên phải 
# lstrip() : cắt bên trái
v = 'acbNgô Côngbca'
e = v.join(['anh ',' handsome'])
print(e.upper())
print(e.encode())
i = v.replace('ô','o',1)
print(i)
print(v.strip('bac'))

# split('x',y) : loại bỏ phần tử x trong 1 chuỗi, y là số lần cắt
# lsplit('x',y) : cắt từ bên trái qua
# rsplit('x',y) : cắt từ bên phải qua
q = 'Ngo Thanh Cong'
print(q.split('o',1))

# partition('x') : tách kí tự x
print(q.partition('T'))

# count('x',y,z) : đếm kí tự x trong chuỗi, (y,z) là khoảng tìm
print(q.count('n',0,8))

# strartwith('x',y,z) : kiểm tra xem chuỗi có bắt đầu bằng kí tự x không, từ vị trí y đến z
print(q.startswith('N',0,5))

# endwith('x',y,z) : kiểm tra xem chuỗi có kết thúc bằng kí tự x không, từ vị trí y đến z
print(q.endswith('g',0,5))

# find('x') : tìm vị trí của chuỗi
# index('x') : tìm vị trí của chuỗi
# rfind : tìm từ phải qua
# lfind : tìm từ trái qua
print(q.find('g'))

# islower(), isupper() : kiểm tra xem chuỗi có viết thường hết không, có viết hoa hết không
# isdigit() : kiểm tra chuỗi có phải số hết không 
# isspace() : kiểm tra xem chuỗi có phải toàn dấu cách không
print(q.islower())


