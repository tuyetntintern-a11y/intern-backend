"""
# Bài 1: Tính tổng theo quy luật

Cho dãy số nguyên `a` gồm `n` phần tử:

```python
a = [a₁, a₂, ..., aₙ]
```

Tính giá trị:

[
a_1 - 2a_2 + 3a_3 - a_4 + 2a_5 - 3a_6 + ...
]

Trong đó:

* Dấu của các phần tử lần lượt là `+`, `-`, `+`, `-`, ...
* Hệ số lần lượt là `1, 2, 3, 1, 2, 3, ...` và được lặp lại.

---

"""
def tinh_gia_tri(array):
    result = 0
    for i in range(len(array)):
        he_so = i % 3 + 1
        if i % 2 == 0:
            result += he_so * array[i]
        else:
            result -= he_so * array[i]
    return result


"""
# Bài 2: Tìm các giá trị xuất hiện đúng một lần

Cho một dãy số nguyên `a`.

Tìm tất cả các giá trị **chỉ xuất hiện đúng một lần** trong dãy.

Ví dụ:

```python
a = [1, 2, 2, 3, 4, 4, 5]
```

Kết quả:

```python
[1, 3, 5]
```

---
"""
def gia_tri_mot_lan(a):
    arr = []
    for num in a:
        if a.count(num) == 1:
            arr.append(num)

    return arr

"""
# Bài 3: Kiểm tra hai dãy có cùng các giá trị

Cho hai dãy số nguyên `a` và `b`.

Kiểm tra xem hai dãy có chứa **cùng một tập hợp các giá trị** hay không.

Không quan trọng:

* Thứ tự xuất hiện của các phần tử.
* Số lần xuất hiện của mỗi giá trị.

Trả về `True` nếu hai dãy chứa cùng các giá trị, ngược lại trả về `False`.

Ví dụ:

```python
a = [1, 2, 2, 3]
b = [3, 1, 2]
```

Kết quả:

```text
True
```

Ví dụ:

```python
a = [1, 2, 3]
b = [1, 2, 4]
```

Kết quả:

```text
False
```

---
"""
def cung_gia_tri_hay_khong(a,b):
    a_set = set(a)
    b_set = set(b)
    if a_set == b_set:
        return True
    else:
        return False

"""
# Bài 4: Tính doanh thu theo sản phẩm

Cho một `dictionary` `prices` chứa tên sản phẩm và giá bán của từng sản phẩm.

Cho một danh sách `sold` chứa tên các sản phẩm đã bán.

Tính **tổng số tiền bán được của từng sản phẩm**.

Ví dụ:

```python
prices = {
    "apple": 10,
    "banana": 5,
    "orange": 8
}

sold = [
    "apple",
    "banana",
    "apple",
    "orange",
    "banana",
    "apple"
]
```

Kết quả:

```python
{
    "apple": 30,
    "banana": 10,
    "orange": 8
}
```

---
"""

def tinh_tong_tien(prices, sold):
    count = {}
    for item in sold:
        count[item] = count.get(item, 0) + 1


    result = {}

    for product in prices:
        if product in count:
            result[product] = prices[product] * count[product]

    return result


"""
# Bài 5: Tìm học sinh có nhiều điểm cao nhất

Cho một `dictionary` chứa tên học sinh và danh sách điểm của từng học sinh.

Một điểm được coi là **điểm cao** nếu điểm đó lớn hơn hoặc bằng `8`.

Tìm tên học sinh có **nhiều điểm cao nhất** và số lượng điểm cao của học sinh đó.

Ví dụ:

```python
students = {
    "An": [8, 9, 7, 10],
    "Bình": [5, 6, 7, 6],
    "Chi": [9, 10, 9, 8]
}
```

Kết quả:

```python
("Chi", 4)
```

Nếu có nhiều học sinh có cùng số lượng điểm cao nhất, trả về một trong những học sinh đó.

---

"""