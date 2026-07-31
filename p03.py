"""
Bài 1. Viết chương trình tìm tất cả các số chia hết cho 7 nhưng không phải bội số của 5, nằm trong đoạn 
2000 và 3200 (tính cả 2000 và 3200). Các số thu được sẽ được in thành chuỗi trên một dòng, 
cách nhau bằng dấu phẩy.

"""
def find_numbers_divisible_by_7_not_5(start, end):
    base = 0
    for i in range(start, start + 8):
        if i % 7 == 0:
            base = i
    results = []
    for j in range(base, end + 1, 7):
        if j % 5 == 0:
            continue
        else:
            results.append(j)
    return ", ".join(map(str, results))
# start, end = map(int, input().split())
# print(find_numbers_divisible_by_7_not_5(start, end))


"""
Bài 2. Viết một chương trình có thể tính giai thừa của một số cho trước. Kết quả được in thành chuỗi trên một dòng,
 phân tách bởi dấu phẩy. Ví dụ, số cho trước là 8 thì kết quả đầu ra phải là 40320.

"""

def calculate_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i   
    return factorial
# n = int(input("nhap so nguyen duong: "))
# if n > 0:
#     print(calculate_factorial(n))
# else:
#     print("vui long nhap so nguyen duong") 




""""
Bài 03. Với số nguyên n nhất định, hãy viết chương trình để tạo ra một dictionary chứa (i, i*i) như là số nguyên 
từ 1 đến n (bao gồm cả 1 và n) sau đó in ra dictionary này. Ví dụ: Giả sử số n là 8 thì đầu ra sẽ là:
 {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}.

"""
def dic_double(n):
    dic = {}
    for i in range(1, n + 1):
        dic[i] = i * i #(neu dung lenh dic[i] *= i thi dic ban dau phai co key)
    return dic
# n = int(input())
# print(dic_double(n))

"""
Bài 04. Viết chương trình chấp nhận một chuỗi số, phân tách bằng dấu phẩy từ giao diện điều khiển,
 tạo ra một List và một tuple chứa mọi số.
"""
# numbers = input("nhap chuoi so, phan cach bang dau phay: ").split(",")
# lst = numbers
# tpl = tuple(numbers)
# print("list la: ",lst)
# print("tuple la: ", tpl)

"""
Bài 05. Viết một hàm tính giá trị bình phương của một số.

"""
def gia_tri_binh_phuong(n):
    return n*n
# n = int(input())
# print(gia_tri_binh_phuong(n))

"""
Bài 06. Viết chương trình tính số Fibonacci thứ n, với n nhập vào từ bàn phím.

"""
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    a = 0
    b = 1

    for i in range(2, n + 1):
        a, b = b, a + b

    return b


# n = int(input("Nhập n: "))
# print(fibonacci(n))


"""
Bài 07. Viết một chương trình nhập vào một danh sách các số và tạo một danh sách mới chỉ gồm phần tử đầu tiên và 
cuối cùng của danh sách đó. Viết chương trình sử dụng hàm.
Ví dụ, nhập vào danh sách [5, 10, 15, 20, 25] thì kết quả trả về là danh sách [5, 25]

"""
def phantu_dau_va_cuoi(array):
    return [array[0], array[-1]]
# array = list(map(int, input().split(", ")))
# print(phantu_dau_va_cuoi(array))

"""
Bài 08. Viết một hàm nhận vào ba số thực và trả về số lớn nhất trong ba số. 
Lưu ý, không sử dụng hàm max() của Python.

"""
def so_lon_nhat(a, b, c):
    so_max = a
    if b > a and b > c:
        max = b
    elif c > b:
        so_max = c
    return so_max
# a, b, c = map(float, input().split())
# print(so_lon_nhat(a, b, c))

"""
Bài 09. Viết chương trình yêu cầu người dùng nhập vào một chuỗi và in ra màn hình thông báo chuỗi đó có phải là 
chuỗi palindrome hay không. (Chuỗi Palindrome là một chuỗi mà đọc xuôi và ngược đều như nhau, ví dụ ABCDCBA.)

"""
def check_palindrome(text):
    if text == text[::-1]:
        return text + " la chuoi  palindrome"
    return text + " khong phai la chuoi palindrome"
text = input("nhap chuoi palindrome: ")
print(check_palindrome(text))