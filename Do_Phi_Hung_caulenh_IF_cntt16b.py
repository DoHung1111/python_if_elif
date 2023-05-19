# Bài 1: Chương trình kiểm tra số chẵn hay lẻ trong Python:
print('>>> Bài 1:')
n = int(input('Nhập n = '))
print(str(n) + ' là số chẵn' if n % 2 == 0 else str(n) + ' là số lẻ')



# Bài 2: Chương trình tìm số lớn nhất trong 3 số bằng Python:
print('>>> Bài 2:')
n = int(input('Nhập vào số lượng phần tử cần kiểm tra = '))
a = []
for i in range(n):
    print('number[', i, '] =', end=" ")
    a.append(int(input()))
print('Số lớn nhất là:', max(a))



# Bài 3: Chương trình in ra các ngày trong tháng bằng Python:
print(">>> Bài 3: ")
month = int(input("Nhập vào một tháng: "))

# hàm tìm năm nhuận
def find_leap_year(year):
    # earth = 1 => năm nhuận
    # earth = 0 => năm không nhuận

    earth = 0
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        earth = 1
    return earth

if month in (1, 3, 5, 7, 8, 10, 12):
    print("Tháng", month, "có 31 ngày")
elif month in (4, 9, 6, 11):
    print("Tháng", month, "có 30 ngày")
elif month == 2:
    year = int(input("Nhập vào năm: "))
    sun = find_leap_year(year)
    if sun == 1:
        print("Tháng", month, "có 29 ngày")
    else:
        print("Tháng", month, "có 28 ngày")
else:
    print("Tháng", month, "không hợp lệ")



'''
Bài 4: Viết chương trình cho người dùng nhập vào một số nguyên n.Nếu n lẻ thì in ra màn hình dòng chữ “Số lẻ”.
Nếu số n chẵn và lớn hơn hoặc bằng 100 thì in ra màn hình dòng chữ “Số chẵn và lớn hơn hoặc bằng 100”,
ngược lại thì in ra dòng chữ “Số chẵn và bé hơn 100”.
'''
print('>>> Bài 4:')
n = int(input('nhập n = '))
phan_tich = ('Số lẻ' if n % 2 == 1 else 'Số chẵn và lớn hơn hoặc bằng 100'
      if n % 2 == 0 and n >= 100 else 'Số chẵn và bé hơn 100')
print(phan_tich)



# Bài 5: Biện luận phương trình bậc nhất ax + b = 0
print('>>> Bài 5:')
print("Cho phương trình ax + b = 0")
a = float(input("Nhập hệ số a = "))
b = float(input("Nhập hệ số b = "))

if a != 0:
    print("Chương trình có nghiệm là x =", -b/a)
    print("<=> " + str(a) + " * " + str(-b/a) + " + " + str(b) + " = 0")
elif b == 0: print("Phương trình có vô số nghiệm")
else: print("Phương trình vô nghiệm")



# Bài 6.  Biện luận phương trình bậc hai ax2+bx+c=0.
print(">>> Bài 6: Phương trình ax2 + bx + c = 0")
from math import sqrt
a = float(input("Nhập hệ số a = "))
b = float(input("Nhập hệ số b = "))
c = float(input("Nhập hệ số c = "))

delta = b * b - 4 * a * c
if delta < 0: print("Phương trình vô nghiệm")
elif delta == 0: print("Phương trình có nghiệm kép x =", -b/(2*a))
else:
    print("Phương trình có 2 nghiệm phân biệt:")
    x1 = (-b + sqrt(delta)) / (2 * a)
    x2 = (-b - sqrt(delta)) / (2 * a)
    print("x1 =", x1)
    print("x2 =", x2)



'''
Bài 7.  Người dùng nhập vào một năm là một số nguyên dương bất kì.
Cho biết năm đó có là năm nhuận hay không?'''
print(">>> Bài 7:")
year = int(input("Nhập vào năm: "))
if sun == 1:
    print("Năm", year, "là năm nhuận")
else:
    print("Năm", year, "là năm không nhuận")



'''
Bài 8: Hãy nhập vào tuổi của một người và đưa ra kết luận
và lứa tuổi của người đó theo quy tắc sau '''
print(">>> Bài 8:")
age = int(input("Nhập tuổi: "))
if age > 0 and age <= 2: print(age, "tuổi là trẻ sơ sinh")
elif age > 2 and age <= 10: print(age, "tuổi là nhi đồng")
elif age > 10 and age <= 17: print(age, "tuổi là vị thành niên")
elif age > 17 and age <= 39: print(age, "tuổi là thanh niên")
elif age > 39 and age <= 50: print(age, "tuổi là trung niên")
else: print(age, "tuổi là cao niên")



''' Bài 9: hãy nhập vào năm sản xuất của một chiếc máy tính,
sau đó đưa ra đề xuất đối máy tính đó theo quy tắc sau '''
print(">>> Bài 9:")
computer = int(input("Tính từ ngày sản xuất máy tính đã được sử dụng được bao nhiêu năm: "))
if computer >= 10 and computer < 15: print("Máy tính cần được bảo trì")
if computer >= 15: print("Máy tính cần thay thế")
else: print("Không có để xuất")



''' Bài 10: Hãy nhập vào một điểm trung bình và xét học bổng đối với
điểm trung bình đó theo quy tắc sau '''
print(">>> Bài 10:")
point = float(input("Nhập điểm trung bình: "))
if point >= 9: print("Học bổng: 5.000.000vnđ")
elif point >= 8 and point < 9: print("Học bổng: 3.000.000vnđ")
elif point >= 7 and point < 8: print("Học bổng: 1.000.000vnđ")
else: print("Học bổng: 0 đồng")



''' Bài 11:
1. Nhập một số N bất kỳ từ bàn phím.
2. N có phải số nguyên không?
3. Kiểm tra tính chẵn lẻ của N.
4. N có phải là số chẵn dương không?
5. N có phải là số lẻ âm không?
6. N có phải là số chính phương không? 
'''
print(">>> Bài 11:")
N = int(input("Nhập N = "))

# hàm dùng để tìm số chính phương
def find_square_number(N):
    # flag = 1 => số chính phương
    # flag = 0 => không phải số chính phương

    flag = 0
    # Tìm số bất kỳ nhỏ hơn hoặc bằng n mà bình phương bằng n
    if any(i ** 2 == N for i in range(N + 1)):
        flag = 1
    return flag

if isinstance(N, int): # kiểm tra N là số nguyên hay số thực
    print(N, "là số nguyên")
    if N % 2 == 0: # nếu N là số chẵn
        print(N, "là số chẵn")
        if N > 0: # nếu N là số chẵn dương
            print(N, "là số chẵn dương")
        else: # nếu N là số âm
            print(N, "không phải là số chẵn dương")
    else: # nếu N là số lẻ
        print(N, "là số lẻ")
        if N > 0: # nếu N là số lẻ dương
            print(N, "là số lẻ dương")
        else: # nếu N là số âm
            print(N, "không phải là số lẻ dương")
else: # nếu N là số thực
    print(N, "không phải là số nguyên")

# tìm số chính phương
check = find_square_number(N)
if check == 1:
    print(N, "là số chính phương")
else:
    print(N, "không phải là số chính phương")



