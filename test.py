"""
1. Cho dãy số a gồm các phần tử a1, a2, a3,...
Hãy tính giá trị của biểu thức: a1 - a2 + a3 - a4 +...
"""
def tinh_array(array):
    res = 0
    for i in range(len(array) ):
        if i % 2 == 0:
            res = res + array[i]
        if i % 2 != 0:
            res = res - array[i]

    return res
array = [1, 2, 3, 5, 6, 9]
print(tinh_array(array))

"""
2. Cho 1 dãy số a. Hãy trả về dãy gồm các 
phần tử chia hết cho 2, 3 và 5 nhưng không chia hết cho 4.
"""
def find_numbers(array):
    result = []
    for i in range(len(array)):
        if array[i] % (2*3*5) == 0 and array[i] % 4 != 0:
            result.append(array[i])

    return result
array = [1,3,5,7,9,30,60]
print(*find_numbers(array))
# dau * de giai nen, tuc la chi lay phan tu ben trong list


"""

3.
  | 1 | 2 | 3 | 4 | 5 | 6
-------------------------
1 | x | x | o | o | x | x
-------------------------
2 | x | x | o | o | x | x
-------------------------
3 | x | o | o | o | o | x
-------------------------
4 | x | x | o | o | x | x
-------------------------
5 | x | x | o | o | x | x
-------------------------
6 | x | x | o | o | x | x
Cho 2 số nguyên r và c với 1 <= r, c <= 6. Nếu ô ở hàng r và cột c trong bảng cố định trên là 'o' 
thì trả về True, là 'x' thì trả về False.

"""
def check_matrix(r, c):
    if c == 3 or c == 4 or (r == 3 and ((c == 2) or (c == 5))):
        return True
    return False
    
"""
4. Cho 3 số nguyên n, m, r > 0. Trả về dãy số gồm tất cả các số nguyên nhỏ hơn n và khi chia 
cho m thì có số dư bằng r.

"""
def find_number(n, m, r):
    result = []
    for i in range(1, n):
        if i % m == r:
            result.append(i)
    return result
"""
5. Bạn được cho:

Một mảng nguyên dương a biểu thị mức độ tham lam của mỗi đứa trẻ.
Một mảng nguyên dương b biểu thị kích thước của các chiếc bánh quy.

Mỗi đứa trẻ chỉ có thể nhận tối đa một chiếc bánh quy.

Một đứa trẻ được xem là hài lòng nếu kích thước của chiếc bánh quy được phát cho nó lớn hơn hoặc bằng 
mức độ tham lam của đứa trẻ đó.

Hãy trả về số lượng lớn nhất các đứa trẻ có thể được làm hài lòng.

"""


def dua_tre_hai_long(arrayA, arrayB):
    arrayA = sorted(arrayA)
    arrayB= sorted(arrayB)
    child = 0
    count = 0

    for cookie in arrayB:
        if child < len(arrayA) and cookie >= arrayA[child]:
            count += 1
            child += 1

    return count
                

    

