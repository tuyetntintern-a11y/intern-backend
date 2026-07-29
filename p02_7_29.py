"""
Bài 43.
Cho số nguyên dương X, khi đảo ngược trật tự các chữ số của X ta sẽ thu được
một số nguyên dương Y, Y được gọi là số đảo ngược của X.
Ví dụ: X = 613 thì Y = 316 là số đảo ngược của X.
Số nguyên dương Y được gọi là số nguyên tố nếu nó chỉ có hai ước số là 1 và
chính nó, số 1 không phải là số nguyên tố.
Cho hai số nguyên dương P và Q (1≤P≤Q≤2*10^9; Q-P≤10^5).

Yêu cầu: Hãy tìm tất cả các số nguyên dương X nằm thỏa mãn P ≤ X ≤ Q và số
đảo ngược của số X là số nguyên tố.
Dữ liệu vào: Cho trong file văn bản TimSo.txt có cấu trúc như sau:
- Dòng 1: Ghi hai số nguyên dương P Q, hai số được ghi cách nhau ít nhất một
dấu cách.
Dữ liệu ra: Ghi ra file văn bản KetQua.txt trên nhiều dòng, mỗi dòng ghi một số
nguyên X tìm dược
Ví dụ:
TimSo.txt
10 19
KetQua.txt
11
13
14
16
17
"""
import math
def reverse_number(x): #ham doi so
    return int(str(x)[::-1])

def is_prime(n): #ham kiem tra co phai la so nguyen to hay khong
    
    if n < 2:
        return False

    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False

    return True

#doc file lay gia tri de xu ly
with open("TimSo.txt", "r", encoding="utf-8") as file:
    P, Q = map(int, file.readline().split())


numbers = []
for x in range(P, Q + 1):
    y = reverse_number(x)
    numbers.append((x, y)) # Lưu dưới dạng tuple để giữ cả X ban đầu và Y đảo ngược


results = []
for x, y in numbers:
    if is_prime(y): #su dung ham is_prime de kiem tra y va lay ket qua x de luu vao results
        results.append(str(x))  # Chuyển x thành chuỗi vì join() chỉ ghép được chuỗi


with open("KetQua.txt", "w", encoding="utf-8") as file: #ghi vao file tra ket qua
    file.write("\n".join(results))


"""
Bài 44.
Viết một chương trình chấp nhận chuỗi từ do người dùng nhập vào, phân tách
nhau
bởi dấu phẩy và in những từ đó thành chuỗi theo thứ tự bảng chữ cái, phân tách
nhau bằng dấu phẩy.
Giả sử đầu vào được nhập là: without,hello,bag,world, thì đầu ra sẽ
là: bag,hello,without,world

| Cách              | Kết quả trả về      | Danh sách ban đầu    |
| ----------------- | ------------------- | -------------------- |
| `sorted(numbers)` | List mới đã sắp xếp | Không thay đổi       |
| `numbers.sort()`  | `None`              | Bị sắp xếp trực tiếp |


"""
def sort_words(text):
    return ",".join(sorted(text))
# text = input().split(",")
# print(sort_words(text))

"""
Bài 45.
Write a function named add_dots that takes a string and adds "." in between each
letter. For example, calling add_dots("test") should return the string "t.e.s.t".
Then, below the add_dots function, write another function named remove_dots
that removes all dots from a string. For example, calling remove_dots("t.e.s.t")
should return "test".
If both functions are correct, calling remove_dots(add_dots(string)) should return
back the original string for any string.
"""
def add_dots(text):
    return ".".join(text)
def remove_dots(text):
    return text.replace(".", "")
# text = input()
# text2 = add_dots(text)
# print(text2)
# print(remove_dots(text2))


"""
Bài 46.
Viết một chương trình chấp nhận đầu vào là một câu, đếm số chữ cái và chữ số
trong câu đó. Giả sử đầu vào sau được cấp cho chương trình:
Input: hello world! 123
Thì đầu ra sẽ là:
Số chữ cái là: 10
Số chữ số là: 3
"""
def count_letters_and_digits(text):
    letters = 0
    digits = 0
    for char in text:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1
    return letters, digits
# text = input()
# letters, digits = count_letters_and_digits(text)

# print("Số chữ cái là: ", letters)
# print("Số chữ số là: ", digits)

