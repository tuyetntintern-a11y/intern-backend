"""
Bài 21.
Làm game chọn nhóm. Có một danh sách gồm 8 người chơi, hãy lựa chọn ngẫu
nhiên 4 người chơi không trùng nhau để cho vào nhóm A, còn lại cho vào nhóm
B.
"""
def create_groups(players):
    import random
    group_a = random.sample(players, 4) 
    #lấy ngẫu nhiên nhiều phần tử từ một danh sách (hoặc tập hợp dữ liệu) mà không bị trùng lặp.

    group_b = [player for player in players if player not in group_a]
    return group_a, group_b
players = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah"]
group_a, group_b = create_groups(players)
print("Group A:", group_a)
print("Group B:", group_b)  


"""
Bài 22.
Tìm vị trí của giá trị chẵn đầu tiên trong mảng 1 chiều các số nguyên. Nếu
mảng không có giá trị chẵn thì sẽ trả về -1
"""
def find_first_even_index(arr):
    for a in range(len(arr)):
        if arr[a]%2 == 0:
            return a
    else:
        return -1
arr = list(map(int, input().split()))
print(find_first_even_index(arr))


"""
Bài 23.
Given the year number. You need to check if this year is a leap year. If it is, print
LEAP, otherwise print COMMON.
The rules in Gregorian calendar are as follows:
a year is a leap year if its number is exactly divisible by 4 and is not exactly
divisible by 100
a year is always a leap year if its number is exactly divisible by 400
"""
def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return "LEAP"
    else:
        return "COMMON" 
    
year = int(input())
print(is_leap_year(year))   


"""
Bài 24.
Viết chương trình tính tổng S = 1 + 1/2 + 1/3 + ...+ 1/n với n là số nguyên dương
nhập từ bàn phím.
"""
def calculate_sum(n):
    total = 0
    for i in range(1, n+1):
        total +=1/i
    return total

n = int(input())
print(calculate_sum(n))


"""
Bài 25.
Liệt kê tất cả các ước số của số nguyên dương n.
"""
def list_divisors(n):
    divisors = []
    for i in range(1,n+1):
        if n % i == 0:
            divisors.append(i)
    return divisors

n = int(input())
print(list_divisors(n))


