
"""
Bài 1.
Cho một số nguyên, in "YES" nếu chữ số cuối của nó là 7 và in "NO" nếu không.
Ví dụ:
127 → YES
333 → NO
"""
# #bai 1:
# n = int(input())
# if n % 10 == 7:
#     print("YES")
# else:
#     print("NO")


"""
Bài 2.
Cho biết tọa độ của ba điểm A, B, C trên một đoạn thẳng. In khoảng cách từ điểm
A đến điểm gần nó nhất.
Ví dụ:
10
35
30
Kết quả: 20
"""
# #bai2
# a = int(input())
# b = int(input())
# c = int(input())
# distances = [abs(a - b), abs(a - c)]
# print(min(distances))

"""
Bài 3.
Viết chương trình tính tổng các số trong một danh sách
Ví dụ:
Input: [2, 5, 8, 10, 12]
Output: Sum = 37
"""

# #bai3
# numbers = list(map(int, input().split()))
# print("Sum =", sum(numbers))


"""
Bài 4.
Viết game đoán số may mắn (guess the number)
Máy tính nghĩ một số random từ 1 cho đến 15 và hỏi bạn đoán. Máy tính sẽ nói
cho bạn khi bạn đoán sai là số may mắn là phải lớn hơn hoặc nhỏ hơn. Bạn sẽ
chiến thắng nếu bạn đoán đúng số đó trong 5 lượt chơi.
Gợi ý:
import random
# random number from 1 to 15
random_number = random.randint(1, 15)
Máy tính sẽ tạo một số ngẫu nhiên từ 1 cho đến 15
Input/Output:
Tôi đang nghĩ một số giữa 1 và 15. Bạn hãy đoán số may mắn đó giúp tôi.
Số may mắn đó là: 10
Số bạn đoán phải nhỏ hơn 10
Số may mắn đó là: 2
Số bạn đoán phải lớn hơn: 2
Số may mắn đó là: 4
Chúc mừng bạn đã chiến thắng. Bạn đã đoán đúng sau 2 lượt chơi.
- Nếu sau 5 lượt chơi bạn không đoán được thì kết thúc chương trình và in ra
Bạn đã không may mắn, đây là số 4
"""
# #bai4
# import random
# print("Tôi đang nghĩ một số giữa 1 và 15. Bạn hãy đoán số may mắn đó giúp tôi.")

# random_number = random.randint(1, 15)
# guess_count = 0
# for i in range(5):
    
#     guess = int(input("Số may mắn đó là: "))
#     guess_count += 1
#     if guess < random_number:
#         print(f"Số bạn đoán phải lớn hơn {guess}")
#     elif guess > random_number:
#         print(f"Số bạn đoán phải nhỏ hơn {guess}")  
#     else:
#         print(f"Chúc mừng bạn đã chiến thắng. Bạn đã đoán đúng sau {guess_count} lượt chơi.")
#         break
# else:
#     print(f"Bạn đã không may mắn, đây là số {random_number}")
    


"""

Bài 5.
Một cửa hàng sẽ giảm giá 10% nếu tổng chi phí mua hàng lớn hơn 10.000
Người dùng về số lượng từ bàn phím
Giả sử, một đơn vị mặt hàng sẽ có giá 100 đồng.
In tổng chi phí hóa đơn cho người dùng.
Ví dụ:
Input: 120
Output: 10800
Input: 20
Output: 2000
"""
# #bai5
# quantity=int(input())
# total_cost = quantity * 100
# if total_cost > 10000:
#     total_cost *= 0.9  # Apply 10% discount
#     print(int(total_cost))
# else:
#     print(int(total_cost))   




"""
Bài 6.
Viết chương trình in ra tất cả các số chẵn trong một danh sách
Ví dụ:
Input: [2, 5, 8, 10, 12]
Output: 2, 8, 10, 12
"""
# #bai6
# numbers = list(map(int, input().split()))
# even = []
# for num in numbers:
#     if num % 2 == 0:
#         even.append(num)

# print(", ".join(map(str, even)))


"""

Bài 7.
Viết một chương trình tìm ra số lớn nhất của một danh sách mà không sử dụng
hàm max()
Ví dụ:
Input: [2, 5, 8, 10, 12]
Output: 12
"""
# #bai7
# numbers = list(map(int, input().split()))
# max_num = numbers[0]
# for num in numbers:
#     if num > max_num:
#         max_num = num
# print(max_num)


