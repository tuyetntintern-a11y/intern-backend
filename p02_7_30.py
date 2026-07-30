"""
Bài 47.
Thiết kế trò chơi đoán từ vựng như chiếc nón kỳ diệu.
Máy tính sẽ hiện các ô chữ tương ứng với số chữ cái của từ bí mật.
Ví dụ:
Tên một loài động vật bơi ở biển có 4 chữ cái ?
Từ bí mật là Fish gồm 4 chữ cái
Welcome to Hangman!
_ _ _ _
Guess your letter: I
Người dùng nhập từ ký tự muốn đoán. Sau đó chương trình sẽ hiện tất cả các ký
tự đó nếu có trong từ bí mật.
_ I _ _
Trò chơi chỉ cho phép bạn đoán sai tối đa 5 lần, nếu quá 5 lần thì chương trình in
ra từ bí mật.
"""

import random


QUESTION_DATA = (
    ("Tên một loài động vật bơi ở biển có 4 chữ cái?", "fish"),
    ("Một loại trái cây màu đỏ có 5 chữ cái?", "apple"),
    ("Một loài động vật lớn sống ở biển có 5 chữ cái?", "whale"),
    ("Một loài động vật sống trong rừng có 5 chữ cái?", "tiger")
)


def choose_question(question_data):
    selected = random.choice(question_data)
    return selected


def play_hangman(question, secret_word):
    print("Welcome to Hangman!")
    print(question)

    secret_word = secret_word.lower()
    display_word = ["_"] * len(secret_word)

    wrong_guesses = 0
    max_wrong = 5
    guessed_letters = []

    while wrong_guesses < max_wrong and "_" in display_word:
        print("\n" + " ".join(display_word))
        print("Số lần đoán sai:", wrong_guesses, "/", max_wrong)

        letter = input("Guess your letter: ").lower()

        # Kiểm tra người dùng chỉ nhập một chữ cái
        if len(letter) != 1 or not letter.isalpha():
            print("Vui lòng nhập đúng một chữ cái.")
            continue

        # Kiểm tra chữ đã được đoán trước đó chưa
        if letter in guessed_letters:
            print("Bạn đã đoán chữ này rồi.")
            continue

        guessed_letters.append(letter)

        # Kiểm tra chữ có trong từ bí mật
        if letter in secret_word:
            for i in range(len(secret_word)):
                if secret_word[i] == letter:
                    display_word[i] = letter.upper()

            print("Chính xác!")
        else:
            wrong_guesses += 1
            print("Không có chữ này trong từ bí mật.")

    print("\n" + " ".join(display_word))

    if "_" not in display_word:
        print("Chúc mừng! Bạn đã đoán đúng.")
    else:
        print("Bạn đã đoán sai 5 lần.")

    print("Từ bí mật là:", secret_word.upper())


# question, secret_word = choose_question(QUESTION_DATA)
# play_hangman(question, secret_word)


"""
Bài 48.
Đọc nội dung của một file INPUT.txt có cấu trúc như sau:
● Dòng đầu tiên ghi số lượng số nguyên có trong file
● Dòng tiếp theo là một dãy số nguyên
Ví dụ: Nội dung file INPUT.txt
8
1 2 3 4 5 6 7 8
Ghi vào file KETQUA_2.txt các số nguyên tố có trong mảng
Ví dụ: Kết quả file KETQUA.txt
2 3 5 7

(Để kiểm tra số n có phải số nguyên tố không:

Nếu n < 2 → không phải số nguyên tố.
Kiểm tra các số từ 2 đến căn bậc hai của n.
Nếu tìm thấy một số chia hết n → n không phải số nguyên tố.
Nếu kiểm tra hết mà không tìm thấy → n là số nguyên tố.)

"""
import math
def find_primes(numbers):
    results = []
    for i in range(len(numbers)):
        if numbers[i] < 2:
            continue
        is_prime = True
        for num in range(2, math.isqrt(numbers[i]) + 1):
            if numbers[i] % num == 0:
                    is_prime = False
                    break
        if is_prime:
            results.append(numbers[i])
    return results
with open("INPUT.txt", "r", encoding="utf-8") as file:
    quantity = int(file.readline())
    numbers = list(map(int, file.read().split()))

if quantity != len(numbers):
    print("Số lượng số nguyên không khớp với dữ liệu trong file.")    

results = find_primes(numbers)

with open ("KETQUA_2.txt", "w", encoding="utf-8") as file:
    file.write(" ".join(map(str, results))) ## join() ghép các phần tử chuỗi trong list thành một chuỗi

"""
Bài 49.
Cho một dữ liệu file input2.txt
Hello! Welcome to Ha noi
Ha noi is the capital city of Vietnam
Good Luck!
Các con hãy lập trình đọc nội dung của file tìm ra từ đầu tiên có độ dài lớn nhất
trong file trên. Các từ trong file sẽ cách nhau một khoảng trắng.
Kết quả: Từ Welcome có độ dài 7 ký tự.
"""
def find_first_longest_word(words):
    longest_word = ""
    max_length = 0

    for word in words:
        count_char = 0

        for char in word:
            count_char += 1

        if count_char > max_length:
            max_length = count_char
            longest_word = word

    return longest_word, max_length
with open ("input2.txt", "r", encoding= "utf-8") as file:
    words = file.read().split()
longest_word, max_length = find_first_longest_word(words)
# print("Từ " + longest_word + " có độ dài " + str(max_length) + " ký tự.")



"""
Bài 50.
Viết một hàm đếm tần số xuất hiện mỗi từ trong một file. Ghi ra file trên mỗi
dòng là từ và tần số xuất hiện của từ đó.
vidu file input2.txt
"""
def count_word_frequencies(words):
    word_frequencies = {}
    for word in words:
        if word in word_frequencies:
            word_frequencies[word] += 1
        else:
            word_frequencies[word] = 1
    return word_frequencies
with open ("input2.txt", "r", encoding= "utf-8") as file:
    words = file.read().split()
print(count_word_frequencies(words))