"""
Bài 26.
Phân tích một số thành tích các thừa số nguyên tố

Input: n = 120
Output: 2 2 2 3 5

***Vì 2 là ước của 4, nên trước khi i tăng lên đến 4,
 thuật toán đã chia cho 2 nhiều lần nhất có thể. Do đó, n sẽ không còn chia hết cho 4 nữa.***

"""
def prime_factorization(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
           factors.append(divisor)
           n = n // divisor #( phep chia lấy phần nguyên)

        divisor += 1
    return factors

n = int(input())
print(*prime_factorization(n)) #Dấu * trong trường hợp này có nghĩa là giải nén một list hoặc tuple


"""
Bài 27.
Given a non-empty string and an int n, return a new string where the char at index
n has been removed. The value of n will be a valid index of a char in the original
string (i.e. n will be in the range 0..len(str)-1 inclusive).
missing_char('kitten', 1) → 'ktten'
missing_char('kitten', 0) → 'itten'
missing_char('kitten', 4) → 'kittn’
"""

def remove_char_at_index(st, n):
    return st[:n] + st[n+1:] #st[start:end] = Lấy từ start đến trước end.
st,n = input().split()
print(remove_char_at_index(st,int(n)))


"""
Bài 28.
Given a string, return a new string where the first and last chars have been
exchanged.
front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba’
"""
def renew_string(st):
    if len(st) <= 1:
        return st
    return st[-1] + st[1:-1] + st[0]

print(renew_string(input()))

""""
Bài 29.
You are driving a little too fast, and a police officer stops you. Write code to
compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big
ticket. If speed is 60 or less, the result is 0. If speed is between 61 and 80
inclusive, the result is 1. If speed is 81 or more, the result is 2. Unless it is your
birthday -- on that day, your speed can be 5 higher in all cases.
caught_speeding(60, False) → 0
caught_speeding(65, False) → 1
caught_speeding(65, True) → 0
"""

def caught_speeding(speed, is_birthday):
    if is_birthday:
        speed -= 5

    if speed <= 60:
        return 0
    elif speed <= 80:
        return 1
    else:
        return 2


speed, brth = input().split()

speed = int(speed)
brth = (brth.capitalize() == "True")

print(caught_speeding(speed, brth))

"""
Bài 30.
Given 3 int values, a b c, return their sum. However, if one of the values is 13
then it does not count towards the sum and values to its right do not count. So
for example, if b is 13, then both b and c do not count.

lucky_sum(1, 2, 3) → 6
lucky_sum(1, 2, 13) → 3
lucky_sum(1, 13, 3) → 1
"""
def lucky_sum(a,b,c):
    lst=[a,b,c]
    total=0
    for x in lst:
        if x == 13:
            break
        total += x
    return total
a,b,c=map(int,input().split)
print(lucky_sum(a,b,c))


"""
Bài 31.
Given an array length 1 or more of ints, return the difference between the largest
and smallest values in the array. Note: the built-in min(v1, v2) and max(v1, v2)
functions return the smaller or larger of two values.
big_diff([10, 3, 5, 6]) → 7
big_diff([7, 2, 10, 9]) → 8
big_diff([2, 10, 7, 2]) → 8
"""
def big_diff(nums):
    result= max(nums)-min(nums)
    return result
nums = list(map(int, input().split()))
print(big_diff(nums))

"""
Bài 32.
Tìm số chẵn cuối cùng trong mảng 1 chiều các số nguyên. Nếu mảng không có
giá trị chẵn thì trả về -1
"""
def last_even(nums):
    even = []
    for n in range(len(nums)):
        if nums[n] % 2 == 0:
            even.append(nums[n])
    if len(even) == 0:
        return -1
    return even[-1]
nums = list(map(int, input().split()))
    
print(last_even(nums))


"""
Bài 33.
Given a dictionary containing counts of both upvotes and downvotes, return what
vote count should be displayed. This is calculated by subtracting the number of
downvotes from upvotes.

Examples
get_vote_count({ "upvotes": 13, "downvotes": 0 }) ➞ 13
get_vote_count({ "upvotes": 2, "downvotes": 33 }) ➞ -31
get_vote_count({ "upvotes": 132, "downvotes": 132 }) ➞ 0
"""
def get_vote_count(dic):
    return dic["upvotes"] - dic["downvotes"]


upvotes, downvotes = map(int, input().split())

dic = {
    "upvotes": upvotes,
    "downvotes": downvotes
}

print(get_vote_count(dic))


"""
Bài 34.
Sắp xếp mảng 1 chiều tăng dần
Input: 3 5 2 8 10 7 12
Output: 2 3 5 7 8 10 12
Lưu ý: Không sử dụng hàm sort()
"""
def sort_arr(lst):
    res = [lst[0]]

    for n in range(1, len(lst)):
        for r in range(len(res)):
            if lst[n] < res[r]:
                res.insert(r, lst[n])
                break

            if r == len(res) - 1:
                res.append(lst[n])

    return res


lst = list(map(int, input().split()))
print(sort_arr(lst))


"""
Bài 35.
Đây là một chương trình tính tổng và trừ 2 số, các con tìm cách viết lại chương
trình này bằng cách sử dụng hàm.
if command == "add":
print("lets add some numbers")
input1 = input("Number 1>")
input2 = input("Number 2>")
number1 = int(input1)
number2 = int(input2)
result = number1 + number2
output = str(result)
print(input1 + " + " + input2 + " = " + output)
elif command == "subtract":
print("lets subtract some numbers")
input1 = input("Number 1>")
input2 = input("Number 2>")
number1 = int(input1)
number2 = int(input2)
result = number1 - number2
output = str(result)
print(input1 + " - " + input2 + " = " + output)
"""

def add():
    print("lets add some numbers")
    input1 = input("Number 1> ")
    input2 = input("Number 2> ")

    number1 = int(input1)
    number2 = int(input2)

    result = number1 + number2
    print(input1 + " + " + input2 + " = " + str(result))


def subtract():
    print("lets subtract some numbers")
    input1 = input("Number 1> ")
    input2 = input("Number 2> ")

    number1 = int(input1)
    number2 = int(input2)

    result = number1 - number2
    print(input1 + " - " + input2 + " = " + str(result))


command = input("Command (add/subtract): ")

if command == "add":
    add()
elif command == "subtract":
    subtract()
else:
    print("Invalid command")