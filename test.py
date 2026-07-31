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