"""
Bài 8.
Cho một danh sách các số, hãy tìm và in tất cả các phần tử lớn hơn phần tử trước
đó.
Ví dụ1:
Input:
1 5 2 4 3

5 4

Ví dụ 2:
Input:
5 5 5 5 5

Output:
5 5 5 5
"""

# #bai8
# numbers = list(map(int, input().split()))
# result = []
# for i in range(len(numbers) - 1):
#     if numbers[i + 1] >= numbers[i]:
#         result.append(numbers[i + 1])
# print(" ".join(map(str, result)))

"""
Bài 9.
Viết một chương trình xóa tất cả phần tử lặp lại (trùng lặp) ra khỏi danh sách.
Ví dụ:
Input: [1, 3, 5, 6, 3, 5, 6, 1]
Output: [1, 3, 5, 6]
"""
# #bai9
# numbers=list(map(int, input().split()))
# unique_numbers = []
# for num in numbers:
#     if num not in unique_numbers:
#         unique_numbers.append(num)
# print(", ".join(map(str, unique_numbers)))  


"""

Bài 10.
Get first, second best scores from the list.
List may contain duplicates.
Input: [86,86,85,85,85,83,23,45,84,1,2,0]
Output: should get 86, 85
"""

# #bai10
# numbers = list(map(int, input().split()))
# first_best = second_best = float('-inf')
# for num in numbers:
#     if num > first_best:
#         second_best = first_best
#         first_best = num
#     elif first_best > num > second_best:
#         second_best = num
# print(first_best, second_best)


"""
Bài 11.
Given an array length 1 or more of ints, return the difference between the largest
and smallest values in the array. Note: the built-in min(v1, v2) and max(v1, v2)
functions return the smaller or larger of two values.
big_diff([10, 3, 5, 6]) → 7
big_diff([7, 2, 10, 9]) → 8
big_diff([2, 10, 7, 2]) → 8
"""
# #bai11
# numbers = list(map(int, input().split()))
# print(max(numbers) - min(numbers))



"""
bai 12:
Viết một chương trình in ra các số chia hết cho 7 nhưng không chia hết cho 5
nằm trong khoảng 100 cho đến 1000 (tính cả 100 và 1000).
Kết quả: In trên một dòng và cách nhau bởi dấu phẩy.
"""
# ##bai12
# results = []
# for i in range(105, 1001, 7):
#     if i % 5 != 0:
#         results.append(i)
# print(", ".join(map(str, results)))

"""
Bài 13.
Viết một chương trình in tất cả các số nguyên tố nhỏ hơn n. Với n là số nguyên
dương nhập từ bàn phím.
Ví dụ:
n = 12
Kết quả:
2 3 5 7 11
"""
# #bai13
# n = int(input())
# primes = [1, 2]
# for i in range(3, n, 2):
#     is_prime = True
#     for j in range(2, int(i ** 0.5) + 1):
#         if i % j == 0:
#             is_prime = False
#             break
#     if is_prime:
#         primes.append(i)
# print(" ".join(map(str, primes)))



# """
# Bài 14.
# Cho một danh sách số nguyên: [5, 10, 15, 20, 25, 46]
# Tìm giá trị lớn nhất và nhỏ nhất của danh sách.
# Gợi ý:
# Không được sử dụng hàm max() và min()
# """
# #bai14
# numbers = [5, 10, 15, 20, 25, 46]
# max_num = numbers[0]
# min_num = numbers[0]

# for num in numbers:
#     if num > max_num:
#         max_num = num
#     if num < min_num:
#         min_num = num

# print("Max:", max_num)
# print("Min:", min_num)



"""
Bài 15.
Viết chương trình nhập vào bán kính đường tròn, tính toán và in ra chu vi và diện
tích hình tròn.
"""
#bai15
import math
radius = float(input("Nhập bán kính đường tròn: "))
perimeter = 2 * math.pi * radius
area = math.pi * radius ** 2
print(f"Chu vi hình tròn: {perimeter}")
print(f"Diện tích hình tròn: {area}")