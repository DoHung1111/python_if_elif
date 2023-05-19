'''
1. Hãy nhập vào số n với điều kiện 0<n<100. 
yêu cầu người dùng nhập cho đến khi thỏa mãn điều kiện
'''
print(">>> Bài 1:")
n = int(input("nhập n = "))
if n > 0:
    while n <= 100:
        print("Thỏa điều kiện")
        break 
else: print("Sai điều kiện vui lòng nhập lại n, trong khoảng 0 < n < 100")
print("-------------------------------------")
 


'''
2.  Cho dãy số vô hạn: 50, 51, 53, 56, 60. Hãy in ra số 2019
'''
print(">>> Bài 2:")
# cho dãy số vô hạn 50, 51, 53, 56, 60. Nhập số bất kỳ
print("Nhập số bất kỳ cho n.")
n = int(input("n = "))
c = 1
while n > 0: 
    if c == 2019:
        break
    c += 1
print(c)
print("-------------------------------------")



'''
3.  Yêu cầu
-   In ra các số thứ tự từ 1 đến 100
-   In ra các số từ 100 đến 1
-   Bạn hãy viết chương trình tính tổng của 50 số 1,2,3,…50
-   Bạn hãy viết chương trình tính tổng của 50 số chẵn bắt đầu từ 2

'''
print(">>> Bài 3:")
print("-In ra các số thứ tự từ 1 đến 100")
for a in range(1, 101):
    print(a)
print("-------------------------------------")

print("-In ra các số từ 100 đến 1")
b = 100
while b > 0:
    print(b)
    b -= 1
print("-------------------------------------")

print("-Bạn hãy viết chương trình tính tổng của 50 số 1,2,3,…50")
sum = 0
for int_number in range(1, 51):
    sum += int_number
print("Tổng của 50 số 1,2,3,…50 là: tổng = ", sum)
print("-------------------------------------")

print("-Bạn hãy viết chương trình tính tổng của 50 số chẵn bắt đầu từ 2")
sum_1 = 0
for int_number_1 in range(1, 51):
    if int_number_1 % 2 == 0:
        sum_1 += int_number_1
print("Tổng của 50 số chẵn bắt đầu từ 2 là: tổng = ", sum_1)
print("-------------------------------------")



'''
5.  Viết chương trình tìm tất cả các số chia hết cho 7 nhưng không phải bội số của 5, 
nằm trong đoạn 2000 và 3200 (tính cả 2000 và 3200).
 Các số thu được sẽ được in thành chuỗi trên một dòng, cách nhau bằng dấu phẩy.
'''
print(">>> Bài 5:")
number_list = [] # Tạo một danh sách rỗng để lưu kết quả
for d in range(2000, 3201): # duyệt các số từ 2000 đến 3201
    if (d % 7 == 0) and (d % 5 != 0): # Kiểm tra xem số i có chia hết cho 7 và không phải là bội số của 5 không
        number_list.append(str(d)) # Nếu đúng, thì thêm số i vào danh sách result
print (', '.join(number_list)) 
print("-------------------------------------")



'''
6. Viết một chương trình có thể tính giai thừa của một số cho trước. 
Kết quả được in thành chuỗi trên một dòng, phân tách bởi dấu phẩy. 
Ví dụ, số cho trước là 8 thì kết quả đầu ra phải là 40320.
'''
print(">>> Bài 6:")
so_nguyen = int(input("Nhập vào số nguyên n = "))
dap_an = 1 # tạo một biến chứa đáp án giai thừa 
so_mot = 1
while so_mot <= so_nguyen: 
    dap_an *= so_mot
    so_mot += 1
print(str(so_nguyen) + "! =", dap_an)
print("-------------------------------------")



