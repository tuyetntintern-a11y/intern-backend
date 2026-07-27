"""
Bài 36.
Viết chương trình nhập vào 2 số nguyên dương a và b. Tìm ước số chung lớn nhất
của a và b.
Ví dụ:
● Input:
○ a = 30
○ b = 40
● Output:
○ UCLN = 10
○ BCNN = 120

Ước chung lớn nhất của hai số nguyên a và b là số nguyên dương lớn nhất mà a và b
chia hết.
Bội số chung nhỏ nhất của hai số nguyên a và b là số nguyên dương nhỏ nhất chia hết
cho cả a và b.
Nếu có số tự nhiên a chia hết cho số tự nhiên b thì ta gọi a là bội của b và b là ước của
a.

Ví dụ:
Tìm ước chung lớn nhất của 27 và 45?
UCLN(27,45)=9
"""
"""
def UCLN(x, y):
    while y != 0:
        x, y = y, x % y
        return x
"""
# def UCLN(x, y):
#     while x != y:
       
#         if x >= y:
#             x = x - y
#         else:
#             y = y - x
#     return x
# x, y= map(int, input().split())
# print(UCLN(x, y))

"""
Bài 37.
Viết chương trình nhập vào 2 số nguyên dương a và b. Tìm bội số chung nhỏ nhất
của a và b.
Ví dụ:
BCNN(6,10) = 30
Bội số của 6: 6 12 18 24 30 36 .......
Bội số của 10: 10 20 30 40 ....
"""

# def BCNN(a, b):
#     x, y = a, b
#     while b != 0:
#         a, b = b, a % b
#     return int((x * y) / a)
# a, b = map(int, input().split())
# print(BCNN(a, b))



"""
Bài 38.
Viết một hàm với đầu vào là tọa độ hai điểm trên mặt phẳng hai chiều và trả về
độ dài đoạn thẳng nối hai điểm đó.
Ví dụ:
line_length([15, 7], [22, 11]) ➞ 8.06
line_length([0, 0], [0, 0]) ➞ 0
line_length([0, 0], [1, 1]) ➞ 1.41
"""

# def line_length(point1, point2):
#     x1, y1 = point1
#     x2, y2 = point2
#     res = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
#     return round(res, 2)
# point1 = list(map(int, input().split()))
# point2 = list(map(int, input().split()))
# print(line_length(point1, point2))


"""
Bài 39.
Viết một hàm có tên capital_indexes. Hàm nhận một tham số duy nhất là một
chuỗi. Hàm của bạn sẽ trả về một danh sách tất cả các chỉ số (index) trong chuỗi
có chữ in hoa.
Ví dụ: gọi capital_indexes ("HeLlO") sẽ trả về danh sách [0, 2, 4].
"""
# def capital_indexes(text):
#     res = []
#     for char in range(len(text)):
#         if text[char].isupper():
#             res.append(char)
#     return res
# text = input()
# print(capital_indexes(text))

"""
Bài 40.
Kiểm tra đối xứng
Một chuỗi gọi là đối xứng khi đọc từ trái qua phải hay phải qua trái thì kết quả
giống nhau.
Ví dụ: Chuỗi "bob" và chuỗi "abba" là đối xứng
Chuỗi “abcd” không phải đối xứng vì "abcd" != "dcba".
Viết một hàm có tên palindrome kiểm tra tính đối xứng. Hàm trả True nếu đối
xứng, False nếu không đối xứng.
"""

# def palindrome(text):
#     for i in range(len(text) // 2):
#         if text[i] != text[len(text) - 1 - i]:
#             return False
       
#     return True

# text = input()
# print(palindrome(text))


"""
Bài 41.
Hãy viết chương trình nhập vào số nguyên dương n. Kiểm tra xem n có phải là số
chính phương hay không? (số chính phương là số khi lấy căn bậc 2 có kết quả là
nguyên). Hãy viết chương trình kiểm tra số chính phương.
"""
# import math
# def is_square(n):
#     if n>= 0 and math.sqrt(n)**2 == n:
#         return True
#     return False
# n = int(input())
# print(is_square(n))

"""
Bài 42.
Viết chương trình nhập vào số n.. xuất số đảo ngược của n đó..
Vd: n = 123 => 321
n = 4320 → 0234
"""
def reverse(num):
    num = list(num)
    indx = 0
    for n in range(len(num) // 2):
        indx = num[n]
        num[n] = num[len(num) - 1 - n]
        num[len(num) - 1 - n] = indx
    return "".join(num)
num = input()
print(reverse(num))


